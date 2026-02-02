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


def trace_graph():
    global ax

    # Clear l'axe avant de tracer
    ax.clear()

    data = read_file()
    
    if data is None:
        return

    # Plot des données en coordonnées X, Y (colorimétrie)
    ax.plot(data["X"], data["Y"], color="steelblue", marker='o', markersize=3)

    ax.set_title("Diagramme de chromaticité")
    ax.set_xlabel("Coordonnée X")
    ax.set_ylabel("Coordonnée Y")
    ax.minorticks_on()
    ax.grid(which='major', alpha=0.7)
    ax.grid(which='minor', linestyle='--', linewidth=0.5, alpha=0.4)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Créer une frame conteneur pour canvas + toolbar
    if hasattr(fenetre, "plot_frame"):
        fenetre.plot_frame.destroy()  # détruire l'ancien s'il existe

    fenetre.plot_frame = ctk.CTkFrame(fenetre)
    fenetre.plot_frame.grid(row=2, column=0, columnspan=3, rowspan=4, sticky="nsew")

    # Canvas matplotlib dans la frame
    canvas = FigureCanvasTkAgg(fig, master=fenetre.plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Toolbar (important pour zoom et save) dans la frame
    toolbar = NavigationToolbar2Tk(canvas, fenetre.plot_frame)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.X)


def window():
    global label_fichier, fenetre, fig, ax

    # Créer une nouvelle fenêtre
    fenetre = ctk.CTk()
    
    # Initialiser la figure matplotlib
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    # mise en forme de la fenetre
    fenetre.title("Colorimétrie")
    fenetre.grid_rowconfigure(5, weight=1)
    fenetre.grid_columnconfigure(0, weight=2)
    fenetre.grid_columnconfigure(1, weight=2)
    fenetre.grid_columnconfigure(2, weight=2)

    # déclaration des boutons
    button_trace = ctk.CTkButton(
        fenetre, text="Tracer le graphique", command=trace_graph
    )

    button_fichier = ctk.CTkButton(
        fenetre, text="Choisir un fichier", command=choisir_fichier
    )

    # déclaration des labels d'information
    label_fichier = ctk.CTkLabel(fenetre, text="Aucun fichier sélectionné")
    label_info = ctk.CTkLabel(
        fenetre, 
        text="Colorimétrie - Diagramme de chromaticité (X, Y)",
        font=ctk.CTkFont(size=14, weight="bold")
    )

    # déclaration des key bindings
    fenetre.bind("<Return>", lambda event: button_trace.invoke())
    fenetre.bind("<KP_Enter>", lambda event: button_trace.invoke())

    # mise en positions des input et label
    label_info.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")
    button_fichier.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    label_fichier.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")
    button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")

    # affichage de la fenetre
    fenetre.mainloop()