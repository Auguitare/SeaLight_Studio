import zone as z


def trace_photometry(self):
    """Trace le graphique de photométrie"""
    self.ax_photo.clear()

    data = self.read_file()
    if data is None:
        return

    # Appliquer le décalage
    decalage = self.var_decalage.get()
    data["Angle °"] = data["Angle °"].apply(lambda x: x + decalage)

    # Tracer les limites
    secteur = self.var_secteur.get()
    angle = self.var_angle.get()
    range_val = int(self.var_range.get())

    self.trace_limit(secteur, range_val, angle)

    # Tracer les données
    self.ax_photo.plot(data["Angle °"], data["cd"], color="steelblue")

    # Afficher le graphique
    self.display_plot(self.photo_plot_frame, self.fig_photo, "photo")

def trace_limit(self, secteur, range_val, inclinaison):
    """Trace les zones limites"""
    if secteur == "Hune":
        z.hune(range_val, inclinaison)
    elif secteur == "Poupe":
        z.poupe(range_val, inclinaison)
    elif secteur == "Babord":
        z.babord(range_val, inclinaison)
    elif secteur == "Tribord":
        z.tribord(range_val, inclinaison)
    elif secteur == "Vide":
        z.only_value()

    # Tracer les zones
    for zone_num in [1, 2, 3]:
        zone = getattr(z, f"zone_limite_{zone_num}")
        self.ax_photo.plot(
            zone["x"], zone["y"], color="red", linestyle="--", alpha=0.5
        )
        self.ax_photo.fill(
            zone["x"],
            zone["y"],
            color="red",
            alpha=0.2,
            label=f"Zone limite {zone_num}",
        )

    self.ax_photo.set_title("Intensité lumineuse en fonction de l'angle")
    self.ax_photo.set_xlabel("Angle (°)")
    self.ax_photo.set_ylabel("Intensité lumineuse (cd)")
    self.ax_photo.minorticks_on()
    self.ax_photo.grid(which="major", alpha=0.7)
    self.ax_photo.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
