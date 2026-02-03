import pandas
import tkinter as tk
from tkinter import filedialog
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
        button_trace = ctk.CTkButton(
            tab_photo, text="Tracer le graphique", command=self.trace
        )
        button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")

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

        # déclaration des key bindings
        tab_photo.bind("<Return>", lambda event: button_trace.invoke())
        tab_photo.bind("<KP_Enter>", lambda event: button_trace.invoke())




        # ========== UI Colorimetrie ==========
        # Configuration de la grille
        tab_color.grid_rowconfigure(0, weight=0)
        tab_color.grid_rowconfigure(1, weight=0)
        tab_color.grid_rowconfigure(2, weight=1)
        tab_color.grid_columnconfigure(0, weight=1)
        tab_color.grid_columnconfigure(1, weight=1)
        tab_color.grid_columnconfigure(2, weight=1)






    def trace(self):
        print("test trace")

    def file(self):
        print("test file")


app = Application()
app.mainloop()
