''' 
powerup
======

This class denotes the following power-ups: 
- shield ░  
- Extra Time +   
- speed-boost A 
- extra life + 
- snake $

It inherits from obstacle.

Additional Data Members
-----------------------

- type

Denotes the type of the powerup

Additional/Re-written Member Functions
--------------------------------------

- Constructor

The obstacle is initialised as a powerup of whatever type you want it to be

- collect

Collect the powerup and make the powerup active

'''


from obstacle import obstacle
import global_stuff


class powerup(obstacle):

    def __init__(self, xpos, ypos, ty):
        '''
        The obstacle is initialised as a powerup of whatever type you want it to be
        '''
        self._type = ty
        if(ty == 'ShieldPU'):
            super().__init__(xpos, ypos, 1, 1, '░', 'ShieldPU')
        elif(ty == 'ExtraTime'):
            super().__init__(xpos, ypos, 1, 1, '+', 'ExtraTime')
        elif(ty == 'SpeedBoost'):
            super().__init__(xpos, ypos, 1, 1, 'A', 'SpeedBoost')
        elif(ty == 'ExtraLife'):
            super().__init__(xpos, ypos, 1, 1, '+', 'ExtraLife')
        elif(ty == 'Snek'):
            super().__init__(xpos, ypos, 1, 1, '$', 'Snek')

    def collect(self, board, h):
        '''
        Collect the powerup and make the powerup active
        '''
        if(global_stuff.debug == 1):
            print(self._type)
        super().destroy_self(board)  # destroy the powerup on the board
        if(self._type == 'ExtraTime'):
            global_stuff.REMAINING_NO += global_stuff.screen_length * \
                global_stuff.TO_SHIFT_SCREEN_TIME/2
        elif(self._type == 'SpeedBoost'):
            global_stuff.speeded_power_up_counter = global_stuff.MAX_SPEED_ACTIVE
            if(global_stuff.speeded == 0):
                global_stuff.TO_SHIFT_SCREEN /= 2
                global_stuff.speeded = 1
                global_stuff.speeded_active_timer = global_stuff.MAX_SPEED_ACTIVE
        elif(self._type == 'ExtraLife'):
            h.gain_life()
        elif(self._type == 'Snek'):
            global_stuff.snek = 1
            global_stuff.snake_collected = 1
