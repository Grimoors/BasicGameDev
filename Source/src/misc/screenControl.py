if "__name__" != "__main__":
    import os

    def clrscr():
        os.system('cls' if os.name=='nt' else 'clear')
else:
    print("This module \'./src/misc/screenControl.py\' cannot run as standalone ")