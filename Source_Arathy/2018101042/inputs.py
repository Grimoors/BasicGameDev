'''
NBInput
=======

This class deals with non-blocking input.
This was obtained from a stack overflow website (moss have mercy)
'''

import sys
import select
import tty
import termios


class NBInput:

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

# USE CASE


if __name__ == '__main__':
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
