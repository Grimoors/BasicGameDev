from asyncio.windows_events import NULL
from multiprocessing.connection import wait
import sys
from time import time
from tracemalloc import start


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

    '''Draw Classes'''
    from src.draw import screen

    #Clear the Screen : 
    scrnCntrl.clrscr() 

    print("Please Set the terminal window screen to 1280x720\n\
The reason for this is that the Drawspace for the game is 200x60.\n\
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
The reason for this is that the Drawspace for the game is 200x60.\n\
This should fit into your screen and not look too bad. Hopefully.\n\n\
Press Y on your keyboard when ready.")
    
    #until GameLoop - Dev Code, Will be commented out or refactored.
    

    state_staack = State_Stack("start")

#Game Loop
    inGameLoop=True
    while( inGameLoop ):
        inputvar = NULL
        #Process Input, If Present
        if( keys.kbHit() ):
            inputvar = keys.getCh()
            
        #Process State Stack
        forward_state_stack(timestep, inputvar)

        #Render Present State Stack
            #Define The GameBoard.
                # Drawing Empty "Screen"
        screen = VScreen(Global.scrnHeight, Global.scrnWidth)

        # screen.prep_to_render()
        #  Base of the State Stack - Welcome Screen.
            #  Then Render the Game Screen on top
            #  Then depending on the inputs the state stack changes.
        for state in state_stack:
            screen.renderState(state)
            
        
        #Display Final Rendering
        display(screen)


else:
    print("This file \'main.py \' can only be run as a standalone")
