import pandas
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

fenetre = ctk.CTk()
zone_limite_1 = dict()
zone_limite_2 = dict()
zone_limite_3 = dict()

def hune():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-132.5, -132.5, -117.5, -117.5, -132.5],
        "y": [6.5, 118, 118, 6.5, 6.5]
    }

    zone_limite_2 = {
        "x": [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5],
        "y": [0, 59, 59, 118, 118, 59, 59, 0, 0]
    }

    zone_limite_3 = {
        "x": [132.5, 132.5, 117.5, 117.5, 132.5],
        "y": [118, 6.5, 6.5, 118, 118]
    }


def read_file():
    lignes_a_sauter = set()
    with open("0.txt", "r") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i))
                break

    data_file = pandas.read_csv("0.txt", sep= ";", 
                skiprows = lambda x: x in lignes_a_sauter, skipfooter = 2,
                engine="python", usecols=["Angle °", "cd", "X", "Y", "Tension V", "Courant A", "temperature ambiante °C"])
    return data_file


def trace_graph():
    data = read_file()
    data['Angle °'] = data['Angle °'].apply(lambda x: x-90)
    hune()
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    # plot des données 
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    #plot des limite remplie (pour plus de classe)
    ax.plot(zone_limite_1["x"], zone_limite_1["y"], color="red", linestyle="--", alpha = 0.5)
    ax.fill(zone_limite_1["x"], zone_limite_1["y"], color="red", alpha=0.2, label="Zone limite 1")
    ax.plot(zone_limite_2["x"], zone_limite_2["y"], color="red", linestyle="--", alpha = 0.5)
    ax.fill(zone_limite_2["x"], zone_limite_2["y"], color="red", alpha=0.2, label="Zone limite 2")
    ax.plot(zone_limite_3["x"], zone_limite_3["y"], color="red", linestyle="--", alpha = 0.5)
    ax.fill(zone_limite_3["x"], zone_limite_3["y"], color="red", alpha=0.2, label="Zone limite 3")

    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")
    ax.grid()
    


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


