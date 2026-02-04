"""
Script principal de l'application d'analyse des données photométriques et colorimétriques.
Ce module initialise l'interface utilisateur avec customtkinter, gère les onglets de navigation,
le chargement des fichiers de données et coordonne l'affichage des graphiques.
"""
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import file_orga as f
import tab_photo as p
import tab_colo as c


class Application(ctk.CTk):
    """
    Classe principale de l'application d'analyse des données photométriques.
    Gère l'interface utilisateur, le chargement des fichiers et l'affichage des graphiques.
    """
    def __init__(self):
        """
        Initialise la fenêtre principale, les onglets et les éléments de l'UI.
        """
        super().__init__()

        self.file_choosen = None
        self.data = None

        self.title("Analyse des données photométrique des feux de navigation")

        # onglets
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=0, pady=0, fill="both", expand=True)
        self.tabview.add("Photométrie")
        self.tabview.add("Colorimétrie")
        self.tabview.set("Photométrie")

        tab_photo = self.tabview.tab("Photométrie")
        tab_color = self.tabview.tab("Colorimétrie")

        # ========== UI Photometrie ==========
        # Configuration de la grille
        tab_photo.grid_rowconfigure(0, weight=0)
        tab_photo.grid_rowconfigure(1, weight=0)
        tab_photo.grid_rowconfigure(2, weight=0)
        tab_photo.grid_rowconfigure(3, weight=1)
        tab_photo.grid_columnconfigure(0, weight=1)
        tab_photo.grid_columnconfigure(1, weight=1)
        tab_photo.grid_columnconfigure(2, weight=1)

        # Variable de la page
        self.var_secteur = ctk.StringVar(value="Vide")
        self.var_range = ctk.StringVar(value="2")
        self.var_angle = ctk.IntVar(value=0)
        self.var_decalage = tk.DoubleVar(value=0.0)

        ## Gestion des bouton/menu
        # position du feux
        secteur_menu = ctk.CTkOptionMenu(
            tab_photo,
            values=["Vide", "Hune", "Poupe", "Babord", "Tribord"],
            variable=self.var_secteur,
        )
        secteur_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Puissance du feux
        range_menu = ctk.CTkOptionMenu(
            tab_photo,
            values=["1", "2", "3", "4", "5", "6"],
            variable=self.var_range,
        )
        range_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Radio bouton d'angle
        rb_0 = ctk.CTkRadioButton(
            tab_photo, text="0°", variable=self.var_angle, value=0
        )
        rb_25 = ctk.CTkRadioButton(
            tab_photo, text="+/-25°", variable=self.var_angle, value=25
        )
        rb_0.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        rb_25.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Bouton de traçage de graphique
        button_trace_photo = ctk.CTkButton(
            tab_photo, text="Tracer le graphique", command=self.trace_photo
        )
        button_trace_photo.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        # Bouton de choix de fichier
        button_fichier = ctk.CTkButton(
            tab_photo, text="Choisir un fichier", command=self.file
        )
        button_fichier.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.label_fichier_photo = ctk.CTkLabel(
            tab_photo, text="Aucun fichier sélectionné"
        )
        self.label_fichier_photo.grid(
            row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w"
        )

        # Entrée de dcalage
        entry_decalage = ctk.CTkEntry(
            tab_photo, textvariable=self.var_decalage, width=50
        )
        entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        label_decalage = ctk.CTkLabel(tab_photo, text="Décalage [°]:")
        label_decalage.grid(row=0, column=2, padx=(10, 0), pady=5)

        # == GRAPHIQUE PHOTOMÉTRIE ==
        self.frame_graph_photo = ctk.CTkFrame(tab_photo)
        self.frame_graph_photo.grid(
            row=3, column=0, columnspan=3, padx=0, pady=0, sticky="nsew"
        )

        # figure matplotlib
        self.fig_photo = Figure(figsize=(8, 5))
        self.ax_photo = self.fig_photo.add_subplot(111)
        p.trace_limit(
            self.ax_photo,
            self.var_secteur.get(),
            int(self.var_range.get()),
            self.var_angle.get(),
        )

        # Intégration
        self.canvas_photo = FigureCanvasTkAgg(
            self.fig_photo, master=self.frame_graph_photo
        )
        self.canvas_photo.draw()
        self.canvas_photo.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_photo, self.frame_graph_photo)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        # ========== UI Colorimetrie ==========
        # Configuration de la grille
        tab_color.grid_rowconfigure(0, weight=0)
        tab_color.grid_rowconfigure(1, weight=0)
        tab_color.grid_rowconfigure(2, weight=1)
        tab_color.grid_columnconfigure(0, weight=1)
        tab_color.grid_columnconfigure(1, weight=1)
        tab_color.grid_columnconfigure(2, weight=1)

        # === Ligne 0 ===
        label_info = ctk.CTkLabel(
            tab_color,
            text="Colorimétrie - Diagramme de chromaticité (X, Y)",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        label_info.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # === Ligne 1 ===
        button_fichier = ctk.CTkButton(
            tab_color, text="Choisir un fichier", command=self.file
        )
        button_fichier.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.label_fichier_color = ctk.CTkLabel(
            tab_color, text="Aucun fichier sélectionné"
        )
        self.label_fichier_color.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        button_trace_color = ctk.CTkButton(
            tab_color, text="Tracer le graphique", command=self.trace_color
        )
        button_trace_color.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        # == GRAPHIQUE Colorimétrie ==
        self.frame_graph_color = ctk.CTkFrame(tab_color)
        self.frame_graph_color.grid(
            row=3, column=0, columnspan=3, padx=0, pady=0, sticky="nsew"
        )

        # figure matplotlib
        self.fig_color = Figure(figsize=(8, 5))

        self.ax_color = self.fig_color.add_subplot(111)
        c.trace_limit(self.ax_color)

        # Intégration
        self.canvas_color = FigureCanvasTkAgg(
            self.fig_color, master=self.frame_graph_color
        )
        self.canvas_color.draw()
        self.canvas_color.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas_color, self.frame_graph_color)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        # déclaration des key bindings
        self.bind("<Return>", self.input_handle)
        self.bind("<KP_Enter>", self.input_handle)

    def trace_photo(self):
        """
        Lit les données du fichier sélectionné et trace le graphique de photométrie.
        Affiche un avertissement si aucun fichier n'est sélectionné.
        """
        if not self.file_choosen:
            tk.messagebox.showwarning(
                "Avertissement", "Veuillez d'abord choisir un fichier à ouvrir."
            )

        else:
            self.data = f.read_file(self.file_choosen)
            p.trace_graph(self.data, self.ax_photo, self.var_decalage)
            p.trace_limit(
                self.ax_photo,
                self.var_secteur.get(),
                int(self.var_range.get()),
                self.var_angle.get(),
            )
            self.canvas_photo.draw()

    def trace_color(self):
        """
        Lit les données du fichier sélectionné et trace le graphique de colorimétrie.
        Affiche un avertissement si aucun fichier n'est sélectionné.
        """
        if not self.file_choosen:
            tk.messagebox.showwarning(
                "Avertissement", "Veuillez d'abord choisir un fichier à ouvrir."
            )

        else:
            self.data = f.read_file(self.file_choosen)
            c.trace_graph(self.data, self.ax_color)
            c.trace_limit(self.ax_color)
            self.canvas_color.draw()

    def file(self):
        """
        Ouvre une boîte de dialogue pour sélectionner
        un fichier et met à jour les labels d'information.
        """
        self.file_choosen = f.choisir_fichier()
        if not self.file_choosen:
            return
        name = f"Fichier sélectionné : {'/'.join(self.file_choosen.split('/')[-3:])}"
        self.label_fichier_photo.configure(text=name)
        self.label_fichier_color.configure(text=name)

    def input_handle(self, _):
        """
        Gère l'événement de pression sur la touche Entrée pour lancer le traçage
        du graphique correspondant à l'onglet actif.

        Args:
            event: L'événement tkinter capturé.
        """
        current_tab = self.tabview.get()
        if current_tab == "Photométrie":
            self.trace_photo()
        elif current_tab == "Colorimétrie":
            self.trace_color()


app = Application()
app.mainloop()
