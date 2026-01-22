# Mantagua Graph tracer

Création d'une application simple permettant de tracer les graphes de puissance lumineuse des test optique d'un feux de navigation.

## Working in a venv
```bash
sudo apt install python3.12-venv
```
### Create venv
```bash
python3 -m venv .venv
```
### going in venv workspace
```bash
source .venv/bin/activate
```
### install libraries
```bash
pip install -r requirements.txt
```

## PyInstaller parameter

```Python
python -m PyInstaller .\lecture_fichier.py --clean -F --noconsole
```
