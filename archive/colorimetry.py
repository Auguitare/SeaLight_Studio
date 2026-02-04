import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class ColorimetryTab:
    """Gère l'onglet de colorimétrie"""
    
    def __init__(self, parent_tab, app):
        self.tab = parent_tab
        self.app = app  # Référence à l'application principale
        
        # Figure matplotlib
        self.fig = Figure(figsize=(8, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        # Construire l'interface
        self.setup_ui()
    
    def setup_ui(self):
        """Construit l'interface de l'onglet colorimétrie"""
        # Configuration de la grille
        self.tab.grid_rowconfigure(0, weight=0)
        self.tab.grid_rowconfigure(1, weight=0)
        self.tab.grid_rowconfigure(2, weight=1)
        self.tab.grid_columnconfigure(0, weight=1)
        self.tab.grid_columnconfigure(1, weight=1)
        self.tab.grid_columnconfigure(2, weight=1)
        
        # === Ligne 0 ===
        label_info = ctk.CTkLabel(
            self.tab,
            text="Colorimétrie - Diagramme de chromaticité (X, Y)",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        label_info.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")
        
        # === Ligne 1 ===
        button_fichier = ctk.CTkButton(
            self.tab, text="Choisir un fichier", command=self.choisir_fichier
        )
        button_fichier.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        self.label_fichier = ctk.CTkLabel(self.tab, text="Aucun fichier sélectionné")
        self.label_fichier.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        button_trace = ctk.CTkButton(
            self.tab, text="Tracer le graphique", command=self.trace_graph
        )
        button_trace.grid(row=1, column=2, padx=10, pady=5, sticky="e")
        
        # === Ligne 2 : Zone du graphe ===
        self.plot_frame = ctk.CTkFrame(self.tab)
        self.plot_frame.grid(
            row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew"
        )
    
    def choisir_fichier(self):
        """Utilise la fonction de l'application principale pour choisir un fichier"""
        self.app.choisir_fichier(self)
    
    def trace_graph(self):
        """Trace le graphique de colorimétrie"""
        self.ax.clear()
        
        data = self.app.read_file()
        if data is None:
            return
        
        # Tracer les données
        self.ax.plot(data["X"], data["Y"], color="steelblue", marker="o", markersize=3)
        
        self.ax.set_title("Diagramme de chromaticité")
        self.ax.set_xlabel("Coordonnée X")
        self.ax.set_ylabel("Coordonnée Y")
        self.ax.minorticks_on()
        self.ax.grid(which="major", alpha=0.7)
        self.ax.grid(which="minor", linestyle="--", linewidth=0.5, alpha=0.4)
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        
        # Afficher le graphique
        self.display_plot()
    
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