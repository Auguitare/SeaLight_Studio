import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")
        self.title("Starting Page")

        # Titre
        self.label_titre = ctk.CTkLabel(
            self, 
            text="Choisissez une option", 
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_titre.pack(pady=30)

        # Bouton pour ouvrir la fenêtre de photométrie
        self.button_photometry = ctk.CTkButton(
            self, 
            text="Photométrie", 
            command=self.ouvrir_photometry,
            width=200,
            height=40
        )
        self.button_photometry.pack(pady=20)

        # Bouton pour la deuxième fenêtre (colorimétrie)
        self.button_autre = ctk.CTkButton(
            self, 
            text="Colorimétrie", 
            command=self.ouvrir_autre,
            width=200,
            height=40
        )
        self.button_autre.pack(pady=20)

        # Bouton pour quitter
        self.button_quitter = ctk.CTkButton(
            self, 
            text="Quitter", 
            command=self.quit,
            width=200,
            height=40,
            fg_color="gray"
        )
        self.button_quitter.pack(pady=20)

    def ouvrir_photometry(self):
        """Ouvre la fenêtre de photométrie"""
        self.destroy()  # Cache la fenêtre principale
        import photometry as p
        p.window()

    def ouvrir_autre(self):
        """Ouvre la fenêtre de colorimétrie"""
        self.destroy()  # Cache la fenêtre principale
        import colorimetry as c
        c.window()

if __name__ == "__main__":
    app = App()
    app.mainloop()