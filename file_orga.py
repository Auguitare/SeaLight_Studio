import tkinter as tk



def choisir_fichier():
    fichier_selectionne = tk.filedialog.askopenfilename(
        title="Choisir un fichier de données",
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Fichiers de calcul", "*.csv"),
            ("Tous les fichiers", "*.*"),
        ],
    )

    return fichier_selectionne
