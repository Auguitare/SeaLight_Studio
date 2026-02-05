"""
Module de gestion de l'affichage photométrique.
Gère le traçage de l'intensité lumineuse en fonction de l'angle, l'application
de décalages angulaires et la visualisation des zones de conformité pour différents secteurs.
"""
import zone as z


def trace_graph(data, ax, decalage, previous_line):
    """
    Trace le graphique de l'intensité lumineuse en appliquant un décalage angulaire si necessaire.

    Args:
        data (pd.DataFrame): Données contenant les colonnes 'Angle °' et 'cd'.
        ax (matplotlib.axes.Axes): Axe matplotlib sur lequel tracer.
        decalage (tkinter.DoubleVar): Objet possédant une méthode get() pour obtenir le décalage.
    """
    if data is None:
        return

    if previous_line is not None:
        previous_line.remove()

    # Appliquer le décalage
    decalage = decalage.get()
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)

    # Tracer les données
    (line,) = ax.plot(data["Angle °"], data["cd"], color="steelblue")
    return line


def trace_limit(ax, secteur, range_val, inclinaison):
    """
    Trace les zones limites (zones interdites) sur le graphique de photométrie.

    Args:
        ax (matplotlib.axes.Axes): Axe matplotlib sur lequel tracer les limites.
        secteur (str): Nom du secteur ("Hune", "Poupe", "Babord", "Tribord", "Vide").
        range_val (float): Valeur de la portée.
        inclinaison (float): Valeur de l'inclinaison.
    """
    zone_interdite = {}
    if secteur == "Hune":
        zone_interdite = z.hune(range_val, inclinaison)
    elif secteur == "Poupe":
        zone_interdite = z.poupe(range_val, inclinaison)
    elif secteur == "Babord":
        zone_interdite = z.babord(range_val, inclinaison)
    elif secteur == "Tribord":
        zone_interdite = z.tribord(range_val, inclinaison)
    elif secteur == "Vide":
        zone_interdite = z.only_value()

    # Tracer les zones
    for zone_num in [1, 2, 3]:
        zone = zone_interdite[zone_num]
        ax.plot(zone["X"], zone["Y"], color="red", linestyle="--", alpha=0.5)
        ax.fill(
            zone["X"],
            zone["Y"],
            color="red",
            alpha=0.2,
        )

    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
