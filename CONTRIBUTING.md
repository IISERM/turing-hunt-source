# Contributing

1. Clone/Download the repo to your machine.
2. Uninstall any old versions of Python. Install Python **3.7** onwards. Make sure to check "Add Python to PATH" when installing
3. On linux, also install `python3-tk`
4. Run `pip install -r req.txt`
5. Install Pyinstaller
    - ```pip install -U pyinstaller```
    - Documentation [here](https://pyinstaller.readthedocs.io/en/v3.6/)
6. Make your changes
7. Test your code as `python3 main.py`
8. Open a command prompt in the same folder as your code (`Shift-RightClick, Open powershell window here`)
9. Run `pyinstaller main.spec`
10. Test `./dist/main.exe`
11. Make a commit and PR
