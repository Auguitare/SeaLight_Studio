# PyInstaller parameter

## Working on windows
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

## working on linux
```Python
python3 -OO -m PyInstaller main.py --strip --optimize 2 --clean -F --noconsole --hidden-import='PIL._tkinter_finder' -n photometrie --icon icon.ico 
```