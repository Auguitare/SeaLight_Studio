import tkinter as tk



def choisir_fichier():
    global fichier_selectionne, dernier_dossier
    fichier_selectionne = tk.filedialog.askopenfilename(
        title="Choisir un fichier de données",
        filetypes=[
            ("Fichiers texte", "*.txt"),
            ("Fichiers de calcul", "*.csv"),
            ("Tous les fichiers", "*.*"),
        ],
    )

    if fichier_selectionne:
        dernier_dossier = "/".join(fichier_selectionne.split("/")[:-1])
        print(dernier_dossier)
        # label_fichier.configure(
        #     text=f"Fichier sélectionné : {fichier_selectionne.split('/')[-1]}"
        # )
    else:
        print("else")
        # label_fichier.configure(text="Aucun fichier sélectionné")
