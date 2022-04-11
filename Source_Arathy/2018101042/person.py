'''
person
======

This class denotes the charcters in the game
It is the base class for hero and enemy

It inherits from obj.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- constructor

It just calls the constructor of the parent class object. 

- move

Moves the hero according to the direction given
The direction can be given either in wasd or up down left right

'''

from obj import obj
import global_stuff


class person(obj):

    def __init__(self, x, y, h, w, style, ty):
        '''
        It just calls the constructor of the parent class object. 
        '''
        super().__init__(x, y, h, w, style, ty)

    def move(self, direction):
        '''
        Moves the hero according to the direction given
        The direction can be given either in wasd or up down left right
        Returns 0 if he moves up, otherwise returns 1
        '''
        if direction in ['w', 'up']:
            if(self._x > 2):
                self._x -= 1
        elif direction in ['s', 'down']:
            if(self._x < global_stuff.screen_height-5):
                self._x += 1
        elif direction in ['a', 'left']:
            if(self._y > 0):
                self._y -= 1
        elif direction in ['d', 'right']:
            if(self._y < global_stuff.screen_length-2):
                self._y += 1
        if direction in ['w', 'up']:
            return 0
        else:
            return 1
        if(global_stuff.debug == 1):
            print(self._x, self._y)
