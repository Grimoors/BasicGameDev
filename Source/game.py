from multiprocessing.connection import wait
import sys
from time import time


if __name__ == "__main__":
    #Imports
    
    '''ClearScreen'''
    from src.misc import screenControl as scrnCntrl
    
    '''Non Blocking Input Loop --- Platform Independent'''
    if (sys.platform == "linux"):
        from src.misc.InputLoop import input_Linux as inputs
    else:
        if( sys.platform == "windows" ):
            from src.misc.InputLoop import input_Windows as inputs

    #Clear the Screen : 
    scrnCntrl.clrscr() 

    print("Please Set the terminal window screen to 1280x720\n\
The reason for this is that the Drawspace for the game is 1120x631.\n\
This should fit into your screen and not look too bad. Hopefully.\n\n\
Press Y on your keyboard when ready.")

    #Start Input Loop
    keys = inputs.NBInput()
    keys.nbTerm()
    keys.flush()

    while(1):
        ch1 = keys.getCh()
        if(ch1 == "Y"):
            print ("Starting in 1 sec")
            wait(time(1))
            break
        else:
            print("Please Set the terminal window screen to 1280x720\n\
The reason for this is that the Drawspace for the game is 1120x631.\n\
This should fit into your screen and not look too bad. Hopefully.\n\n\
Press Y on your keyboard when ready.")

    #Start Game Loop.

    


    #Show StartScreen

    

\

else:
    print("This file \'main.py \' can only be run as a standalone")
