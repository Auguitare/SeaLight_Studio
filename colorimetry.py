def trace_colorimetry(self):
    """Trace le graphique de colorimétrie"""
    self.ax_color.clear()

    data = self.read_file()
    if data is None:
        return

    # Tracer les données
    self.ax_color.plot(
        data["X"], data["Y"], color="steelblue", marker="o", markersize=3
    )

    self.ax_color.set_title("Diagramme de chromaticité")
    self.ax_color.set_xlabel("Coordonnée X")
    self.ax_color.set_ylabel("Coordonnée Y")
    self.ax_color.minorticks_on()
    self.ax_color.grid(which="major", alpha=0.7)
    self.ax_color.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
    self.ax_color.set_xlim(0, 1)
    self.ax_color.set_ylim(0, 1)

    # Afficher le graphique
    self.display_plot(self.color_plot_frame, self.fig_color, "color")
