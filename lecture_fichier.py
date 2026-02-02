import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Strating page")

        # add widgets to app
        self.button = ctk.CTkButton(self, text="Tracer le graphique", command=self.button_click)
        self.button.place(relx=0.5, rely=0.5, anchor="center")

    def button_click(self):
        import photometry as p
        p.window()


app = App()
app.mainloop()