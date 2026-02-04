import zone as z

def trace_graph(data, ax, decalage):
    if data is None:
        return

    ax.clear()
    
    # Appliquer le décalage
    decalage = decalage.get()
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)

    # Tracer les données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    

def trace_limit(ax, secteur, range_val, inclinaison):
    """Trace les zones limites"""
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
        ax.plot(
            zone["X"], zone["Y"], color="red", linestyle="--", alpha=0.5
        )
        ax.fill(
            zone["X"],
            zone["Y"],
            color="red",
            alpha=0.2,
            label=f"Zone limite {zone_num}",
        )
    
    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité lumineuse (cd)")
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
