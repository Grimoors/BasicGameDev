'''
hero
====

This class denotes the Mandalorian who is controlled by the player.
He is small; he is cute.
He looks different based on the powerups he is on

It inherits from person class.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Initialises the person with the characteristics of a hero
Style:
[▄
||

- print_direct

Checks how high the hero is currently (that is, which all power-ups are active atm)
Then prints the hero directly onto the screen

- collision_manager

Manages the collision of the hero with the beams, coins, magnet and powerups on the board

- magnet_attraction

Manages the attraction of the hero towards the magnet if the magnet is on the screen

'''


from person import person
import global_stuff
from powerUp import powerup
import time


class hero(person):

    def __init__(self):
        '''
        Initialises the person with the characteristics of a hero
        '''
        super().__init__(global_stuff.screen_height - 5,
                         0, 2, 2, global_stuff.hero, 'Hero')
        self._life_remaining = global_stuff.total_life
        self._is_shielded = 0

    def is_shield(self):
        '''
        returns 1 if the hero is shielded
        '''
        return self._is_shielded

    def print_direct(self):
        '''
        Checks how high the hero is currently (that is, which all power-ups are active atm)
        Then prints the hero directly onto the screen
        '''
        if(global_stuff.speeded == 1):
            self.change_type('SpeededHero')
            super().print_direct()
        elif(self._is_shielded == 1):
            self.change_type('ShieldedHero')
            super().print_direct()
        else:
            self.change_type('Hero')
            super().print_direct()

    def lose_life(self, k):
        '''
        reduce the life of the hero by k if he is not in snake or shield mode
        '''
        if(self._is_shielded == 1):
            self.unshield_self()
        elif(global_stuff.snek == 1):
            global_stuff.snek = 0
            global_stuff.trigger = 1
        else:
            self._life_remaining -= k
        if(self._life_remaining < 0):
            self._life_remaining = 0

    def get_lives_remaining(self):
        '''
        gets the number of lives remaining
        '''
        return self._life_remaining

    def gain_life(self):
        '''
        Adds a life to the hero
        '''
        self._life_remaining += 1
        if(self._life_remaining >= global_stuff.total_life):
            self._life_remaining = global_stuff.total_life

    def collision_manager(self, board):
        '''
        Manages the collision of the hero with the beams, coins, magnet and powerups on the board
        '''
        # print(self._h,self._w)
        for i in range(self._h):
            for j in range(self._w):
                what_is_destroyed = board.destroy_object(self._x+i, self._y+j)
                if(global_stuff.debug == 1):
                    if(what_is_destroyed != 'No collision'):
                        print(what_is_destroyed)
                # coins
                if(what_is_destroyed == 'Coin'):
                    global_stuff.coins_collected += 1
                    global_stuff.score += 10
                # beams
                elif what_is_destroyed in ['Hbeam', 'Vbeam', 'Dbeam1', 'Dbeam2']:
                    self.lose_life(1)
                # power-ups
                elif what_is_destroyed in ['ExtraLife', 'ShieldPU', 'SpeedBoost', 'Snek', 'ExtraLife']:
                    p = powerup(self._x+i, self._y+j, what_is_destroyed)
                    p.collect(board, self)
                # magnets
                elif(what_is_destroyed == 'Magnet'):
                    global_stuff.hit_by_a_magnet = 1

    def magnet_attraction(self, board):
        '''
        Manages the attraction of the hero towards the magnet if the magnet is on the screen
        '''
        is_magnet_on_screen = board.is_magnet_on_screen()
        if(is_magnet_on_screen != 'NOT ON SCREEN'):
            if(global_stuff.debug == 1):
                print('Moving the guy close to ', is_magnet_on_screen)
            if(is_magnet_on_screen+4-1 > self._y):
                self.move('right')
            elif(is_magnet_on_screen+4-1 < self._y):
                self.move('left')
                self.move('left')
            self.collision_manager(board)

    def shield_self(self):
        '''
        Develop a shield around the hero
        '''
        self._style = [['█', '['], ['║', '║']]
        self.change_type('ShieldedHero')
        self._is_shielded = 1
        global_stuff.shield_active_timer = global_stuff.MAX_SHIELD_ACTIVE

    def unshield_self(self):
        '''
        remove the shield around the hero
        '''
        self._style = global_stuff.hero
        self.change_type('Hero')
        self._is_shielded = 0
        global_stuff.shield_active_timer = 0
        global_stuff.shield_countdown = global_stuff.MAX_SHIELD_COOLDOWN

    def check_if_dead(self):
        '''
        Checks if the hero is dead or not:
            How did you die?
            How did the game end?
            Answers all these questions
        '''
        if(global_stuff.hit_by_a_magnet == 1):
            return 'Death by Magnet'
        elif (self._life_remaining <= 0):
            return 'No Lives Remaining'
        elif(global_stuff.time_left <= 0):
            return 'Time out'
        elif(global_stuff.touch_boss == 1):
            return 'Touched Boss'
        elif(global_stuff.boss_dead == 1):
            return 'Boss Dead'
        else:
            return 'Alive'

    def move(self, direction):
        k = super().move(direction)
        if(k == 1):  # if he is moving up, then initialise the time
            global_stuff.last_move_up_time = time.time()

    def do_gravity(self, v):
        '''
        Perform the gravity part
        '''
        v += 1
        self._x += v
