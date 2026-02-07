# Analyseur de Feux de Navigation - SeaLight_Studio

Application d'analyse des données photométriques et colorimétriques pour les feux de navigation maritime conformes aux normes Wheelmark et USCG/ABYC-C5.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![iso](https://img.shields.io/badge/LA-RACHE-blue.svg)


## Table des matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Format des données](#format-des-données)
- [Normes et références](#normes-et-références)
- [Contribuer](#contribuer)
- [Licence](#licence)

## Aperçu

Cette application permet d'analyser et de valider la conformité des feux de navigation maritime en traçant :
- **Courbes photométriques** : Intensité lumineuse (cd) en fonction de l'angle
- **Diagrammes colorimétriques** : Coordonnées chromatiques (X, Y) sur le diagramme CIE

L'outil aide à la vérification de la conformité avec les zones réglementaires pour différents types de feux :
- Feu de hune (masthead light)
- Feu de poupe (stern light)
- Feu de bâbord (port light)
- Feu de tribord (starboard light)

## ✨ Fonctionnalités

### Analyse photométrique
- ✅ Tracé de l'intensité lumineuse en fonction de l'angle
- ✅ Application de décalages angulaires
- ✅ Visualisation des zones de conformité selon le secteur
- ✅ Calcul du facteur d'intensité (ratio max/min × 1.5)
- ✅ Support des inclinaisons (0° et ±25°)
- ✅ Portées de 1 à 6 miles nautiques

### Analyse colorimétrique
- ✅ Diagramme de chromaticité CIE (X, Y)
- ✅ Zones réglementaires pour :
  - Blanc (white)
  - Vert (green)
  - Rouge (red)
  - Jaune (yellow)

### Interface utilisateur
- Interface graphique moderne avec CustomTkinter
- Graphiques interactifs avec Matplotlib
- Zoom et navigation dans les graphiques
- Raccourcis clavier (Entrée pour tracer)
- Import de fichiers CSV/TXT
- Création une application portable

## 🔧 Installation

### Prérequis

- Python 3.10 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation du projet

1. Clonez ou téléchargez le projet :
```bash
git clone https://github.com/Auguitare/SeaLight_Studio.git
cd SeaLight_Studio
```

2. Installez les bibliothèques nécessaires :
```bash
sudo apt install python3.12-venv
```

3. Créez l'environement
```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Installez les dépendances sont installées :
```bash
pip install -r requirements.txt
```

5. Lancez l'application :
```bash
python main.py
```
6. Creez une application portable
    - consultez le fichier `instruction.md`

## Utilisation

### Lancement rapide

1. **Démarrez l'application** :

    ```bash
    source .venv/bin/activate
    python main.py
    ```

2. **Choisissez un fichier de données** :
    - Cliquez sur "Choisir un fichier"
    - Sélectionnez votre fichier CSV ou TXT

3. **Configurez les paramètres** (onglet Photométrie) :
    - Secteur : Hune, Poupe, Bâbord, Tribord ou Vide
    - Portée : 1 à 6 miles nautiques
    - Inclinaison du test  : 0° ou ±25° (±5° ayant les même contrainte qu'à 0)

4. **Tracez le graphique** :
    - Cliquez sur "Tracer le graphique" ou appuyez sur Entrée

5. **Ajustez votre graphique**
    - Utilisez l'entrée "Décalage [°]" pour ajuster la position de votre graphique dans les bornes des secteurs

6. **Ajustez le visuel**
    - Ajustez si besoin le zoom et la position du graphique avec la toolbar en dessous 

7. **Sauvegardez**
    - Sauvegardez votre graphique en PNG avec la dernière icone de la toolbar

### Guide détaillé

#### Onglet Photométrie

**Paramètres disponibles :**

| Paramètre | Description | Valeurs |
|-----------|-------------|---------|
| Secteur | Type de feu à analyser | Hune, Poupe, Bâbord, Tribord, Vide |
| Portée | Distance en miles nautiques | 1, 2, 3, 4, 5, 6 |
| Inclinaison | Angle d'inclinaison du test | 0°, ±25° |
| Décalage | Correction angulaire (en degrés) | Valeur décimale |
| Facteur 1.5 | Affiche le facteur d'intensité | Checkbox |

**Lecture du graphique :**
- **Courbe bleue** : Intensité mesurée
- **Zones rouges** : Zones interdites (non-conformité)
- **Point rouge** (si facteur activé) : Intensité minimale dans la zone
- **Ligne rouge pointillée** : Seuil du facteur 1.5

#### Onglet Colorimétrie

Affiche le diagramme chromatique avec :
- **Points noirs** : Mesures de votre feu
- **Zones colorées** : Zones réglementaires pour chaque couleur

Les points doivent se situer dans la zone correspondant à la couleur du feu.

### Raccourcis clavier

- `Entrée` : Tracer le graphique de l'onglet actif (marche aussi avec le Keyboard)
- `Ctrl+O` : Ouvrir un fichier

## 📁 Structure du projet

```
SeaLight_Studio/
│
├── main.py              # Application principale
├── tab_photo.py         # Gestion de l'affichage photométrique
├── tab_colo.py          # Gestion de l'affichage colorimétrique
├── zone.py              # Calculs des zones de conformité
├── file_orga.py         # Gestion des fichiers
│
├── icon.ico             # Icône Windows (optionnel)
├── icon.png             # Icône Linux/Mac (optionnel)
│
├── README.md            # Ce fichier
└── requirements.txt     # Liste des dépendances
```

### Description des modules

#### `main.py`
Point d'entrée de l'application. Gère :
- Interface utilisateur (fenêtre, onglets, boutons)
- Coordination entre les différents modules
- Gestion des événements utilisateur

#### `tab_photo.py`
Module de photométrie. Fonctions principales :
- `trace_graph()` : Trace la courbe d'intensité
- `trace_limit()` : Affiche les zones réglementaires
- `trace_factor()` : Calcule et affiche le facteur d'intensité

#### `tab_colo.py`
Module de colorimétrie. Fonctions principales :
- `trace_graph()` : Trace les points chromatiques
- `trace_limit()` : Affiche les zones de couleur réglementaires

#### `zone.py`
Calculs des zones de conformité. Fonctions :
- `intensity_calc()` : Calcule les intensités limites
- `hune()`, `poupe()`, `babord()`, `tribord()` : Définit les coordonnées des zones

#### `file_orga.py`
Gestion des fichiers. Fonctions :
- `choisir_fichier()` : Dialogue de sélection de fichier
- `read_file()` : Lecture et parsing des données

## 📊 Format des données

### Format CSV/TXT attendu

Le fichier doit contenir une ligne d'en-tête avec le mot "Angle" suivie des données :

```csv
Angle °;cd;lux;X;Y
-180.0;0.52;0.12;0.315;0.330
-179.0;0.54;0.13;0.316;0.331
...
```

**Colonnes requises :**
- `Angle °` : Angle de mesure (en degrés)
- `cd` : Intensité lumineuse (en candelas)
- `lux` : Éclairement (en lux)
- `X` : Coordonnée chromatique X (CIE 1931)
- `Y` : Coordonnée chromatique Y (CIE 1931)

**Format du fichier :**
- Séparateur : point-virgule (`;`)
- Encodage : UTF-8
- Les deux dernières lignes sont ignorées (généralement métadonnées)

### Exemple de fichier

```
Informations du test
Date: 2024-02-07
Équipement: Feu de navigation LED
---
Angle °;cd;lux;X;Y
0.0;5.8;1.35;0.320;0.335
1.0;5.7;1.33;0.321;0.336
2.0;5.6;1.30;0.319;0.334
...
Notes complémentaires
Fin du fichier
```

## Normes et références

### Normes appliquées

- **USCG (United States Coast Guard)**
- **ABYC-C5** : American Boat & Yacht Council - Standard C5

### Portées et intensités

| Portée (NM) | Intensité minimale (cd) à 0° | Intensité minimale (cd) à ±25° |
|-------------|------------------------------|--------------------------------|
| 1           | 1.1                          | 0.55                           |
| 2           | 5.4                          | 2.7                            |
| 3           | 15                           | 7.5                            |
| 4           | 33                           | 16.5                           |
| 5           | 65                           | 32.5                           |
| 6           | 118                          | 59                             |

### Secteurs angulaires

| Type de feu | Secteur horizontal |
|-------------|-------------------|
| Hune        | 225° (112.5° B/T) vers l'avant |
| Poupe       | 135° (67.5° B/T) vers l'arrière  |
| Bâbord      | 112.5° (vers B)   |
| Tribord     | 112.5° (vers T)   |

### Couleurs réglementaires (coordonnées CIE)

**Blanc :**
- X: 0.310 - 0.525
- Y: 0.283 - 0.440

**Vert :**
- X: 0.009 - 0.300
- Y: 0.356 - 0.723

**Rouge :**
- X: 0.660 - 0.735
- Y: 0.259 - 0.320

**Jaune :**
- X: 0.575 - 0.618
- Y: 0.382 - 0.425

## Dépannage

### L'application ne se lance pas

**Problème** : `ModuleNotFoundError: No module named 'customtkinter'`

**Solution** :
```bash
pip install customtkinter
```

### Erreur lors du chargement du fichier

**Problème** : "Colonnes manquantes dans le fichier"

**Solution** :
- Vérifiez que votre fichier contient bien les colonnes : `Angle °`, `cd`, `lux`, `X`, `Y`
- Vérifiez que le séparateur est un point-virgule (`;`)

### L'icône ne s'affiche pas

**Problème** : Warning "Impossible de charger l'icône"

**Solution** :
- Sur Windows : Placez `icon.ico` dans le même dossier que `main.py`
- Sur Linux/Mac : Placez `icon.png` dans le même dossier que `main.py`
- Ce warning n'empêche pas l'application de fonctionner

### Les zones ne s'affichent pas correctement

**Problème** : Zones rouges absentes ou mal positionnées

**Solution** :
- Vérifiez que vous avez sélectionné un secteur (pas "Vide")
- Vérifiez que la portée est configurée (1-6)
- Relancez le tracé avec "Tracer le graphique"

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment participer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

### Axes d'amélioration

- [ ] Export des résultats en PDF
- [ ] Génération de rapports de conformité
- [ ] Base de données de mesures
- [ ] Comparaison entre plusieurs feux
- [ ] Mode batch pour analyser plusieurs fichiers

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Auteur

Développé avec ❤️ pour l'analyse de conformité des feux de navigation maritime.

## Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Consultez la documentation des normes USCG/ABYC-C5

---

**Note** : Cette application est un outil d'aide à l'analyse. Les résultats doivent être validés par un organisme certifié pour une homologation officielle.