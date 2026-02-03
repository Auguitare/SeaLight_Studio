def trace_graph(data, ax, decalage):
    if data is None:
        return

    ax.clear()
    
    # Appliquer le décalage
    decalage = decalage.get()
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)
    
    # Tracer les données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    
    ax.set_title("Intensité lumineuse en fonction de l'angle")
    ax.set_xlabel("Angle (°)")
    ax.set_ylabel("Intensité (cd)")
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
    