# Mantagua Graph tracer

Création d'une application simple permettant de tracer les graphes de puissance lumineuseet de colorimétrie des test optique d'un feux de navigation.

## Create a venv
`sudo apt install python3.12-venv`
```bash
python3 -m venv .venv # Create venv
source .venv/bin/activate # going in venv workspace
pip install -r requirements.txt # install libraries
```
### MAJ venv requirements.txt
```bash
pip freeze > requirements.txt
```
### Working ina venv
```bash
source .venv/bin/activate # going in venv workspace
python3 lecture_fichier.py
```

## PyInstaller parameter

### Working on windows
```Python
python -OO -m PyInstaller main.py 
--optimize 2
--clean
--onefile
--noconsole
--name Photometrie
--icon icon.ico
--add-data icon.ico:image/.
```

### working on linux
```Python
python3 -OO -m PyInstaller main.py --strip --optimize 2 --clean -F --noconsole --hidden-import='PIL._tkinter_finder' -n photometrie --icon icon.ico 
```
