import zone as z
import pandas
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

fichier_selectionne = None  # pour stocker le chemin du fichier choisi
dernier_dossier = "."

fig = None
ax = None
fenetre = None


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
                lignes_a_sauter.update(range(0, i), range(i + 1, i + 3))
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
            "lux",
        ],
    )
    return data_file


def trace_limit(secteur, range, inclinaison):
    if secteur == "Hune":
        z.hune(range, inclinaison)
    elif secteur == "Poupe":
        z.poupe(range, inclinaison)
    elif secteur == "Babord":
        z.babord(range, inclinaison)
    elif secteur == "Tribord":
        z.tribord(range, inclinaison)
    elif secteur == "Vide":
        z.only_value()

    # trace zone interdite 1
    ax.plot(
        z.zone_limite_1["x"],
        z.zone_limite_1["y"],
        color="red",
        linestyle="--",
        alpha=0.5,
    )
    ax.fill(
        z.zone_limite_1["x"],
        z.zone_limite_1["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 1",
    )
    # trace zone interdite 2
    ax.plot(
        z.zone_limite_2["x"],
        z.zone_limite_2["y"],
        color="red",
        linestyle="--",
        alpha=0.5,
    )
    ax.fill(
        z.zone_limite_2["x"],
        z.zone_limite_2["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 2",
    )
    # trace zone interdite 3
    ax.plot(
        z.zone_limite_3["x"],
        z.zone_limite_3["y"],
        color="red",
        linestyle="--",
        alpha=0.5,
    )
    ax.fill(
        z.zone_limite_3["x"],
        z.zone_limite_3["y"],
        color="red",
        alpha=0.2,
        label="Zone limite 3",
    )

    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
    # ax.grid()


def modifier_angles(data, decalage=0):
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)
    return data


def trace_graph():
    global ax

    # Clear l'axe avant de tracer
    ax.clear()

    data = read_file()
    decalage = var_decalage.get()
    data = modifier_angles(data, decalage=decalage)

    # Choix du secteur et de l'angle des limites
    var_secteur_value = var_secteur.get()
    angle_value = var_angle.get()
    range_value = int(var_range.get())
    trace_limit(var_secteur_value, range_value, angle_value)

    # plot des données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")

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
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    # # ajout de label relativ au graphe
    # label_test1 = ctk.CTkLabel(fenetre, text="test 1")
    # label_test2 = ctk.CTkLabel(fenetre, text="test 2")
    # label_test3 = ctk.CTkLabel(fenetre, text="test 3")
    # label_test4 = ctk.CTkLabel(fenetre, text="test 4")
    # label_test5 = ctk.CTkLabel(fenetre, text="test 5")
    # label_test6 = ctk.CTkLabel(fenetre, text="test 6")
    # label_test7 = ctk.CTkLabel(fenetre, text="test 7")
    # fenetre.grid_columnconfigure(3, weight=1)
    # label_test1.grid(row=0, column=3, padx=10, pady=5, sticky="w")
    # label_test2.grid(row=1, column=3, padx=10, pady=5, sticky="w")
    # label_test3.grid(row=2, column=3, padx=10, pady=5, sticky="w")
    # label_test4.grid(row=3, column=3, padx=10, pady=5, sticky="nw")
    # label_test5.grid(row=4, column=3, padx=10, pady=5, sticky="nw")
    # label_test6.grid(row=5, column=3, padx=10, pady=5, sticky="nw")
    # label_test7.grid(row=6, column=3, padx=10, pady=5, sticky="nw")


def fermer_autre(self, fenetre):
    """Ferme la fenêtre secondaire et réaffiche le menu"""
    fenetre.destroy()
    self.deiconify()


def window():
    global \
        var_secteur, \
        var_range, \
        var_angle, \
        var_decalage, \
        label_fichier, \
        fenetre, \
        fig, \
        ax

    # Créer une nouvelle fenêtre
    fenetre = ctk.CTk()

    # Initialiser la figure matplotlib
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    # mise en forme de la fenetre
    fenetre.title("graphe")
    fenetre.grid_rowconfigure(6, weight=1)
    fenetre.grid_columnconfigure(0, weight=2)
    fenetre.grid_columnconfigure(1, weight=2)
    fenetre.grid_columnconfigure(2, weight=2)

    # déclaration des valiables des boutons
    var_secteur = ctk.StringVar(value="Vide")
    var_range = ctk.StringVar(value="2")
    var_angle = ctk.IntVar(value=0)
    var_decalage = tk.DoubleVar(value=0)
    print(var_decalage.get())

    # déclaration des input
    secteur_menu = ctk.CTkOptionMenu(
        fenetre,
        values=["Vide", "Hune", "Poupe", "Babord", "Tribord"],
        variable=var_secteur,
    )

    range_menu = ctk.CTkOptionMenu(
        fenetre,
        values=["1", "2", "3", "4", "5", "6"],
        variable=var_range,
    )

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
    range_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    button_fichier.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    rb_0.grid(row=0, column=1, padx=10, pady=5, sticky="w")
    rb_25.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    label_fichier.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")
    entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")
    button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")

    # affichage de la fenetre
    fenetre.mainloop()
