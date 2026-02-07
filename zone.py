# -*- coding: utf-8 -*-
"""
Module de calcul des zones d'intensité et des coordonnées géométriques.
Définit les limites d'intensité lumineuse et les secteurs angulaires pour les différents
types de feux de navigation (Hune, Poupe, Babord, Tribord) selon les normes.
"""
import tkinter as tk


def intensity_calc(light_range, inclinaison):
    """
    Calcule la puissance maximale basée sur la portée de la lumière et l'inclinaison,
    et retourne un dictionnaire de valeurs d'intensité pour trois zones.

    Args:
        light_range (int): La portée de la lumière (1-6).
        inclinaison (float/int): L'angle d'inclinaison. Si non nul, puissance est divisée par deux.

    Returns:
        dict: Un dictionnaire contenant les données
        d'intensité (valeurs Y) pour les zones 1, 2 et 3.
    """
    max_power = 0
    match light_range:
        case 1:
            max_power = 1.1
        case 2:
            max_power = 5.4
        case 3:
            max_power = 15
        case 4:
            max_power = 33
        case 5:
            max_power = 65
        case 6:
            max_power = 118
        case _:
            tk.messagebox.showwarning("Avertissement", "choisir une portée.")
            return

    if inclinaison != 0:
        max_power *= 0.5

    return {
        1: {
            "Y": [
                0.1 * max_power,
                max_power,
                max_power,
                0.1 * max_power,
                0.1 * max_power,
            ]
        },
        2: {
            "Y": [
                0,
                0.5 * max_power,
                0.5 * max_power,
                max_power,
                max_power,
                0.5 * max_power,
                0.5 * max_power,
                0,
                0,
            ]
        },
        3: {"Y": [max_power, 0.1 * max_power, 0.1 * max_power, max_power, max_power]},
    }


def hune(light_range = 1, inclinaison = 0):
    """
    Définit les coordonnées pour les zones de feu de hune.

    Args:
        light_range (int): La portée de la lumière.
        inclinaison (float/int): L'angle d'inclinaison.

    Returns:
        dict: Le dictionnaire d'intensité avec les coordonnées X ajoutées pour chaque zone.
    """
    zone = intensity_calc(light_range, inclinaison)

    zone[1]["X"] = [-132.5, -132.5, -117.5, -117.5, -132.5]
    zone[2]["X"] = [-112.5, -112.5, -107.5, -107.5, 107.5, 107.5, 112.5, 112.5, -112.5]
    zone[3]["X"] = [132.5, 132.5, 117.5, 117.5, 132.5]

    return zone


def poupe(light_range = 1, inclinaison = 0):
    """
    Définit les coordonnées pour les zones de feu de poupe.

    Args:
        light_range (int): La portée de la lumière.
        inclinaison (float/int): L'angle d'inclinaison.

    Returns:
        dict: Le dictionnaire d'intensité avec les coordonnées X ajoutées pour chaque zone.
    """
    zone = intensity_calc(light_range, inclinaison)

    zone[1]["X"] = [85, 85, 107.5, 107.5, 85]
    zone[2]["X"] = [112.5, 112.5, 117.5, 117.5, 242.5, 242.5, 247.5, 247.5, 112.5]
    zone[3]["X"] = [267.5, 267.5, 252.5, 252.5, 267.5]

    return zone


def babord(light_range = 1, inclinaison = 0):
    """
    Définit les coordonnées pour les zones de feu de bâbord.

    Args:
        light_range (int): La portée de la lumière.
        inclinaison (float/int): L'angle d'inclinaison.

    Returns:
        dict: Le dictionnaire d'intensité avec les coordonnées X ajoutées pour chaque zone.
    """
    zone = intensity_calc(light_range, inclinaison)

    zone[1]["X"] = [-30, -30, -3, -3, -30]
    zone[2]["X"] = [0, 0, 0, 0, 107.5, 107.5, 112.5, 112.5, 0]
    zone[3]["X"] = [142.5, 142.5, 117.5, 117.5, 142.5]

    return zone


def tribord(light_range = 1, inclinaison = 0):
    """
    Définit les coordonnées pour les zones de feu de tribord.

    Args:
        light_range (int): La portée de la lumière.
        inclinaison (float/int): L'angle d'inclinaison.

    Returns:
        dict: Le dictionnaire d'intensité avec les coordonnées X ajoutées pour chaque zone.
    """
    zone = intensity_calc(light_range, inclinaison)

    zone[1]["X"] = [-142.5, -142.5, -117.5, -117.5, -142.5]
    zone[2]["X"] = [-112.5, -112.5, -107.5, -107.5, 0, 0, 0, 0, -112.5]
    zone[3]["X"] = [30, 30, 3, 3, 30]

    return zone


def only_value():
    """
    Retourne un dictionnaire de zone avec des coordonnées initialisées à zéro.

    Returns:
        dict: Une structure de dictionnaire pour trois zones avec des valeurs X et Y vides ou nulles
    """
    zone = {}
    zone[1] = {"X": [], "Y": []}
    zone[2] = {"X": [], "Y": []}
    zone[3] = {"X": [], "Y": []}

    zone[1]["X"] = [0]
    zone[1]["Y"] = [0]
    zone[2]["X"] = [0]
    zone[2]["Y"] = [0]
    zone[3]["X"] = [0]
    zone[3]["Y"] = [0]

    return zone
