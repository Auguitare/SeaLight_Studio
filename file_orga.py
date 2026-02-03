import tkinter as tk
import pandas as pd



def choisir_fichier():
    fichier_selectionne = tk.filedialog.askopenfilename(
        title="Choisir un fichier de données",
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Fichiers de calcul", "*.csv"),
            ("Tous les fichiers", "*.*"),
        ],
    )

    return fichier_selectionne


def read_file(fichier_selectionne):
    lignes_a_sauter = set()
    with open(fichier_selectionne, "r") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i), range(i + 1, i + 3))
                break

    data_file = pd.read_csv(
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
