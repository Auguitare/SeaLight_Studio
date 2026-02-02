import photometry as p
import colorimetry as c

import pandas
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure



class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analyse Photométrique et Colorimétrique")

        # Variables globales pour les fichiers
        self.fichier_selectionne = None
        self.dernier_dossier = "."

        # Créer le système d'onglets
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        self.tabview.add("Photométrie")
        self.tabview.add("Colorimétrie")

        # Configurer chaque onglet
        self.setup_photometry_tab()
        self.setup_colorimetry_tab()

    # ========== ONGLET PHOTOMÉTRIE ==========
    def setup_photometry_tab(self):
        tab = self.tabview.tab("Photométrie")

        # Configuration de la grille
        tab.grid_rowconfigure(0, weight=0)
        tab.grid_rowconfigure(1, weight=0)
        tab.grid_rowconfigure(2, weight=0)
        tab.grid_rowconfigure(3, weight=1)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=1)
        tab.grid_columnconfigure(2, weight=1)

        # Variables
        self.var_secteur = ctk.StringVar(value="Vide")
        self.var_range = ctk.StringVar(value="2")
        self.var_angle = ctk.IntVar(value=0)
        self.var_decalage = ctk.DoubleVar(value=0.0)

        # Figure matplotlib
        self.fig_photo = Figure(figsize=(8, 5), dpi=100)
        self.ax_photo = self.fig_photo.add_subplot(111)

        # Ligne 0
            # colone 0 - secteur
        secteur_menu = ctk.CTkOptionMenu(
            tab,
            values=["Vide", "Hune", "Poupe", "Babord", "Tribord"],
            variable=self.var_secteur,
        )
        secteur_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            # colone 1 - angle (0°)
        rb_0 = ctk.CTkRadioButton(tab, text="0°", variable=self.var_angle, value=0)
        rb_0.grid(row=0, column=1, padx=10, pady=5, sticky="w")

            # colone 2 - décalage d'angle
        label_decalage = ctk.CTkLabel(tab, text="Décalage (°):")
        label_decalage.grid(row=0, column=2, padx=(10, 0), pady=5, sticky="w")
        entry_decalage = ctk.CTkEntry(
            tab,
            textvariable=self.var_decalage,
            width=50,
        )
        entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")

        # Ligne 1
            # colone 0 - distance de visibilité
        range_menu = ctk.CTkOptionMenu(
            tab,
            values=["1", "2", "3", "4", "5", "6"],
            variable=self.var_range,
        )
        range_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")

            # colone 1 - angle +/-25°
        rb_25 = ctk.CTkRadioButton(
            tab, text="+/-25°", variable=self.var_angle, value=25
        )
        rb_25.grid(row=1, column=1, padx=10, pady=5, sticky="w")

            # colone 2 - tracer le graphique
        button_trace_photo = ctk.CTkButton(
            tab, text="Tracer le graphique", command=p.trace_photometry
        )
        button_trace_photo.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        #Ligne 2
            # colone 0 et 1 - select file
        button_fichier_photo = ctk.CTkButton(
            tab,
            text="Choisir un fichier",
            command=lambda: self.choisir_fichier("photo"),
        )
        button_fichier_photo.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.label_fichier_photo = ctk.CTkLabel(tab, text="Aucun fichier sélectionné")
        self.label_fichier_photo.grid(
            row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w"
        )

        # Ligne 3 - graphic place
        self.photo_plot_frame = ctk.CTkFrame(tab)
        self.photo_plot_frame.grid(
            row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

        # Key bindings
        self.bind("<Return>", lambda event: p.trace_photometry())
        self.bind("<KP_Enter>", lambda event: p.trace_photometry())


    # ========== ONGLET COLORIMÉTRIE ==========
    def setup_colorimetry_tab(self):
        tab = self.tabview.tab("Colorimétrie")

        # Configuration de la grille
        tab.grid_rowconfigure(0, weight=0)
        tab.grid_rowconfigure(1, weight=0)
        tab.grid_rowconfigure(2, weight=1)
        tab.grid_columnconfigure(0, weight=1)
        tab.grid_columnconfigure(1, weight=1)
        tab.grid_columnconfigure(2, weight=1)

        # Figure matplotlib
        self.fig_color = Figure(figsize=(8, 5), dpi=100)
        self.ax_color = self.fig_color.add_subplot(111)

        # Widgets - Ligne 0
        label_info = ctk.CTkLabel(
            tab,
            text="Colorimétrie - Diagramme de chromaticité (X, Y)",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        label_info.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # Widgets - Ligne 1
        button_fichier_color = ctk.CTkButton(
            tab,
            text="Choisir un fichier",
            command=lambda: self.choisir_fichier("color"),
        )
        button_fichier_color.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.label_fichier_color = ctk.CTkLabel(tab, text="Aucun fichier sélectionné")
        self.label_fichier_color.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        button_trace_color = ctk.CTkButton(
            tab, text="Tracer le graphique", command=c.trace_colorimetry
        )
        button_trace_color.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        # Zone du graphe - Ligne 2
        self.color_plot_frame = ctk.CTkFrame(tab)
        self.color_plot_frame.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )

    # ========== FONCTIONS COMMUNES ==========
    def choisir_fichier(self, tab_type):
        """Choisir un fichier de données"""
        self.fichier_selectionne = filedialog.askopenfilename(
            title="Choisir un fichier de données",
            filetypes=[
                ("Fichiers texte", "*.txt"),
                ("Fichiers de calcul", "*.csv"),
                ("Tous les fichiers", "*.*"),
            ],
        )

        if self.fichier_selectionne:
            self.dernier_dossier = "/".join(self.fichier_selectionne.split("/")[:-1])
            nom_fichier = self.fichier_selectionne.split("/")[-1]

            if tab_type == "photo":
                self.label_fichier_photo.configure(
                    text=f"Fichier sélectionné : {nom_fichier}"
                )
            else:
                self.label_fichier_color.configure(
                    text=f"Fichier sélectionné : {nom_fichier}"
                )
        else:
            if tab_type == "photo":
                self.label_fichier_photo.configure(text="Aucun fichier sélectionné")
            else:
                self.label_fichier_color.configure(text="Aucun fichier sélectionné")

    def read_file(self):
        """Lit le fichier sélectionné"""
        if not self.fichier_selectionne:
            tk.messagebox.showwarning(
                "Avertissement", "Veuillez d'abord choisir un fichier à ouvrir."
            )
            return None

        lignes_a_sauter = set()
        with open(self.fichier_selectionne, "r") as f:
            lignes = f.readlines()
            for i, ligne in enumerate(lignes):
                if "Angle" in ligne:
                    lignes_a_sauter.update(range(0, i), range(i + 1, i + 3))
                    break

        data_file = pandas.read_csv(
            self.fichier_selectionne,
            sep=";",
            skiprows=lambda x: x in lignes_a_sauter,
            skipfooter=2,
            engine="python",
            usecols=["Angle °", "cd", "X", "Y", "lux"],
        )
        return data_file

    def display_plot(self, frame, fig, plot_type):
        """Affiche un graphique matplotlib dans une frame"""
        # Nettoyer la frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Canvas matplotlib
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Toolbar
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
