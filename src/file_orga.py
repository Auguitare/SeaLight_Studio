# -*- coding: utf-8 -*-
# Copyright (c) 2025 OrionOfCreation
# Licensed under the MIT License - see LICENSE file for details
"""
Module de gestion des fichiers
Gère l'import des fichiers et la la transmormation en donnée
"""

import sys
import os

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
    try:
        ligne_header = 0
        with open(fichier_selectionne, "r", encoding="utf-8") as f:
            for i, ligne in enumerate(f):
                if "Angle" in ligne:
                    ligne_header = i
                    break

        data_file = pd.read_csv(
            fichier_selectionne,
            sep=";",
            skiprows= ligne_header,
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
            f"Colonnes manquantes dans le fichier : {str(e).rsplit('[', maxsplit=1)[-1].strip(']')}"
        )
        return None


def resource_path(relative_path):
    """Obtenir le chemin absolu vers la ressource, fonctionne pour PyInstaller"""
    try:
        # PyInstaller crée un dossier temporaire et stocke le chemin dans _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
