# from asyncio.windows_events import NULL
from multiprocessing.connection import wait
import sys
import time
from tracemalloc import start
# from turtle import Screen
from src.state.screen import *
from src.state.defstate import states


def ProcessState(currState,ScreenIn):
    
    nextState = currState
    ScreenOut = ScreenIn
    print("Current State:", nextState)
    if (nextState.get("state") == "start"):
        ScreenOut = Vscreen (60,200)
        ScreenOut.updateScreenGrid(StaticDraws.DefaultBorder(ScreenOut,5,3))
        ScreenOut.updateScreenGrid( StaticDraws.TitleDisplay( screenIn = ScreenOut) )
        ScreenOut.updateScreenGrid(StaticDraws.PlayBackground(screenIn= ScreenOut))
    
    if (nextState.get("state") == "game" ):
        pass

    if (nextState.get("state") == "titlemenu" ):
        ScreenOut =Vscreen(60,200)
        ScreenOut.updateScreenGrid(StaticDraws.DefaultBorder(ScreenOut,5,3))
        ScreenOut.updateScreenGrid( StaticDraws.TitleDisplay( screenIn = ScreenOut) )
        ScreenOut.updateScreenGrid(StaticDraws.PlayBackground(screenIn= ScreenOut))

    if(nextState.get("state") == "gameover"):
        pass

    if(nextState.get("state") == "quit"):
        pass

    if(nextState.get("state") == "pausemenu"):
        pass

    if(nextState.get("state") == "levelselect"):
        pass

    return nextState, ScreenOut
    


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
    # from src.draw import screen

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
            time.sleep(1)
            break
        else:
            print("Please Set the terminal window screen to 1280x720\n\
The reason for this is that the Drawspace for the game is 200x60.\n\
This should fit into your screen and not look too bad. Hopefully.\n\n\
Press Y on your keyboard when ready.")
    
    #until GameLoop - Dev Code, Will be commented out or refactored.
    

    gSstack = states()
    gScreen = Vscreen (60,200)

#Game Loop
    inGameLoop=True
    while( inGameLoop ):
        inputvar = ""
        #Process Input, If Present
        if( keys.kbHit() ):
            inputvar = keys.getCh()
            # print(inputvar)
            keys.flush()
        
        #Get Current State
        currState = gSstack.peek()
        # print(currState)
        # print(currState["state"])
        # print(currState["screen"])
        # print(currState["timestep"])
        # print(currState["input"])
        # print(currState["onPop"])
        # print(currState["toPop"])

        #Check if State is to be popped
        if(currState["toPop"] == inputvar):
            gSstack.pop()
            # print("Popped")
            # print(gSstack.peek())
        
        #Check if a State is to be pushed
        if(currState["onPop"] == inputvar):
            # print("Pushing")
            # print(currState["onPop"])
            # print(currState["toPop"])
            p = gSstack.StateList.indexOf(currState["onPop"])
            gSstack.push(  gSstack.StateJsons[ p ] )
            # print(gSstack.peek())

        #Check if Quit State
        if(currState["state"] == "quit"):
            inGameLoop = False
            print("Quitting") 
            # print(gSstack.peek())
            sys.exit(0)

        #Check if State is to be Flushed
        if(currState["state"] == "flush"):
            gSstack.flush()
            gSstack.push( gSstack.StateJsons[0] )
            # print("Flushed")
            # print(gSstack.peek())
        
        #Check if State is to be Reset
        if(currState["state"] == "reset"):
            gSstack.pop()
            gSstack.push(currState["onPop"])
            # print("Reset")
            # print(gSstack.peek())

        #Check if State is to be Processed before next cycle
        currState = gSstack.peek()
        
        currState,gScreen = ProcessState(currState,gScreen)
        

        gScreen.displayScreen()

        

        

        
        
        #Process State Stack
        # forward_state_stack(timestep, inputvar)

        #Render Present State Stack
            #Define The GameBoard.
                # Drawing Empty "Screen"
        # screen = VScreen(Global.scrnHeight, Global.scrnWidth)

        # screen.prep_to_render()
        #  Base of the State Stack - Welcome Screen.
            #  Then Render the Game Screen on top
            #  Then depending on the inputs the state stack changes.
        # for state in state_stack:
        #     screen.renderState(state)
            
        
        #Display Final Rendering
        # display(screen)


else:
    print("This file \'main.py \' can only be run as a standalone")
