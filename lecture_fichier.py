import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Strating page")
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)


        # add widgets to app
        self.button = ctk.CTkButton(self, command=self.button_click)
        self.button.grid(row=1, column=1, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        import photometry as p
        p.window()


app = App()
app.mainloop()