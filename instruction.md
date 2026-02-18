# PyInstaller parameter

## Working on windows
```Python
python -OO -m PyInstaller src/main.py 
--optimize 2
--clean
--onefile
--noconsole
--name SeaLight_Studio
--icon icon.ico
--add-data icon.ico:image/.
```

## working on linux
```Python
python3 -OO -m PyInstaller src/main.py --strip --optimize 2 --clean -F --hidden-import='PIL._tkinter_finder' -n SeaLight_Studio --icon icon/icon.ico --add-data="icon/icon.ico:."
```