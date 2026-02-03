from matplotlib.figure import Figure



def trace_graph(data, ax, decalage):
    if data is None:
        return

    ax.clear()
    
    # Appliquer le décalage
    decalage = decalage.get()
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)
    
    # Tracer les données
    ax.plot(data["Angle °"], data["cd"], color="steelblue")
    
    # Afficher le graphiqu