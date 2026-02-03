def trace_graph(data, ax):
    if data is None:
        return

    ax.clear()
    
    # Tracer les données
    ax.plot(data["X"], data["Y"], color="steelblue")
    
    ax.set_title("Diagramme chromatique")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
