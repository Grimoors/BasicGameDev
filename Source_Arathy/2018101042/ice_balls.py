'''
ball
====

This class denotes the Bullet of the dragon enemy
Ice ball is an obstacle with the ability to move only backward (the BOSS is backward in both thinking and working)

It inherits from obstacle class.

Additional Data Members
-----------------------

- exist

This variable is 1 if the ball has already been deployed by the enemy and is currently on the screen

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Fixes the shape of the ball
Style: █▓▒░·     
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


class ball(obstacle):

    def __init__(self):
        '''
        Fixes the shape of the ball
        Makes its existence 0
        '''
        super().__init__(0, 0, 1, 5, [['·', '░', '▒', '▓', '█']], 'Ice Ball')
        self.__exist = 0

    def check_if_exists(self):
        '''
        Returns 1 if the ball is already deployed, that is the ball is currenly on the screen
        '''
        return self.__exist

    def check_collision(self, board, h):  # RECHECK
        '''
        Manages the collision of the ball with the coins and obstacles, and the hero
        '''
        if(self.check_if_exists() == 1):
            try:
                for i in range(0, 5):
                    # whatever obstacle it touches would be destroyed (there would be only coins :/) no need to give coins or shiz
                    board.destroy_object(self._x, self._y+i)
                    # what if it touches the hero
                    (hh, hw) = h.get_dim()
                    (hx, hy) = h.get_coord()
                    for k in range(hh):
                        for l in range(hw):
                            if((hx+k, hy-l) == (self._x, self._y+i)):
                                # you lose two lives if that ball touches you; so be warned! (if you are not shielded)
                                h.lose_life(2)
                                self.__exist = 0
                                return
            except Exception as e:
                if(global_stuff.debug):
                    print(e)
                pass

    def move_left(self, board, h):
        '''
        Move the ball left after destroying everything in its path
        '''
        if(self.check_if_exists() == 1):
            try:
                self.check_collision(board, h)
            except:
                pass
            self._y -= 5
            if(global_stuff.ball_gravity_count == 3):
                if(self._x < global_stuff.screen_height-4):
                    self._x += 1
                global_stuff.ball_gravity_count = 0
            else:
                global_stuff.ball_gravity_count += 1
            if(self._y <= 0):
                self.__exist = 0
            try:
                self.check_collision(board, h)
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
