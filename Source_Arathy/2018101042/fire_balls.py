'''
fire
====

This class denotes the firey nature of the snek version of hero
Fire is an obstacle with the ability to move only foreward by a few steps

It inherits from obstacle class.

Additional Data Members
-----------------------

- exist

This variable is 1 if the ball has already been deployed by the snek and is currently on the screen

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Fixes the shape of the ball
Style: reverse (█▓▒░·   )  
Makes its existence 0

- check_if_exists

Returns 1 if the ball is already deployed, that is the ball is currenly on the screen

- check_collision

Manages the collision of the ball with the coins and obstacles, and the hero

- move_left

Move the ball left after destroying everything in its path

- deploy(self, x, y):

Deploy the ball
'''

import global_stuff
from obstacle import obstacle


class fire(obstacle):

    def __init__(self):
        '''
        Fixes the shape of the ball
        Makes its existence 0
        '''
        super().__init__(0, 0, 1, 5, [['█', '▓', '▒', '░', '·']], 'Fire')
        self.__exist = 0

    def check_if_exists(self):
        '''
        Returns 1 if the ball is already deployed, that is the ball is currenly on the screen
        '''
        return self.__exist

    def erase_ball(self):
        '''
        Erases the ball out of existance
        '''
        self.__exist = 0

    def check_collision(self, board):
        '''
        Manages the collision of the ball with the coins and obstacles, and the hero
        '''
        if(self.check_if_exists() == 1):
            try:
                for i in range(-5, 1):
                    # whatever obstacle it touches would be destroyed (there would be only coins :/) no need to give coins or shiz
                    c = board.destroy_object(self._x, self._y+i)
                    if(c == "Coin"):
                        global_stuff.coins_collected += 1
                        global_stuff.score += 10
            except Exception as e:
                if(global_stuff.debug):
                    print(e)
                pass

    def move_right(self, board, posi):
        '''
        Move the ball right after destroying everything in its path
        '''
        if(self.check_if_exists() == 1):
            try:
                self.check_collision(board)
            except:
                pass
            self._y += 5
            if(self._y >= posi+20):
                self.__exist = 0
            try:
                self.check_collision(board)
            except:
                pass

    def deploy(self, x, y):
        '''
        Deploy the ball
        '''
        self._x = x
        self._y = y
        self.__exist = 1
        self.print_direct()
