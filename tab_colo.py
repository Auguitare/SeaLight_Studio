def trace_graph(data, ax):
    if data is None:
        return

    ax.clear()
    
    # Tracer les données
    ax.scatter(data["X"], data["Y"], c='black', s=50, alpha=0.6)
    
    ax.set_title("Diagramme chromatique")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.minorticks_on()
    ax.grid(which="major", alpha=0.7)
    ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
