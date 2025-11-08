import pandas
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

fenetre = ctk.CTk()
# test git


zone_limite_1 = dict()
zone_limite_2 = dict()
zone_limite_3 = dict()
fichier_selectionne = None  # pour stocker le chemin du fichier choisi
dernier_dossier = "."

fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)


def choisir_fichier():
    global fichier_selectionne, dernier_dossier
    fichier_selectionne = filedialog.askopenfilename(
        title="Choisir un fichier de données",
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Fichiers de calcul", "*.csv"),
            ("Tous les fichiers", "*.*"),
        ],
    )

    if fichier_selectionne:
        dernier_dossier = "/".join(fichier_selectionne.split("/")[:-1])
        label_fichier.configure(
            text=f"Fichier sélectionné : {fichier_selectionne.split('/')[-1]}"
        )
    else:
        label_fichier.configure(text="Aucun fichier sélectionné")


def read_file():
    global fichier_selectionne
    if not fichier_selectionne:
        tk.messagebox.showwarning(
            "Avertissement", "Veuillez d'abord choisir un fichier à ouvrir."
        )
        return None

    lignes_a_sauter = set()
    with open(fichier_selectionne, "r") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i))
                break

    data_file = pandas.read_csv(
        fichier_selectionne,
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


def hune_25():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-132.5, -132.5, -117.5, -117.5, -132.5],
        "y": [6.5, 59, 59, 6.5, 6.5],
    }

    zone_limite_2 = {
        "x": [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5],
        "y": [0, 29.5, 29.5, 59, 59, 29.5, 29.5, 0, 0],
    }

    zone_limite_3 = {
        "x": [132.5, 132.5, 117.5, 112.5, 132.5],
        "y": [59, 6.5, 6.5, 59, 59],
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


def poupe_25():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [92.5, 92.5, 107.5, 107.5, 92.5],
        "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    }

    zone_limite_2 = {
        "x": [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5],
        "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    }

    zone_limite_3 = {
        "x": [267.5, 267.5, 252.5, 252.5, 267.5],
        "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    }

    trace_limit()


def babord_0():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-30, -30, -3, -3, -30],
        "y": [1.5, 15, 15, 1.5, 1.5],
    }

    zone_limite_2 = {
        "x": [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0],
        "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    }

    zone_limite_3 = {
        "x": [142.5, 142.5, 117.5, 117.5, 142.5],
        "y": [15, 1.5, 1.5, 15, 15],
    }

    trace_limit()


def babord_25():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-30, -30, -3, -3, -30],
        "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    }

    zone_limite_2 = {
        "x": [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0],
        "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    }

    zone_limite_3 = {
        "x": [142.5, 142.5, 117.5, 117.5, 142.5],
        "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    }

    trace_limit()


def tribord_0():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-142.5, -142.5, -117.5, -117.5, -142.5],
        "y": [1.5, 15, 15, 1.5, 1.5],
    }

    zone_limite_2 = {
        "x": [-112.5, -112.5, -107.5, -107.5, -5, -5, 0, 0, -112.5],
        "y": [0, 7.5, 7.5, 15, 15, 7.5, 7.5, 0, 0],
    }

    zone_limite_3 = {
        "x": [30, 30, 5, 5, 30],
        "y": [15, 1.5, 1.5, 15, 15],
    }

    trace_limit()


def tribord_25():
    global zone_limite_1, zone_limite_2, zone_limite_3

    zone_limite_1 = {
        "x": [-142.5, -142.5, -117.5, -117.5, -142.5],
        "y": [1.5, 7.5, 7.5, 1.5, 1.5],
    }

    zone_limite_2 = {
        "x": [-112.5, -112.5, -107.5, -107.5, -5, -5, 0, 0, -112.5],
        "y": [0, 3.75, 3.75, 7.5, 7.5, 3.75, 3.75, 0, 0],
    }

    zone_limite_3 = {
        "x": [30, 30, 5, 5, 30],
        "y": [7.5, 1.5, 1.5, 7.5, 7.5],
    }

    trace_limit()


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


def modifier_angles(data, decalage=0):
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)
    return data


def trace_graph():
    global ax

    # Clear l'axe avant de tracer (important si tu traces plusieurs fois)
    ax.clear()

    data = read_file()
    decalage = var_decalage.get()
    data = modifier_angles(data, decalage=decalage)

    # Choix du var_secteur et de l'angle
    var_secteur_value = var_secteur.get()
    angle_value = var_angle.get()
    if var_secteur_value == "Hune" and angle_value == 0:
        hune_0()
    elif var_secteur_value == "Hune" and angle_value == 25:
        hune_25()
    elif var_secteur_value == "Poupe" and angle_value == 0:
        poupe_0()
    elif var_secteur_value == "Poupe" and angle_value == 25:
        poupe_25()

    # plot des données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    trace_limit()

    # Créer une frame conteneur pour canvas + toolbar
    if hasattr(fenetre, "plot_frame"):
        fenetre.plot_frame.destroy()  # détruire l'ancien s'il existe

    fenetre.plot_frame = ctk.CTkFrame(fenetre)
    fenetre.plot_frame.grid(row=3, column=0, columnspan=3, rowspan=4, sticky="nsew")

    # Canvas matplotlib dans la frame
    canvas = FigureCanvasTkAgg(fig, master=fenetre.plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Toolbar(important pour zoom et save) dans la frame
    toolbar = NavigationToolbar2Tk(canvas, fenetre.plot_frame)
    toolbar.update()
    toolbar.pack(side=tk.TOP, fill=tk.X)

    # ajout de label relativ au graphe
    label_test1 = ctk.CTkLabel(fenetre, text="test 1")
    label_test2 = ctk.CTkLabel(fenetre, text="test 2")
    label_test3 = ctk.CTkLabel(fenetre, text="test 3")
    label_test4 = ctk.CTkLabel(fenetre, text="test 4")
    label_test5 = ctk.CTkLabel(fenetre, text="test 5")
    label_test6 = ctk.CTkLabel(fenetre, text="test 6")
    label_test7 = ctk.CTkLabel(fenetre, text="test 7")
    fenetre.grid_columnconfigure(3, weight=1)
    label_test1.grid(row=0, column=3, padx=10, pady=5, sticky="w")
    label_test2.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    label_test3.grid(row=2, column=3, padx=10, pady=5, sticky="w")
    label_test4.grid(row=3, column=3, padx=10, pady=5, sticky="nw")
    label_test5.grid(row=4, column=3, padx=10, pady=5, sticky="nw")
    label_test6.grid(row=5, column=3, padx=10, pady=5, sticky="nw")
    label_test7.grid(row=6, column=3, padx=10, pady=5, sticky="nw")


def window():
    global var_secteur, var_angle, var_decalage, label_fichier  # pour qu'il soit accessible dans trace_graph

    # mise en forme de la fenètre
    fenetre.title("graphe")
    fenetre.grid_rowconfigure(6, weight=1)
    fenetre.grid_columnconfigure(0, weight=2)
    fenetre.grid_columnconfigure(1, weight=2)
    fenetre.grid_columnconfigure(2, weight=2)

    # déclaration des valiables des boutons
    var_secteur = ctk.StringVar(value="Hune")
    var_angle = ctk.IntVar(value=0)
    var_decalage = tk.DoubleVar(value=0)

    # déclaration des input
    secteur_menu = ctk.CTkOptionMenu(
        fenetre,
        values=["Hune", "Poupe"],
        variable=var_secteur,
    )

    # rb_hune = ctk.CTkRadioButton(fenetre, text="hune", variable=var_secteur, value=1)
    # rb_poupe = ctk.CTkRadioButton(fenetre, text="poupe", variable=var_secteur, value=2)
    rb_0 = ctk.CTkRadioButton(fenetre, text="0°", variable=var_angle, value=0)
    rb_25 = ctk.CTkRadioButton(fenetre, text="+/-25°", variable=var_angle, value=25)
    button_trace = ctk.CTkButton(
        fenetre, text="Tracer le graphique", command=trace_graph
    )
    button_fichier = ctk.CTkButton(
        fenetre, text="Choisir un fichier", command=choisir_fichier
    )
    entry_decalage = ctk.CTkEntry(fenetre, textvariable=var_decalage)

    # déclaration des labels d'information
    label_fichier = ctk.CTkLabel(fenetre, text="Aucun fichier sélectionné")

    # déclaration des key bindings
    fenetre.bind("<Return>", lambda event: button_trace.invoke())
    fenetre.bind("<KP_Enter>", lambda event: button_trace.invoke())

    # mise en positions des input et label
    secteur_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    # rb_hune.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    # rb_poupe.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    rb_0.grid(row=0, column=1, padx=10, pady=5)
    rb_25.grid(row=1, column=1, padx=10, pady=5)
    entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")
    button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")
    button_fichier.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    label_fichier.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")

    # affichage de la fenetre
    fenetre.mainloop()


window()
