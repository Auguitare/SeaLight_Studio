import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Page de choix")

        # Titre
        self.label_titre = ctk.CTkLabel(
            self, text="Choisissez une option", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_titre.pack(pady=30)

        # Bouton pour ouvrir la fenêtre de photométrie
        self.button_photometry = ctk.CTkButton(
            self,
            text="Photométrie",
            command=self.ouvrir_photometry,
            width=200,
            height=40,
        )
        self.button_photometry.pack(pady=20)

        # Bouton pour la deuxième fenêtre (à implémenter)
        self.button_autre = ctk.CTkButton(
            self,
            text="Autre fonctionnalité",
            command=self.ouvrir_autre,
            width=200,
            height=40,
        )
        self.button_autre.pack(pady=20)

        # Bouton pour quitter
        self.button_quitter = ctk.CTkButton(
            self,
            text="Quitter",
            command=self.quit,
            width=200,
            height=40,
            fg_color="gray",
        )
        self.button_quitter.pack(pady=20)

    def ouvrir_photometry(self):
        """Ouvre la fenêtre de photométrie"""
        self.withdraw()  # Cache la fenêtre principale
        import photometry as p

        p.window()
        self.deiconify()  # Réaffiche la fenêtre principale après fermeture

    def ouvrir_autre(self):
        """Ouvre une autre fenêtre (à implémenter)"""
        self.withdraw()  # Cache la fenêtre principale

        # Création d'une fenêtre temporaire comme exemple
        autre_fenetre = ctk.CTkToplevel(self)
        autre_fenetre.title("Autre fonctionnalité")
        autre_fenetre.geometry("400x300")

        label = ctk.CTkLabel(
            autre_fenetre,
            text="Cette fenêtre sera implémentée plus tard",
            font=ctk.CTkFont(size=16),
        )
        label.pack(pady=50)

        button_retour = ctk.CTkButton(
            autre_fenetre,
            text="Retour",
            command=lambda: self.fermer_autre(autre_fenetre),
        )
        button_retour.pack(pady=20)

        # Empêche la fermeture sans passer par le bouton
        autre_fenetre.protocol(
            "WM_DELETE_WINDOW", lambda: self.fermer_autre(autre_fenetre)
        )

    def fermer_autre(self, fenetre):
        """Ferme la fenêtre secondaire et réaffiche le menu"""
        fenetre.destroy()
        self.deiconify()


if __name__ == "__main__":
    app = App()
    app.mainloop()
