import pandas
import tkinter as tk
import customtkinter as ctk


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analyse des données photométrique feux de navigation")

        # onglets
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
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
        var_secteur = ctk.StringVar(value="Vide")
        var_range = ctk.StringVar(value="2")
        var_angle = ctk.IntVar(value=0)
        var_decalage = tk.DoubleVar(value=0.0)

        ## Gestion des bouton/menu
        # position du feux
        secteur_menu = ctk.CTkOptionMenu(
            tab_photo,
            values=["Vide", "Hune", "Poupe", "Babord", "Tribord"],
            variable=var_secteur,
        )
        secteur_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Puissance du feux
        range_menu = ctk.CTkOptionMenu(
            tab_photo,
            values=["1", "2", "3", "4", "5", "6"],
            variable=var_range,
        )
        range_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Radio bouton d'angle
        rb_0 = ctk.CTkRadioButton(tab_photo, text="0°", variable=var_angle, value=0)
        rb_25 = ctk.CTkRadioButton(
            tab_photo, text="+/-25°", variable=var_angle, value=25
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
        label_fichier = ctk.CTkLabel(tab_photo, text="Aucun fichier sélectionné")
        label_fichier.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")

        # Entrée de dcalage
        entry_decalage = ctk.CTkEntry(tab_photo, textvariable=var_decalage, width=40)
        entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        label_decalage = ctk.CTkLabel(tab_photo, text="Décalage [°]:")
        label_decalage.grid(row=0, column=2, padx=(10, 0), pady=5, sticky="w")


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
        
        self.label_fichier = ctk.CTkLabel(tab_color, text="Aucun fichier sélectionné")
        self.label_fichier.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        button_trace_colo = ctk.CTkButton(
            tab_color, text="Tracer le graphique", command=self.trace_colo
        )
        button_trace_colo.grid(row=1, column=2, padx=10, pady=5, sticky="e")


        # déclaration des key bindings
        self.bind("<Return>", self.input_handle)
        self.bind("<KP_Enter>", self.input_handle)



    def trace_photo(self):
        print("test trace photo")

    def trace_colo(self):
        print("test trace colo")

    def file(self):
        print("test file")


    def input_handle(self, event):
        current_tab = self.tabview.get()
        if current_tab == "Photométrie":
            self.trace_photo()
        elif current_tab == "Colorimétrie":
            self.trace_colo()


app = Application()
app.mainloop()
