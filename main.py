import pandas
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Analyse des données photométrique feux de navigation")

        # onglets
        self.tabview = ctk.CTkTabview(self, width=1050, height=750)
        self.tabview.pack(padx=20, pady=20, fill="both", expand=True)
        self.tabview.add("Photométrie")
        self.tabview.add("Colorimétrie")




def main():
    app = Application()
    app.mainloop()


main()