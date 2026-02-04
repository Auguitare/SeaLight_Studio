"""
Archive : Ancienne implémentation de l'onglet de photométrie.
Ce module contient une version de classe pour gérer l'interface, les paramètres
de secteur et le traçage de l'intensité lumineuse.
"""
import zone as z
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class PhotometryTab:
    """Gère l'onglet de photométrie"""
    
    def __init__(self, parent_tab, app):
        self.tab = parent_tab
        self.app = app  # Référence à l'application principale
        
        # Variables spécifiques à la photométrie
        self.var_secteur = ctk.StringVar(value="Vide")
        self.var_range = ctk.StringVar(value="2")
        self.var_angle = ctk.IntVar(value=0)
        self.var_decalage = ctk.DoubleVar(value=0.0)
        
        # Figure matplotlib
        self.fig = Figure(figsize=(8, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        # Construire l'interface
        self.setup_ui()
    
    def setup_ui(self):
        """Construit l'interface de l'onglet photométrie"""
        # Configuration de la grille
        self.tab.grid_rowconfigure(0, weight=0)
        self.tab.grid_rowconfigure(1, weight=0)
        self.tab.grid_rowconfigure(2, weight=0)
        self.tab.grid_rowconfigure(3, weight=1)
        self.tab.grid_columnconfigure(0, weight=1)
        self.tab.grid_columnconfigure(1, weight=1)
        self.tab.grid_columnconfigure(2, weight=1)
        
        # === Ligne 0 ===
        secteur_menu = ctk.CTkOptionMenu(
            self.tab,
            values=["Vide", "Hune", "Poupe", "Babord", "Tribord"],
            variable=self.var_secteur,
        )
        secteur_menu.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        rb_0 = ctk.CTkRadioButton(
            self.tab, text="0°", variable=self.var_angle, value=0
        )
        rb_0.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        label_decalage = ctk.CTkLabel(self.tab, text="Décalage d'angle:")
        label_decalage.grid(row=0, column=2, padx=(10, 0), pady=5, sticky="w")
        
        entry_decalage = ctk.CTkEntry(
            self.tab,
            textvariable=self.var_decalage,
            width=100,
            placeholder_text="Décalage (°)",
        )
        entry_decalage.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        
        # === Ligne 1 ===
        range_menu = ctk.CTkOptionMenu(
            self.tab, values=["1", "2", "3", "4", "5", "6"], variable=self.var_range
        )
        range_menu.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        rb_25 = ctk.CTkRadioButton(
            self.tab, text="+/-25°", variable=self.var_angle, value=25
        )
        rb_25.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        button_trace = ctk.CTkButton(
            self.tab, text="Tracer le graphique", command=self.trace_graph
        )
        button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")
        
        # === Ligne 2 ===
        button_fichier = ctk.CTkButton(
            self.tab, text="Choisir un fichier", command=self.choisir_fichier
        )
        button_fichier.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        
        self.label_fichier = ctk.CTkLabel(self.tab, text="Aucun fichier sélectionné")
        self.label_fichier.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="w")
        
        # === Ligne 3 : Zone du graphe ===
        self.plot_frame = ctk.CTkFrame(self.tab)
        self.plot_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    def choisir_fichier(self):
        """Utilise la fonction de l'application principale pour choisir un fichier"""
        self.app.choisir_fichier(self)
    
    def trace_graph(self):
        """Trace le graphique de photométrie"""
        self.ax.clear()
        
        data = self.app.read_file()
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
        self.ax.plot(data["Angle °"], data["cd"], color="steelblue")
        
        # Afficher le graphique
        self.display_plot()
    
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
            self.ax.plot(
                zone["x"], zone["y"], color="red", linestyle="--", alpha=0.5
            )
            self.ax.fill(
                zone["x"],
                zone["y"],
                color="red",
                alpha=0.2,
                label=f"Zone limite {zone_num}",
            )
        
        self.ax.set_title("Intensité lumineuse en fonction de l'angle")
        self.ax.set_xlabel("Angle (°)")
        self.ax.set_ylabel("Intensité lumineuse (cd)")
        self.ax.minorticks_on()
        self.ax.grid(which="major", alpha=0.7)
        self.ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
    
    def display_plot(self):
        """Affiche le graphique matplotlib"""
        # Nettoyer la frame
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        
        # Canvas matplotlib
        canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.plot_frame)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)