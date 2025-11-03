import pandas
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

fenetre = ctk.CTk()


def read_file():
    lignes_a_sauter = set()
    with open("+25.txt", "r") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i))
                break

    data_file = pandas.read_csv("+25.txt", sep= ";", 
                skiprows = lambda x: x in lignes_a_sauter, skipfooter = 2,
                engine="python", usecols=["Angle °", "cd", "X", "Y", "Tension V", "Courant A", "temperature ambiante °C"])
    return data_file


def trace_graph():
    data = read_file()
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")

def data_update():
    data['Angle °'] = data['Angle °'].apply(lambda x: x-90)

    # Intégration dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=fenetre)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Barre d'outils
    toolbar = NavigationToolbar2Tk(canvas, fenetre)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)





def window():
    fenetre.title("graphe")
    #fenetre.geometry("300x150")

    bouton = ctk.CTkButton(fenetre, text="Tracer le graphique", command=trace_graph)
    bouton.pack(pady=20)

    fenetre.mainloop()

window()


def hune():
    zone_limite_1 = {-132.5:6.5, -132.5:118,-117.5:118,-117.5:6.5,-132.5:6.5}
    zone_limite_2 = {-112.5:0, -112.5:59, -107.5:59, -107.5:118, 107.5:118, 107.5:59, 112.5:59, 112.5:0, -112.5:0}
    zone_limite_3 = {132.5:118, 132.5:6.5, 117.5:6.5, 117.5:118, 132.5:118}

