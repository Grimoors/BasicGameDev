import sys
import select
import tty
import termios

import subprocess as sp

class NBInput:
    '''
    class to deal with non-blocking input
    '''

    def __init__(self):
        '''
        Initializes the object to be used for non-blocking input.
         - Saves original state at time of function call
         - Conversion to new mode has to be manual
        '''
        self.old_settings = termios.tcgetattr(sys.stdin)

    def nbTerm(self):
        '''
        Sets up the terminal for non-blocking input
        '''
        tty.setcbreak(sys.stdin.fileno())

    def orTerm(self):
        '''
        Sets terminal back to original state
        '''
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def kbHit(self):
        '''
        returns True if keypress has occured
        '''
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def getCh(self):
        '''
        returns input character
        '''
        return sys.stdin.read(1)

    def flush(self):
        '''
        clears input buffer
        '''
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

if __name__ == "__main__":
    keys=NBInput()
    keys.nbTerm() #enable non-blocking input
    keys.flush()
    k=keys.getCh()
    print(k)
    input=""
    while input!='q':
        if keys.kbHit(): # poll for input
            input = keys.getCh()
            print(input)
        print('.',end="")
    keys.orTerm()
