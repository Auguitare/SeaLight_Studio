Analyse Photométrique des Feux de Navigation
=============================================

.. image:: _static/logo.png
   :width: 200px
   :align: center
   :alt: Logo

|

Bienvenue dans la documentation de l'application d'analyse photométrique
et colorimétrique des feux de navigation maritimes.

Cette application permet d'analyser la conformité des feux de navigation
selon les normes internationales COLREG (Convention on the International
Regulations for Preventing Collisions at Sea).

.. toctree::
   :maxdepth: 2
   :caption: Documentation:

   installation
   guide_utilisateur
   api
   exemples
   developpement

Introduction
------------

Les feux de navigation sont essentiels pour la sécurité maritime. Ils doivent
respecter des normes strictes en termes d'intensité lumineuse et de couleur.

Cette application vous permet de :

* 📊 Analyser l'intensité lumineuse en fonction de l'angle horizontal
* 🎨 Vérifier la conformité colorimétrique sur le diagramme CIE
* 📈 Calculer le facteur d'intensité (uniformité du feu)
* 💾 Exporter les résultats et graphiques

Types de feux analysés
-----------------------

.. list-table::
   :widths: 20 20 30 30
   :header-rows: 1

   * - Type
     - Couleur
     - Position
     - Secteur angulaire
   * - Hune
     - Blanc
     - Sommet du mât
     - 360°
   * - Poupe
     - Blanc
     - Arrière
     - 135° (67.5° de chaque côté)
   * - Bâbord
     - Rouge
     - Gauche
     - 112.5° (de l'avant vers bâbord)
   * - Tribord
     - Vert
     - Droite
     - 112.5° (de l'avant vers tribord)

Portées lumineuses
-------------------

L'application supporte 6 portées selon les normes :

.. code-block:: text

   Portée 1 : 1.1 cd   (≈ 1 mille nautique)
   Portée 2 : 5.4 cd   (≈ 2 milles nautiques)
   Portée 3 : 15 cd    (≈ 3 milles nautiques)
   Portée 4 : 33 cd    (≈ 4 milles nautiques)
   Portée 5 : 65 cd    (≈ 5 milles nautiques)
   Portée 6 : 118 cd   (≈ 6 milles nautiques)

.. note::
   Les valeurs d'intensité sont réduites de 50% pour les feux inclinés.

Démarrage rapide
----------------

1. Installation des dépendances::

      pip install -r requirements.txt

2. Lancement de l'application::

      python main.py

3. Sélectionner un fichier de données (format .csv ou .txt)

4. Choisir le type de feu et la portée

5. Cliquer sur "Tracer le graphique"

.. tip::
   Utilisez la touche **Entrée** pour tracer rapidement le graphique
   après avoir sélectionné un fichier.

Format des fichiers de données
-------------------------------

Les fichiers doivent contenir les colonnes suivantes :

* ``Angle °`` : Angle horizontal en degrés
* ``cd`` : Intensité lumineuse en candelas
* ``lux`` : Éclairement (optionnel)
* ``X`` : Coordonnée chromatique X (CIE 1931)
* ``Y`` : Coordonnée chromatique Y (CIE 1931)

Exemple de format CSV::

   Angle;cd;lux;X;Y
   -180;0.5;2.3;0.312;0.329
   -179;0.6;2.4;0.314;0.331
   ...

Captures d'écran
----------------

Interface Photométrie
~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/screenshots/photometrie.png
   :width: 700px
   :align: center
   :alt: Interface photométrie

*Analyse de l'intensité lumineuse avec zones de conformité*

Interface Colorimétrie
~~~~~~~~~~~~~~~~~~~~~~

.. image:: _static/screenshots/colorimetrie.png
   :width: 700px
   :align: center
   :alt: Interface colorimétrie

*Diagramme chromatique CIE avec zones réglementaires*

Support et contribution
-----------------------

.. seealso::
   Pour contribuer au projet, consultez la section :doc:`developpement`.

Indices et tables
=================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Licence
-------

Copyright © 2024 - Tous droits réservés
