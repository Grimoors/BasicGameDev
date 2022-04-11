r'''
enemy
=====

This class denotes the boss enemy Viserion, the flying dragon
He is small; he is a tiny squishy squirrel-like dragon; but why did he want to take Baby Yoda?

It inherits from person class. The enemy is also a person, remember that while shooting bullets at him

Additional Data Members
-----------------------

- state

Tells which state he is in
He has three states:

State 0: Normal state 1 where he looks like this
 |\_//|   /_(
 _/(o)/  /_( 
/o_.-. \/__( 
  __/__/___( 
 ¨-¨-¨-¨-¨  

State 1: Normal state 2 where he looks like this
 |\_//|   /_(
 _/(o)/  /_( 
/__.-. \/__( 
  __/__/___( 
 ¨-¨-¨-¨-¨  

State DEAD: The dragon looks dead in this state
 |\_//|   /_(
 _/xxx/  /_( 
/__.-. \/__( 
  __/__/___( 
 ¨-¨-¨-¨-¨  

- ball

Denotes the beautiful ice balls he likes to deploy at the hero
But since he is dumb, he does not deploy it properly at the hero

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Initialises the person with the characteristics of an enemy and gives it two additional attributes: state and ball

- print_direct

Checks the state of the dragon and prints him accordingly directly onto the screen; also prints his ball (if it exists)

- follow

Make the dragon follow the hero along the x axis

- release_balls

release those balls, filled with ice if it is not already deployed

- move_balls

Moves the balls left

- check_collision

Checks if the hero is colliding with the boss 
Decrease the boss health if bullet hits the boss and increase the score by 10 per pain inflicted to the enemy
Also checks if his ball is colliding with anything
'''


from person import person
import global_stuff
from ice_balls import ball
import random


class enemy(person):

    def __init__(self):
        '''
        Initialises the person with the characteristics of an enemy and gives it two additional attributes: state and ball
        '''
        super().__init__(2, global_stuff.screen_length-5,
                         5, 13, global_stuff.enemy_style_1, 'Enemy')
        self._state = 0
        self._ball = ball()
        self._life_remaining = global_stuff.boss_total_life

    def print_direct(self):
        '''
        Checks the state of the dragon and prints him accordingly directly onto the screen; also prints his ball (if it exists)
        '''
        if(self._state == 0):
            self._style = global_stuff.enemy_style_1
        elif(self._state == 1):
            self._style = global_stuff.enemy_style_2
        elif(self._state == 'DEAD'):
            self._style = global_stuff.enemy_style_dead
        super().print_direct()
        if(self._ball.check_if_exists() == 1):
            self._ball.print_direct()

    def follow(self, h):
        '''
        Make the dragon follow the hero along the x axis
        '''
        (hx, _) = h.get_coord()
        if(global_stuff.debug == 1):
            print('Following ', hx, self._x, global_stuff.screen_height-5-3)
        if(hx > self._x):
            if(self._x <= global_stuff.screen_height-9):
                super().move('down')
        elif(hx < self._x):
            super().move('up')

    def release_balls(self):
        '''
        release those balls, filled with ice if it is not already deployed
        '''
        if(self._ball.check_if_exists() == 0):
            p = random.randint(0, 4)
            self._ball.deploy(self._x+p, self._y)

    def move_balls(self, board, hero):
        '''
        Moves the balls left
        '''
        self._ball.move_left(board, hero)

    def check_collision(self, board, h):
        '''
        Checks if the hero is colliding with the boss 
        Decrease the boss health if bullet hits the boss and increase the score by 10 per pain inflicted to the enemy
        '''
        # Hero
        (hx, hy) = h.get_coord()
        (hh, hw) = h.get_dim()
        for i in range(self._h):
            for j in range(self._w):
                for k in range(hh):
                    for l in range(hw):
                        if((self._x+i, self._y-j) == (hx+k, hy-l)):
                            global_stuff.touch_boss = 1  # game is over so don't care about anything else
                            return
        # Bullet
        bullet_accounted = 0
        for i in range(self._h):
            if(bullet_accounted == 1):
                break
            for j in range(self._w):
                if(board.get_type(self._x+i, self._y-j) == 'Bullet'):
                    self._life_remaining -= 1
                    bullet_accounted = 1
                    break
        # otherwise check if the ball is colliding with anything
        self._ball.check_collision(board, h)

    def get_lives_remaining(self):
        '''
        A getter function to return the lives remaining of the boss
        '''
        return self._life_remaining
