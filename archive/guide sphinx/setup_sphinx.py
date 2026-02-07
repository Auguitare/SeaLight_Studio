#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Script d'initialisation automatique de Sphinx pour le projet.

Ce script crée automatiquement la structure de documentation Sphinx
sans passer par l'assistant interactif.

Usage:
    python setup_sphinx.py
"""

import os
import shutil
from pathlib import Path


def create_sphinx_structure():
    """Crée la structure complète de documentation Sphinx."""
    
    print("🚀 Initialisation de Sphinx...")
    
    # Créer les dossiers
    docs_dir = Path("docs")
    source_dir = docs_dir / "source"
    build_dir = docs_dir / "build"
    static_dir = source_dir / "_static"
    templates_dir = source_dir / "_templates"
    
    for directory in [docs_dir, source_dir, build_dir, static_dir, templates_dir]:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"✅ Dossier créé: {directory}")
    
    # Créer le Makefile
    makefile_content = """# Minimal makefile for Sphinx documentation

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help Makefile

help:
\t@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
\t@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
"""
    
    (docs_dir / "Makefile").write_text(makefile_content)
    print("✅ Makefile créé")
    
    # Créer make.bat pour Windows
    make_bat_content = """@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
\tset SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
\techo.
\techo.The 'sphinx-build' command was not found.
\tgoto end
)

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
"""
    
    (docs_dir / "make.bat").write_text(make_bat_content)
    print("✅ make.bat créé")
    
    # Créer index.rst de base
    index_content = """Analyse Photométrique des Feux de Navigation
=============================================

Bienvenue dans la documentation !

.. toctree::
   :maxdepth: 2
   :caption: Table des matières:

   installation
   guide_utilisateur
   api

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
    (source_dir / "index.rst").write_text(index_content)
    print("✅ index.rst créé")
    
    # Créer un conf.py minimal
    conf_content = """# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Analyse Photométrique Feux Navigation'
copyright = '2024'
author = 'Votre Nom'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
language = 'fr'
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
"""
    
    (source_dir / "conf.py").write_text(conf_content)
    print("✅ conf.py créé")
    
    # Créer des fichiers RST de base
    installation_content = """Installation
============

Prérequis
---------

* Python 3.10+
* pip

Installation
------------

::

   pip install -r requirements.txt
"""
    
    (source_dir / "installation.rst").write_text(installation_content)
    print("✅ installation.rst créé")
    
    guide_content = """Guide utilisateur
=================

À compléter...
"""
    
    (source_dir / "guide_utilisateur.rst").write_text(guide_content)
    print("✅ guide_utilisateur.rst créé")
    
    api_content = """Documentation API
=================

Module file_orga
----------------

.. automodule:: file_orga
   :members:
   :undoc-members:

Module zone
-----------

.. automodule:: zone
   :members:
   :undoc-members:

Module tab_photo
----------------

.. automodule:: tab_photo
   :members:
   :undoc-members:

Module tab_colo
---------------

.. automodule:: tab_colo
   :members:
   :undoc-members:
"""
    
    (source_dir / "api.rst").write_text(api_content)
    print("✅ api.rst créé")
    
    # Créer un README dans docs
    readme_content = """# Documentation

## Générer la documentation

```bash
cd docs
make html
```

La documentation sera disponible dans `build/html/index.html`.

## Autres formats

```bash
make latexpdf  # PDF
make epub      # EPUB
make man       # Page de manuel
```

## Nettoyer

```bash
make clean
```
"""
    
    (docs_dir / "README.md").write_text(readme_content)
    print("✅ README.md créé")
    
    print("\n✨ Structure Sphinx créée avec succès !")
    print("\n📝 Prochaines étapes :")
    print("1. Installer Sphinx: pip install sphinx sphinx-rtd-theme")
    print("2. Aller dans docs/: cd docs")
    print("3. Générer la doc: make html")
    print("4. Ouvrir: build/html/index.html")


if __name__ == "__main__":
    create_sphinx_structure()
