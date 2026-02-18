# PyInstaller parameter

## Working on windows
```Python
python -OO -m PyInstaller src/main.py  --optimize 2 --clean --onefile --noconsole --name SeaLight_Studio --icon icon/icon.ico --add-data="icon/icon.ico;icon"
```

## working on linux
```Python
python3 -OO -m PyInstaller src/main.py --strip --optimize 2 --clean -F --noconsole --hidden-import='PIL._tkinter_finder' --name SeaLight_Studio --icon icon/icon.ico --add-data="icon/icon.ico:icon"
```