'''
NBInput Windows
===============
This Class is an Ad-hoc port of input_Linux.py for Windows Systems.
This was obtained from Stack Over Flow. Moss be damned.
'''

import msvcrt as msvcrt
import sys
from tkinter import END

class NBInput:

    def __init__(self):
        '''
        Initializes the object to be used for non-blocking input.
         - Saves original state at time of function call
         - Conversion to new mode has to be manual

             Windows there isnt much to do.
        '''
        inputChar = str()
        # self.old_settings = msvcrt.tcgetattr(sys.stdin)

    def nbTerm(self):
        '''
        Sets up the terminal for non-blocking input #Unnecessary
        '''
        pass
        # tty.setcbreak(sys.stdin.fileno())

    def orTerm(self):
        '''
        Sets terminal back to original state - Unnessary in Windows.
        '''
        # termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
        pass

    def kbHit(self):
        '''
        returns True if keypress has occured
        '''
        # return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
        return msvcrt.kbhit()

    def getCh(self):
        '''
        returns input character
        '''
        # return sys.stdin.read(1)
        return msvcrt.getch()

    def flush(self):
        '''
        clears input buffer -> https://stackoverflow.com/questions/54299405/how-to-flush-stdin-without-requiring-user-input 
        '''
        # termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        f=open(sys.stdin,"rw+")
        f.seek(0,END)
        f.close
        pass


if "__name__" == "__main__":

    if (input("Put 1 or 2") == 1):
        num = 0
        done = 0

        while (not done):
            print (num)
            num += 1

            if (msvcrt.kbhit()):
                print("You pressed :",msvcrt.getch())
                if (msvcrt.getch()=="\x1b"):
                    print("ESC read, exiting.")
                    break
    else:
        keys = NBInput()  # initialize
        keys.nbTerm()  # enable non-blocking input
        keys.flush()  # Flush everything
        k = keys.getCh()  # get the key pressed
        print(k)
        input = ''
        while input != 'q':  # GAME LOOP
            if keys.kbHit():  # poll for input
                input = keys.getCh()  # get the input and store it in the variable
                print(input)
            print('.', end='')
        keys.orTerm()  # DONE
