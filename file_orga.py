# -*- coding: utf-8 -*-
"""
Module de gestion des fichiers
Gère l'import des fichiers et la la transmormation en donnée
"""
import tkinter as tk
import pandas as pd


def choisir_fichier():
    """
    Ouvre une boîte de dialogue pour sélectionner un fichier de données.

    Returns:
        str: Le chemin du fichier sélectionné ou une chaîne vide si annulé.
    """

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
    """
    Lit un fichier CSV/texte et retourne un DataFrame pandas contenant les colonnes utiles.

    Saute les lignes d'en-tête jusqu'à trouver "Angle" et ignore les deux dernières lignes.

    Args:
        fichier_selectionne (str): Chemin du fichier à lire.

    Returns:
        pd.DataFrame: DataFrame contenant les données, ou None en cas d'erreur.
    """
    lignes_a_sauter = set()
    with open(fichier_selectionne, "r", encoding="utf-8") as f:
        lignes = f.readlines()
        for i, ligne in enumerate(lignes):
            if "Angle" in ligne:
                lignes_a_sauter.update(range(0, i))
                break

    try:
        data_file = pd.read_csv(
            fichier_selectionne,
            sep=";",
            skiprows=lambda x: x in lignes_a_sauter,
            skipfooter=2,
            engine="python",
            usecols=[
                "Angle °",
                "cd",
                "lux",
                "X",
                "Y",
            ],
        )
        return data_file
    except FileNotFoundError:
        tk.messagebox.showerror("Erreur", "Fichier introuvable")
        return None
    except pd.errors.ParserError:
        tk.messagebox.showerror("Erreur", "Format de fichier invalide")
        return None
    except ValueError as e:
        tk.messagebox.showerror(
            "Colone manquante",
            f"Colonnes manquantes dans le fichier : {str(e).rsplit('[', maxsplit=1)[-1].strip(']')}",
        )
        return None
