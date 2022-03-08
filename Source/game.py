if __name__ == "__main__":
    #Imports
    from src.misc import screenControl as scrnCntrl

    #Clear the Screen : 
    scrnCntrl.clrscr() 

    print("Please Set the terminal window screen to 1280x720\n\
The reason for this is that the Drawspace for the game is 1120x631.\n\
This should fit into your screen and not look too bad. Hopefully.\n\n\
Press Y on your keyboard when ready.")

    



else:
    print("This file \'main.py \' can only be run as a standalone")
