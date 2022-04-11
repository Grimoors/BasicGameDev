'''
gameboard
=========

This class denotes the game board that is currently being displayed on the screen.

Data Members:
-------------

- rows

Denotes the number of rows (horizontal things) : 50

- columns

Denotes the number of columns (vertical things) : 200

- board

Denotes the canvas were we would draw everything

Member Functions:
-----------------

- Constructor

Initialises the full board with the length, width and the board matrix
Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot
Also sets up the top bar(the first two rows), bottom bar(the last three rows) and prints all the accessories of the game board

- gamename_display

Displays the game name on the top left corner of the game board on the top bar

- score_update

Displays the score on the top right corner of the game board on the top bar 
The score is left padded with 0s

- life_display

Displays the life remaining of the hero on the top left corner of the bottom bar
The life remaining is drawn using black blocks like a progress bar

- time_display

Displays the time remaining for the hero to save Baby Yoda on left side of the bottom bar
The time remaining is drawn using black blocks like a progress bar

- game_progress_display

Displays the progress, i.e. how close the hero is to see the boss, on left side of the bottom bar
The progress is drawn using black blocks like a progress bar

- bullets_display

Displays the number of bullets that are ready to be deployed but not deployed yet on the right side of the bottom bar


- print_enemy_life

Displays the life remaining of the enemy on the top bar when the enemy comes
The life remaining is drawn using black blocks like a progress bar

- prepare_board(self):

Prepares, i.e. updates the board before printing it on the screen

- print(self):

Prints the gameboard onto the screen

- write_full_on_board(self, full_board, start_in):

Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled

- shift_right(self, full_board, line_to_add):

Shift everything to right every .5 seconds

- is_magnet_on_screen(self):

Returns the y coordinate of the magnet if it is on the screen, otherwise return -1

- destroy_object(self, X, Y):  

Destroys whatever object is there at position X,Y completely and returns the object type
This function deals only with coins, beams and powerups
However since magnets cannot be destoyed, if the current position has a magnet, then it does not destroy it

'''

import numpy as np
from colored_printing import color_text
import global_stuff
from full_board import full_board
import time
from powerUp import powerup
from board import board


class gameboard(board):
    def __init__(self, rows, columns):
        '''
        Initialises the full board with the length, width and the board matrix
        Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
        Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot
        Also sets up the top bar(the first two rows), bottom bar(the last three rows) and prints all the accessories of the game board
        '''
        super().__init__(rows, columns)
        # The top bar
        for i in range(0, 2):
            for j in range(self._columns):
                self.put_to_board(i, j, ' ', 'Top Bar')
        # The game body
        for i in range(2, self._rows-3):
            for j in range(self._columns):
                self.put_to_board(i, j, ' ', 'Normal')
        # the bottom bar
        for i in range(self._rows-3, self._rows):
            for j in range(self._columns):
                self.put_to_board(i, j, ' ', 'Bottom Bar')
        self.gamename_display()

    def gamename_display(self):
        '''
        Displays the game name on the top left corner of the game board on the top bar
        '''
        gamename = 'THE MANDALORIAN: THE GAME'
        leng = len(gamename)
        startat = 2
        for i in range(leng):
            self.put_to_board(0, i+startat, gamename[i], "Top Bar")

    def score_update(self):
        '''
        Displays the score on the top right corner of the game board on the top bar 
        The score is left padded with 0s
        '''
        scorename = 'SCORE: '+str(global_stuff.score).rjust(10, '0')
        leng = len(scorename)
        startat = self._columns-2-leng
        for i in range(leng):
            self.put_to_board(0, i+startat, scorename[i], "Top Bar")

    def life_display(self, h):
        '''
        Displays the life remaining of the hero on the top left corner of the bottom bar
        The life remaining is drawn using black blocks like a progress bar
        '''
        # Print the word life
        lf = 'LIFE:     '
        leng = len(lf)
        for i in range(leng):
            self.put_to_board(self._rows-3, i, lf[i], "Bottom Bar")
        # Print the life bar
        percentage_to_fill = h.get_lives_remaining() / global_stuff.total_life
        totwid = int(self._columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.put_to_board(self._rows-3, i+leng, k[i], "Life")

    def time_display(self):
        '''
        Displays the time remaining for the hero to save Baby Yoda on left side of the bottom bar
        The time remaining is drawn using black blocks like a progress bar
        '''
        # Print the word 'TIME LEFT'
        lf = 'TIME LEFT:'
        leng = len(lf)
        for i in range(leng):
            self.put_to_board(self._rows-2, i, lf[i], "Bottom Bar")
        # Print the time bar
        percentage_to_fill = global_stuff.REMAINING_NO/global_stuff.MAXIMUM_NO
        totwid = int(self._columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.put_to_board(self._rows-2, i+leng, k[i], "Time")

    def shield_pu_display(self, h):
        '''
        Displays the shield powerup, that is, if it is active or not and so on
        '''
        # Print the word Shield
        lf = 'SHIELD:            '
        leng = len(lf)
        startat = int(global_stuff.screen_length/2)+5
        for i in range(leng):
            self.put_to_board(self._rows-2, i+startat, lf[i], "Bottom Bar")
        # Print the progress bar
        if(h.is_shield() == 0):
            percentage_to_fill = global_stuff.shield_countdown / \
                global_stuff.MAX_SHIELD_COOLDOWN
            typ = 'ShieldedHero'
        else:
            percentage_to_fill = global_stuff.shield_active_timer / \
                global_stuff.MAX_SHIELD_ACTIVE
            typ = 'ShieldPU'
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self._columns/2-30)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            # put the time left
            self.put_to_board(self._rows-2, i+leng + startat, k[i], typ)

    def SpeedBoost_pu_display(self):
        '''
        prints the time remaining for the speedboost
        '''
        lf = 'SPEED BOOST:       '
        leng = len(lf)
        startat = int(global_stuff.screen_length/2)+5
        for i in range(leng):
            self.put_to_board(self._rows-1, i + startat, lf[i], "Bottom Bar")
        # Print the progress bar
        if(global_stuff.speeded == 0):
            percentage_to_fill = 0
        else:
            percentage_to_fill = global_stuff.speeded_active_timer/global_stuff.MAX_SPEED_ACTIVE
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self._columns/2-30)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            # put the time left
            self.put_to_board(self._rows-1, i + leng +
                              startat, k[i], "SpeededHero")

    def game_progress_display(self):
        '''
        Displays the progress, i.e. how close the hero is to see the boss, on left side of the bottom bar
        The progress is drawn using black blocks like a progress bar
        '''
        # Print the word progress
        lf = 'PROGRESS: '
        leng = len(lf)
        for i in range(leng):
            self.put_to_board(self._rows-1, i, lf[i], "Bottom Bar")
        # Print the progress bar
        progress = global_stuff.shown_until-global_stuff.screen_length
        percentage_to_fill = progress / \
            ((global_stuff.enemy_comes_after-1)*global_stuff.screen_length)
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self._columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.put_to_board(self._rows-1, i + leng, k[i], "Progress")

    def bullets_display(self):
        '''
        Displays the number of bullets that are ready to be deployed but not deployed yet on the right side of the bottom bar
        '''
        lf = 'BULLETS LEFT:      '
        k = ''
        for _ in range(global_stuff.bullets_left):
            k += '> '
        for _ in range(global_stuff.bullets_left, global_stuff.total_bullets):
            k += '  '
        lf += k
        leng = len(lf)
        startat = int(global_stuff.screen_length/2)+5
        for i in range(leng):
            self.put_to_board(self._rows-3, i + startat, lf[i], "Bottom Bar")

    def print_enemy_life(self, enemy):
        '''
        Displays the life remaining of the enemy on the top bar when the enemy comes
        The life remaining is drawn using black blocks like a progress bar
        '''
        # Print the word enemy
        lf = 'ENEMY: '
        leng = len(lf)
        for i in range(leng):
            self.put_to_board(1, i, lf[i], 'Top Bar')
        # Print the enemy life bar
        percentage_to_fill = enemy.get_lives_remaining() / global_stuff.boss_total_life
        if(percentage_to_fill <= 0):
            global_stuff.boss_dead = 1
        totwid = int(self._columns-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.put_to_board(1, i+leng, k[i], 'Life')

    def prepare_board(self, h):
        '''
        Prepares, i.e. updates the board before printing it on the screen
        '''
        self.score_update()
        self.life_display(h)
        self.time_display()
        self.bullets_display()
        self.game_progress_display()
        self.shield_pu_display(h)
        self.SpeedBoost_pu_display()

    def print(self, h, enemy):
        '''
        Prints the gameboard onto the screen
        '''
        self.prepare_board(h)
        if(global_stuff.enemy_come == 1):
            self.print_enemy_life(enemy)
        for i in range(self._rows):
            for j in range(self._columns):
                self.printxy(i, j)
            print()

    def write_full_on_board(self, full_board, start_in):
        ''' 
        Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled
        '''
        (r, _) = full_board.getdim()
        try:
            for i in range(0, r):  # all the rows from blahblahblah
                for j in range(0, self._columns):  # all the columns from teh gameboard
                    self._board[i+2][j] = full_board.getxy(i, j+start_in)
        except Exception as e:
            print(e)

    def shift_right(self, full_board, line_to_add):
        '''
        Shift everything to right every .5 seconds
        '''
        (r, _) = full_board.getdim()
        for i in range(r):
            for j in range(self._columns-1):
                self._board[i+2][j] = self._board[i+2][j+1]
        for i in range(r):
            self._board[i+2][self._columns -
                             1] = full_board.getxy(i, line_to_add)

    def is_magnet_on_screen(self):
        '''
        Returns the y coordinate of the magnet if it is on the screen, otherwise return -1
        '''
        position = global_stuff.magnet_y_pos_fullboard - \
            global_stuff.shown_until+global_stuff.screen_length
        if(position < global_stuff.screen_length and position >= -7):
            return position
        return 'NOT ON SCREEN'

    def destroy_object(self, X, Y):
        '''
        Destroys whatever object is there at position X,Y completely and returns the object type
        This function deals only with coins, beams and powerups
        However since magnets cannot be destoyed, if the current position has a magnet, then it does not destroy it
        '''
        # No collision
        if(self.get_type(X, Y) == 'Normal'):
            return 'No collision'
        # Coin
        elif(self.get_type(X, Y) == 'Coin'):
            self.remove_from_board(X, Y)
            return 'Coin'
        # Horizontal beam
        elif(self.get_type(X, Y) == 'Hbeam'):
            try:  # for left side
                i = 0
                while (self.get_type(X, Y+i) == 'Hbeam'):
                    self.remove_from_board(X, Y+i)
                    i += 1
            except:
                pass
            try:  # for right side
                i = 1
                while (self.get_type(X, Y-i) == 'Hbeam'):
                    self.remove_from_board(X, Y-i)
                    i += 1
            except:
                pass
            return 'Hbeam'
        # Vertical beam
        elif (self.get_type(X, Y) == 'Vbeam'):
            try:  # for up or down
                i = 0
                while (self.get_type(X+i, Y) == 'Vbeam'):
                    self.remove_from_board(X+i, Y)
                    i += 1
            except:
                pass
            try:  # for the other thing
                i = 1
                while (self.get_type(X-i, Y) == 'Vbeam'):
                    self.remove_from_board(X-i, Y)
                    i += 1
            except:
                pass
            return 'Vbeam'
        # Diagonal 1 beam
        elif (self.get_type(X, Y) == 'Dbeam1'):
            try:
                i = 0
                while (self.get_type(X+i, Y+i) == 'Dbeam1'):
                    self.remove_from_board(X+i, Y+i)
                    i += 1
            except:
                pass
            try:
                i = 1
                while (self.get_type(X-i, Y-i) == 'Dbeam1'):
                    self.remove_from_board(X-i, Y-i)
                    i += 1
            except:
                pass
            return 'Dbeam1'
        # Diagonal 2 beam
        elif(self.get_type(X, Y) == 'Dbeam2'):
            try:
                i = 0
                while (self.get_type(X-i, Y+i) == 'Dbeam2'):
                    self.remove_from_board(X-i, Y+i)
                    i += 1
            except:
                pass
            try:
                i = 1
                while (self.get_type(X+i, Y-i) == 'Dbeam2'):
                    self.remove_from_board(X+i, Y-i)
                    i += 1
            except:
                pass
            return 'Dbeam2'
        # Power-ups
        elif(self.get_type(X, Y) in ['ExtraLife', 'ShieldPU', 'SpeedBoost', 'Snek', 'ExtraTime']):
            t = self.get_type(X, Y)
            self.remove_from_board(X, Y)
            return t
        # Magnet
        elif(self.get_type(X, Y) == 'Magnet'):
            return 'Magnet'
