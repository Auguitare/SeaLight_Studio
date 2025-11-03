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

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)


def hune_0():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-132.5, -132.5, -117.5, -117.5, -132.5],
        "y": [6.5, 118, 118, 6.5, 6.5],
    }

    zone_limite_2 = {
        "x": [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5],
        "y": [0, 59, 59, 118, 118, 59, 59, 0, 0],
    }

    zone_limite_3 = {
        "x": [132.5, 132.5, 117.5, 117.5, 132.5],
        "y": [118, 6.5, 6.5, 118, 118],
    }
    trace_limit()


def poupe_0():
    global zone_limite_1, zone_limite_2, zone_limite_3

    # Secteur interdit 1
    zone_limite_1 = {"x": [85, 85, 107.5, 107.5, 85], "y": [1.5, 15, 15, 1.5, 1.5]}

    # Secteur interdit 2
    zone_limite_2 = {
        "x": [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5],
        "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    }

    # Secteur interdit 3
    zone_limite_3 = {
        "x": [267.5, 267.5, 252.5, 252.5, 267.5],
        "y": [15, 1.5, 1.5, 15, 15],
    }
    trace_limit()


def read_file():
    lignes_a_sauter = set()
    with open("0.txt", "r") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i))
                break

    data_file = pandas.read_csv(
        "0.txt",
        sep=";",
        skiprows=lambda x: x in lignes_a_sauter,
        skipfooter=2,
        engine="python",
        usecols=[
            "Angle °",
            "cd",
            "X",
            "Y",
            "Tension V",
            "Courant A",
            "temperature ambiante °C",
        ],
    )
    return data_file


def trace_limit():
    # plot des limite remplie (pour plus de classe)
    ax.plot(
        zone_limite_1["x"], zone_limite_1["y"], color="red", linestyle="--", alpha=0.5
    )
    ax.fill(
        zone_limite_1["x"],
        zone_limite_1["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 1",
    )
    ax.plot(
        zone_limite_2["x"], zone_limite_2["y"], color="red", linestyle="--", alpha=0.5
    )
    ax.fill(
        zone_limite_2["x"],
        zone_limite_2["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 2",
    )
    ax.plot(
        zone_limite_3["x"], zone_limite_3["y"], color="red", linestyle="--", alpha=0.5
    )
    ax.fill(
        zone_limite_3["x"],
        zone_limite_3["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 3",
    )

    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")
    ax.grid()


def trace_graph():
    global ax

    # Clear l'axe avant de tracer (important si tu traces plusieurs fois)
    ax.clear()

    data = read_file()
    data["Angle °"] = data["Angle °"].apply(lambda x: x - 90)

    secteur_value = secteur.get()  # récupérer la valeur du Radiobutton
    if secteur_value == 1:
        hune_0()
    elif secteur_value == 2:
        poupe_0()

    # plot des données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    trace_limit()

    # Créer un frame conteneur pour canvas + toolbar
    if hasattr(fenetre, "plot_frame"):
        fenetre.plot_frame.destroy()  # détruire l'ancien s'il existe

    fenetre.plot_frame = ctk.CTkFrame(fenetre)
    fenetre.plot_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

    # Canvas matplotlib dans le frame
    canvas = FigureCanvasTkAgg(fig, master=fenetre.plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Toolbar dans le frame
    toolbar = NavigationToolbar2Tk(canvas, fenetre.plot_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)


def window():
    global secteur  # pour qu'il soit accessible dans trace_graph
    fenetre.title("graphe")
    fenetre.grid_rowconfigure(2, weight=1)
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)

    secteur = ctk.IntVar(value=1)  # valeur par défaut

    rb1 = ctk.CTkRadioButton(fenetre, text="hune", variable=secteur, value=1)
    rb1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    rb2 = ctk.CTkRadioButton(fenetre, text="poupe", variable=secteur, value=2)
    rb2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    bouton3 = ctk.CTkButton(fenetre, text="Tracer le graphique", command=trace_graph)
    bouton3.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    fenetre.mainloop()


window()
