''' 
coins
====

This class denotes money!! :)
It looks like this: 0 in yellow

It inherits from obstacle.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

It is initialised as an obstacle with 0 as its shape. (well, a coin is never an obstacle right?)

- collect

This is supposed to be called when the coin is collected
Sadly, noone called it...

'''

from obstacle import obstacle
import global_stuff


class coins(obstacle):

    def __init__(self, xpos, ypos):
        '''
        initialise the coins as an obstacle
        '''
        super().__init__(xpos, ypos, 1, 1, ['0'], 'Coin')

    def collect(self, board):
        '''
        collect the coins
        '''
        super().destroy_self(board)
        global_stuff.coins_collected += 1
        global_stuff.score += 10
