'''
NBInput
=======
This class deals with non-blocking input.
This was obtained from a Github Repo. Moss be damned. 
'''

import sys
import select
import tty
import termios
import signal


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


class AlarmException(Exception):
    """Handling alarm exception."""
    pass

def alarmHandler(signum, frame):
    """Handling timeouts."""
    raise AlarmException


def input_to(getch, timeout=0.1):
    """Taking input from user."""
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return None