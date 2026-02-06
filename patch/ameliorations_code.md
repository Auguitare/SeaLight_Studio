# Améliorations du code - Analyse PEP 8 et bonnes pratiques

## 🔴 PROBLÈMES CRITIQUES

### 1. Encodage des caractères
**Problème** : Nombreux caractères mal encodés (É, Ã, etc.)
**Solution** :
```python
# Ajouter en première ligne de TOUS les fichiers :
# -*- coding: utf-8 -*-
```

### 2. Noms de variables non conformes (PEP 8)
**Problème** : Utilisation de CamelCase pour des variables
```python
# ❌ Incorrect
self.file_choosen  # devrait être "chosen"
self.var_secteur
self.var_range
self.label_fichier_photo
```

**Solution** :
```python
# ✅ Correct (tout en minuscules avec underscores)
self.file_chosen  # correction orthographique aussi
self.sector_var
self.range_var
self.photo_file_label
```

## 🟡 PROBLÈMES MAJEURS

### 3. Imports non organisés (PEP 8 E401)
**Problème** : Ordre incorrect des imports
```python
# Actuel dans main.py
import platform
import tkinter as tk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import file_orga as f
import tab_photo as p
import tab_colo as c
```

**Solution** :
```python
# Standard library imports
import platform
import tkinter as tk

# Third party imports
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

# Local application imports
import file_orga
import tab_photo
import tab_colo

# Éviter les alias d'une lettre (f, p, c) - pas clair
```

### 4. Constantes magiques non définies
**Problème** : Valeurs hardcodées partout
```python
# Dans zone.py
case 1:
    max_power = 1.1
case 2:
    max_power = 5.4
```

**Solution** :
```python
# En haut du fichier zone.py
LIGHT_RANGE_POWERS = {
    1: 1.1,
    2: 5.4,
    3: 15,
    4: 33,
    5: 65,
    6: 118,
}

# Utilisation
max_power = LIGHT_RANGE_POWERS.get(light_range, 0)
if max_power == 0:
    tk.messagebox.showwarning("Avertissement", "Choisir une portée valide (1-6).")
```

### 5. Type hints manquants
**Problème** : Pas d'annotations de type
```python
# ❌ Actuel
def trace_graph(data, ax, decalage, previous_line=None):
```

**Solution** :
```python
# ✅ Avec type hints
from typing import Optional
import pandas as pd
import matplotlib.axes

def trace_graph(
    data: pd.DataFrame,
    ax: matplotlib.axes.Axes,
    decalage: tk.StringVar,
    previous_line: Optional[matplotlib.lines.Line2D] = None
) -> matplotlib.lines.Line2D:
```

### 6. Longueur de ligne excessive (PEP 8 E501)
**Problème** : Lignes dépassant 79-88 caractères
```python
# ❌ Trop long
self.label_fichier_photo = ctk.CTkLabel(tab_photo, text="Aucun fichier sélectionné")
```

**Solution** :
```python
# ✅ Correct
self.label_fichier_photo = ctk.CTkLabel(
    tab_photo,
    text="Aucun fichier sélectionné"
)
```

## 🟢 PROBLÈMES MINEURS

### 7. Docstrings non conformes (PEP 257)
**Problème** : Docstrings manquent de détails
```python
# ❌ Actuel
def trace_graph(data, ax, decalage, previous_line=None):
    """
    Trace le graphique de l'intensité lumineuse.
    """
```

**Solution** :
```python
# ✅ Google Style
def trace_graph(data, ax, decalage, previous_line=None):
    """Trace le graphique de l'intensité lumineuse avec décalage angulaire.
    
    Args:
        data: DataFrame contenant les colonnes 'Angle °' et 'cd'.
        ax: Axe matplotlib pour le traçage.
        decalage: Variable tkinter contenant le décalage en degrés.
        previous_line: Ligne précédente à supprimer, si existante.
    
    Returns:
        Objet Line2D représentant la courbe tracée.
    
    Raises:
        ValueError: Si le décalage n'est pas convertible en float.
    
    Example:
        >>> line = trace_graph(df, ax, StringVar(value="5.0"))
    """
```

### 8. Gestion d'erreurs améliorable
**Problème** : Try/except trop large ou silencieux
```python
# Dans file_orga.py
try:
    val_decalage = float(decalage.get())
except ValueError:
    val_decalage = 0.0  # Silencieux - l'utilisateur ne sait pas
```

**Solution** :
```python
try:
    val_decalage = float(decalage.get())
except ValueError:
    tk.messagebox.showwarning(
        "Valeur invalide",
        f"Le décalage '{decalage.get()}' n'est pas valide. Utilisation de 0.0."
    )
    val_decalage = 0.0
```

### 9. Méthode match/case
**Problème** : Bon usage de match/case, mais peut être simplifié
```python
# Actuel - correct mais verbeux
match light_range:
    case 1:
        max_power = 1.1
    case 2:
        max_power = 5.4
    # etc.
```

**Solution** :
```python
# Plus simple et maintenable
LIGHT_RANGE_POWERS = {1: 1.1, 2: 5.4, 3: 15, 4: 33, 5: 65, 6: 118}
max_power = LIGHT_RANGE_POWERS.get(light_range)
if max_power is None:
    tk.messagebox.showwarning("Avertissement", "Choisir une portée (1-6).")
    return None
```

### 10. Espaces autour des opérateurs (PEP 8 E225)
**Problème** : Inconsistance dans les espaces
```python
# ❌ Inconsistent
x_factor_l = int(zone_interdite[2]["X"][3])
filtered_data = data[(data["Angle °"]>=x_factor_l)&(data["Angle °"]<=x_factor_r)]
```

**Solution** :
```python
# ✅ Espaces cohérents
x_factor_l = int(zone_interdite[2]["X"][3])
filtered_data = data[
    (data["Angle °"] >= x_factor_l) & (data["Angle °"] <= x_factor_r)
]
```

## 📋 STRUCTURE ET ORGANISATION

### 11. Séparation des responsabilités
**Amélioration** : Créer des classes pour mieux organiser

**Actuel** :
```python
# Tout dans des fonctions module-level
def hune(light_range=1, inclinaison=0):
def poupe(light_range=1, inclinaison=0):
def babord(light_range=1, inclinaison=0):
```

**Suggestion** :
```python
# zone.py
class NavigationLightZone:
    """Gestionnaire des zones de feux de navigation."""
    
    LIGHT_RANGE_POWERS = {1: 1.1, 2: 5.4, 3: 15, 4: 33, 5: 65, 6: 118}
    
    def __init__(self, light_range: int, inclinaison: float = 0):
        self.light_range = light_range
        self.inclinaison = inclinaison
        self.max_power = self._calculate_max_power()
    
    def _calculate_max_power(self) -> float:
        """Calcule la puissance maximale."""
        power = self.LIGHT_RANGE_POWERS.get(self.light_range)
        if power is None:
            raise ValueError(f"Portée invalide: {self.light_range}")
        return power * (0.5 if self.inclinaison != 0 else 1.0)
    
    def get_hune_zones(self) -> dict:
        """Retourne les zones pour feu de hune."""
        # ...
```

### 12. Configuration centralisée
**Suggestion** : Créer un fichier `config.py`

```python
# config.py
"""Configuration de l'application."""

# Constantes d'interface
WINDOW_TITLE = "Analyse des données photométrique des feux de navigation"
DEFAULT_SECTOR = "Vide"
DEFAULT_RANGE = "2"
DEFAULT_ANGLE = 0
DEFAULT_OFFSET = "0.0"

# Constantes de calcul
INTENSITY_FACTOR = 1.5
INCLINATION_POWER_REDUCTION = 0.5

# Zones de couleur pour colorimétrie
COLOR_ZONES = {
    'white': {
        'X': [0.525, 0.525, 0.452, 0.310, 0.31, 0.443, 0.525],
        'Y': [0.382, 0.44, 0.44, 0.348, 0.283, 0.382, 0.382],
    },
    'green': {
        'X': [0.028, 0.009, 0.3, 0.203, 0.028],
        'Y': [0.385, 0.723, 0.511, 0.356, 0.385],
    },
    # etc.
}

# Colonnes requises dans les fichiers
REQUIRED_COLUMNS = ["Angle °", "cd", "lux", "X", "Y"]
```

### 13. Logging au lieu de print
**Problème** :
```python
print(f"Impossible de charger l'icône: {e}")
```

**Solution** :
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Usage
logger.warning(f"Impossible de charger l'icône: {e}")
```

## 🎯 PLAN D'ACTION PRIORITAIRE

### Phase 1 - Critique (à faire immédiatement)
1. ✅ Fixer l'encodage UTF-8 en haut de tous les fichiers
2. ✅ Corriger `file_choosen` → `file_chosen`
3. ✅ Extraire les constantes magiques (LIGHT_RANGE_POWERS)
4. ✅ Organiser les imports selon PEP 8

### Phase 2 - Important (semaine suivante)
5. ✅ Ajouter les type hints
6. ✅ Améliorer les docstrings
7. ✅ Créer config.py pour centraliser les constantes
8. ✅ Ajouter validation et feedback pour les erreurs silencieuses

### Phase 3 - Amélioration continue
9. ✅ Ajouter des tests unitaires
10. ✅ Refactoriser en classes si le projet grandit
11. ✅ Ajouter logging
12. ✅ Documenter l'API avec Sphinx

## 📝 CHECKLIST PEP 8

- [ ] Encodage UTF-8 déclaré
- [ ] Imports groupés et triés (stdlib, third-party, local)
- [ ] Lignes < 79-88 caractères
- [ ] 2 lignes blanches entre fonctions de module
- [ ] 1 ligne blanche entre méthodes de classe
- [ ] Espaces autour des opérateurs
- [ ] Pas d'espace avant les parenthèses de fonction
- [ ] Noms en snake_case pour variables/fonctions
- [ ] Noms en PascalCase pour classes
- [ ] MAJUSCULES pour constantes
- [ ] Docstrings pour modules, classes, fonctions publiques
- [ ] Type hints pour signatures de fonctions

## 🔧 OUTILS RECOMMANDÉS

```bash
# Formatage automatique
pip install black isort

# Vérification
pip install flake8 pylint mypy

# Usage
black *.py          # Formatage automatique
isort *.py          # Tri des imports
flake8 *.py         # Vérification PEP 8
pylint *.py         # Analyse approfondie
mypy *.py           # Vérification des types
```
