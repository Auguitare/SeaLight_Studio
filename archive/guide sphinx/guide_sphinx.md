# Guide Sphinx - Documentation Python professionnelle

## 📚 Qu'est-ce que Sphinx ?

Sphinx est le générateur de documentation de référence pour Python. Il :
- Convertit vos docstrings Python en documentation HTML/PDF élégante
- Est utilisé par la documentation officielle de Python
- Supporte plusieurs formats de sortie (HTML, PDF, ePub, etc.)
- Génère automatiquement l'API depuis votre code
- Permet d'écrire des tutoriels en reStructuredText ou Markdown

### Exemples de projets utilisant Sphinx
- Documentation officielle Python (https://docs.python.org)
- NumPy, Pandas, Django, Flask
- Pratiquement tous les grands projets Python

## 🚀 Installation et configuration

### Installation

```bash
pip install sphinx sphinx-rtd-theme sphinx-autodoc-typehints

# Pour support Markdown (optionnel)
pip install myst-parser
```

### Initialisation du projet

```bash
# Se placer dans votre projet
cd /path/to/votre_projet

# Créer le dossier docs
mkdir docs
cd docs

# Lancer l'assistant de configuration
sphinx-quickstart
```

L'assistant vous posera plusieurs questions :

```
> Separate source and build directories (y/n) [n]: y
> Project name: Analyse Photométrique Feux Navigation
> Author name(s): Votre Nom
> Project release []: 1.0.0
> Project language [en]: fr
```

Cela créera la structure :

```
votre_projet/
├── docs/
│   ├── build/           # Documentation générée (HTML, PDF, etc.)
│   ├── source/          # Fichiers source de la documentation
│   │   ├── conf.py      # Configuration Sphinx
│   │   ├── index.rst    # Page d'accueil
│   │   └── _static/     # CSS, images, etc.
│   └── Makefile         # Commandes de build
├── file_orga.py
├── main.py
└── ...
```

## ⚙️ Configuration (conf.py)

Voici une configuration recommandée pour votre projet :

```python
# docs/source/conf.py

import os
import sys

# Ajouter le chemin de votre code source
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'Analyse Photométrique Feux Navigation'
copyright = '2024, Votre Nom'
author = 'Votre Nom'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',        # Extraction automatique des docstrings
    'sphinx.ext.napoleon',       # Support Google/NumPy docstring style
    'sphinx.ext.viewcode',       # Liens vers le code source
    'sphinx.ext.todo',           # Support des TODO
    'sphinx.ext.coverage',       # Vérification de la couverture doc
    'sphinx.ext.mathjax',        # Équations mathématiques
    'sphinx.ext.intersphinx',    # Liens vers autre doc (ex: NumPy)
    'sphinx_autodoc_typehints',  # Support type hints
    # 'myst_parser',             # Support Markdown (optionnel)
]

# Napoleon settings (docstrings Google/NumPy style)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = True

# Intersphinx mapping (liens vers docs externes)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None),
}

# Templates path
templates_path = ['_templates']

# Language
language = 'fr'

# Patterns à exclure
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Thème ReadTheDocs (élégant)
html_static_path = ['_static']

# Thème options
html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
}

# -- Options for PDF output --------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
}
```

## 📝 Structure de la documentation

### index.rst (Page d'accueil)

```rst
Analyse Photométrique des Feux de Navigation
=============================================

Bienvenue dans la documentation de l'application d'analyse photométrique
et colorimétrique des feux de navigation maritimes.

.. toctree::
   :maxdepth: 2
   :caption: Table des matières:

   installation
   guide_utilisateur
   api
   exemples
   developpement

Introduction
------------

Cette application permet d'analyser les données photométriques et colorimétriques
des feux de navigation selon les normes maritimes internationales.

Fonctionnalités principales
----------------------------

* Analyse photométrique avec zones de conformité
* Diagramme colorimétrique CIE
* Calcul du facteur d'intensité
* Export des graphiques

Démarrage rapide
----------------

Installation::

   pip install -r requirements.txt

Lancement::

   python main.py

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

### api.rst (Documentation API)

```rst
Documentation API
=================

Modules principaux
------------------

Module file_orga
~~~~~~~~~~~~~~~~

.. automodule:: file_orga
   :members:
   :undoc-members:
   :show-inheritance:

Module zone
~~~~~~~~~~~

.. automodule:: zone
   :members:
   :undoc-members:
   :show-inheritance:

Module tab_photo
~~~~~~~~~~~~~~~~

.. automodule:: tab_photo
   :members:
   :undoc-members:
   :show-inheritance:

Module tab_colo
~~~~~~~~~~~~~~~

.. automodule:: tab_colo
   :members:
   :undoc-members:
   :show-inheritance:

Classe principale
-----------------

.. autoclass:: main.Application
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__
```

### installation.rst

```rst
Installation
============

Prérequis
---------

* Python 3.10 ou supérieur
* pip

Dépendances
-----------

Les packages suivants sont requis :

* tkinter (inclus avec Python)
* customtkinter >= 5.0
* pandas >= 2.0
* matplotlib >= 3.5

Installation des dépendances
-----------------------------

Via pip::

   pip install -r requirements.txt

Ou individuellement::

   pip install customtkinter pandas matplotlib

Vérification de l'installation
-------------------------------

Pour vérifier que tout fonctionne::

   python -c "import customtkinter, pandas, matplotlib; print('OK')"
```

### guide_utilisateur.rst

```rst
Guide utilisateur
=================

Interface principale
--------------------

L'application comprend deux onglets principaux :

1. **Photométrie** : Analyse de l'intensité lumineuse
2. **Colorimétrie** : Diagramme chromatique CIE

Utilisation - Photométrie
--------------------------

1. Sélectionner le secteur du feu
   
   * Hune (feu de mât)
   * Poupe (feu arrière)
   * Bâbord (feu rouge gauche)
   * Tribord (feu vert droit)

2. Choisir la portée (1-6)

3. Sélectionner un fichier de données (.csv ou .txt)

4. (Optionnel) Entrer un décalage angulaire

5. Cliquer sur "Tracer le graphique"

Facteur d'intensité
~~~~~~~~~~~~~~~~~~~

Pour afficher le facteur d'intensité (ratio max/min) :

1. Cocher "Facteur d'intensité 1.5"
2. Le point minimal apparaît en rouge
3. Une ligne orange à 1.5× la valeur minimale est affichée

.. note::
   Le facteur d'intensité n'est disponible que si un secteur
   (autre que "Vide") est sélectionné.

.. image:: _static/screenshots/photometrie.png
   :width: 600px
   :align: center
   :alt: Interface photométrie

Utilisation - Colorimétrie
---------------------------

1. Sélectionner un fichier de données

2. Cliquer sur "Tracer le graphique"

3. Les points sont affichés sur le diagramme CIE avec les zones de couleur

.. warning::
   Le fichier doit contenir les colonnes X et Y pour la colorimétrie.
```

## 🎨 Formats de docstrings supportés

Sphinx supporte plusieurs styles via l'extension Napoleon :

### Style Google (recommandé - plus lisible)

```python
def trace_factor(ax, data, secteur):
    """Calcule et trace le facteur d'intensité.
    
    Le facteur est le ratio entre l'intensité maximale et minimale
    dans une zone spécifique définie par le secteur.
    
    Args:
        ax (matplotlib.axes.Axes): Axe matplotlib pour le traçage.
        data (pd.DataFrame): Données avec colonnes 'Angle °' et 'cd'.
        secteur (str): Nom du secteur ("Hune", "Poupe", etc.).
    
    Returns:
        list: Liste contenant les objets graphiques tracés.
    
    Raises:
        ValueError: Si le secteur est inconnu.
    
    Example:
        >>> artists = trace_factor(ax, df, "Hune")
        >>> len(artists)
        2
    
    Note:
        Cette fonction trace à la fois le point minimal et
        la ligne horizontale à 1.5× cette valeur.
    
    See Also:
        trace_graph: Pour tracer la courbe principale
        trace_limit: Pour tracer les limites réglementaires
    """
```

### Style NumPy (plus verbeux)

```python
def trace_factor(ax, data, secteur):
    """
    Calcule et trace le facteur d'intensité.
    
    Le facteur est le ratio entre l'intensité maximale et minimale
    dans une zone spécifique définie par le secteur.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axe matplotlib pour le traçage.
    data : pd.DataFrame
        Données avec colonnes 'Angle °' et 'cd'.
    secteur : str
        Nom du secteur ("Hune", "Poupe", etc.).
    
    Returns
    -------
    list
        Liste contenant les objets graphiques tracés.
    
    Raises
    ------
    ValueError
        Si le secteur est inconnu.
    
    Examples
    --------
    >>> artists = trace_factor(ax, df, "Hune")
    >>> len(artists)
    2
    
    Notes
    -----
    Cette fonction trace à la fois le point minimal et
    la ligne horizontale à 1.5× cette valeur.
    
    See Also
    --------
    trace_graph : Pour tracer la courbe principale
    trace_limit : Pour tracer les limites réglementaires
    """
```

## 🔨 Génération de la documentation

### Commandes principales

```bash
# Générer HTML
cd docs
make html

# Ouvrir dans le navigateur
# Linux/Mac
open build/html/index.html
# Windows
start build/html/index.html

# Générer PDF
make latexpdf

# Nettoyer et régénérer
make clean
make html

# Vérifier la couverture de la documentation
make coverage
```

### Automatisation avec watch

Pour régénérer automatiquement lors des modifications :

```bash
pip install sphinx-autobuild

# Lancer le serveur avec auto-reload
sphinx-autobuild source build/html --port 8000
```

Puis ouvrir http://localhost:8000

## 📊 Directives utiles

### Admonitions (notes, warnings, etc.)

```rst
.. note::
   Ceci est une note importante.

.. warning::
   Attention à ce point !

.. danger::
   Action dangereuse !

.. tip::
   Astuce utile.

.. seealso::
   Voir aussi cette section.
```

### Code avec coloration syntaxique

```rst
.. code-block:: python
   :linenos:
   :emphasize-lines: 3,5

   def ma_fonction():
       x = 10
       y = 20  # ligne mise en évidence
       z = 30
       return x + y + z  # ligne mise en évidence
```

### Images

```rst
.. image:: _static/image.png
   :width: 400px
   :align: center
   :alt: Texte alternatif

.. figure:: _static/graph.png
   :scale: 50%
   :align: center

   Légende de la figure
```

### Tables

```rst
.. list-table:: Portées et puissances
   :widths: 20 80
   :header-rows: 1

   * - Portée
     - Puissance (cd)
   * - 1
     - 1.1
   * - 2
     - 5.4
   * - 3
     - 15.0
```

### Équations mathématiques

```rst
La formule d'intensité est :

.. math::

   I_{facteur} = \frac{I_{max}}{I_{min}}

Ou inline : :math:`I = I_0 \times 1.5`
```

## 🎨 Thèmes populaires

### Read the Docs Theme (recommandé)

```bash
pip install sphinx-rtd-theme
```

```python
# conf.py
html_theme = 'sphinx_rtd_theme'
```

### Autres thèmes

```bash
# Thème Book (élégant)
pip install sphinx-book-theme
html_theme = 'sphinx_book_theme'

# Thème PyData (moderne)
pip install pydata-sphinx-theme
html_theme = 'pydata_sphinx_theme'

# Thème Furo (minimaliste)
pip install furo
html_theme = 'furo'
```

## 🚀 Publication de la documentation

### GitHub Pages (gratuit)

1. Générer la doc :
```bash
make html
```

2. Créer un fichier `.nojekyll` dans `build/html/`

3. Pousser le dossier `build/html/` sur la branche `gh-pages`

4. Activer GitHub Pages dans les settings du repo

### Read the Docs (gratuit, recommandé)

1. Créer un compte sur https://readthedocs.org

2. Connecter votre repo GitHub

3. Créer un fichier `.readthedocs.yaml` :

```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

sphinx:
  configuration: docs/source/conf.py

python:
  install:
    - requirements: requirements.txt
```

4. La doc sera automatiquement générée à chaque commit !

## 📦 Exemple complet pour votre projet

Structure finale :

```
votre_projet/
├── docs/
│   ├── source/
│   │   ├── conf.py
│   │   ├── index.rst
│   │   ├── installation.rst
│   │   ├── guide_utilisateur.rst
│   │   ├── api.rst
│   │   ├── exemples.rst
│   │   ├── developpement.rst
│   │   └── _static/
│   │       └── screenshots/
│   ├── build/
│   └── Makefile
├── file_orga.py
├── main.py
├── tab_photo.py
├── tab_colo.py
├── zone.py
├── config.py
├── requirements.txt
└── README.md
```

### Workflow recommandé

1. Écrire le code avec de bonnes docstrings
2. Lancer `make html` régulièrement pour vérifier
3. Ajouter des pages de guide utilisateur en RST
4. Publier sur Read the Docs
5. Mettre à jour à chaque release

## 🎯 Avantages de Sphinx

✅ **Professionnel** : Aspect standardisé et reconnu
✅ **Automatique** : Docstrings → Documentation sans effort
✅ **Multi-format** : HTML, PDF, ePub, etc.
✅ **Recherche** : Index et recherche intégrés
✅ **Versionning** : Support de plusieurs versions de doc
✅ **Interactivité** : Liens croisés entre sections
✅ **Gratuit** : Hébergement gratuit sur Read the Docs

Avec Sphinx, votre projet aura une documentation aussi professionnelle 
que celle de NumPy ou Django ! 🚀
