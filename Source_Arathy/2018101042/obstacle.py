'''
obstacle
========

This class denotes every object on the screen that has been rasterized on the board
It has no extra features.

It inherits from object.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

It just calls the constructor of the parent class object. 

'''

from obj import obj


class obstacle(obj):

    def __init__(self, xpos, ypos, length, width, shape, style):
        '''
        Initialize an object as an obstacle (no extra features)
        '''
        super().__init__(xpos, ypos, length, width, shape, style)
