'''
full_board
==========

This class denotes the entire board of the game that is pre-generated.
Also known as the canvas of the game
It has a height of only screen_height-5 as 2 of the rows are taken for the top bar and 3 for the bottom bar

Playable area: 
-------------
height: 2, screen_height-3
width: screen_length * total_no_screens

Additional Data Members:
-----------------------

- rows

Denotes the number of rows (horizontal things)

- columns

Denotes the number of columns (vertical things)

- board

Denotes the canvas were we would draw everything

Member Functions:
-----------------

- Constructor

Initialises the full board with the length, width and the board matrix
Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot

- getrows

A getter function for getting the number of rows in the full_board

- generate_background

generate a background of modern art up to the point where the enemy comes. Once the enemy comes, then the background is black and dismal

- check_if_permissible

returns 0 if the given coordinates of (X,Y) is not permissible
That is, there is something else already at that location

- put_coins_block

Puts a coin block (of random height and width) at a random position on the given screen_no
The counting of the screen_no starts from 1

- put_beam_block

Puts a beam block (of the given type) at a random position on the given screen_no
The counting of the screen_no starts from 1
Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it
100 attempts are made before giving up(since the game must go on)

- put_powerup

Puts a powerup (of the given type) at a random position on the given screen_no
The counting of the screen_no starts from 1
Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it
100 attempts are made before giving up(since the game must go on)

- randomly_add_coins_everywhere

Generate coins randomly on the board based on the following metric
Screen 1    : 2 blocks (need not be distinct)
Screen 2 - 9: 4 blocks (need not be distinct)

- randomly_add_beams

Generate all kinds of beams randomly on the board based on the following metric
Screen 0.5 - 5    : 2 blocks (placing if permissible) per beam type

- randomly_add_powerups

Generate all types of powerups randomly on the board based on the following metric
Extra Life :     1-10:         1 (placing if permissible)
Speed Up   :     1- 5:         1 (placing if permissible)
Shield     :     1- 5:         2 (placing if permissible)
Snek       :     1- 2:         1 (placing if permissible)

- add_magnet

Generate a magnet and place it on the screen randomly
Screen number 3

- def prepare_board

Prepares the board :)

'''

import global_stuff
import numpy as np
from coins import coins
import random
from beam import beam
from powerUp import powerup
from magnet import magnet
from board import board


class full_board(board):

    def __init__(self, rows, columns):
        '''
        Initialises the full board with the length, width and the board matrix
        Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
        Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot
        '''
        super().__init__(rows-5, columns*global_stuff.total_no_screens)

    def generate_background(self):
        '''
        generate a background of modern art up to the point where the enemy comes. Once the enemy comes, then the background is black and dismal
        '''
        for i in range(self._rows):
            for j in range(self._columns):
                prob = random.random()
                if(prob > 0.99):
                    self.put_to_board(i, j, ' ', 'Bg2')
                else:
                    self.put_to_board(i, j, ' ', 'Bg1')

    def check_if_permissible(self, X, Y):
        ''' 
        returns 0 if the given coordinates of (X,Y) is not permissible
        That is, there is something else already at that location
        '''
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if self.get_type(X+i, Y+j) != 'Normal':
                        return 0
                except:
                    continue
        return 1

    def put_coins_block(self, screen_no):
        '''
        Puts a coin block (of random height and width) at a random position on the given screen_no
        The counting of the screen_no starts from 1
        '''
        h = random.randint(2, 7)
        w = random.randint(10, 30)
        xpos = random.randint(3, self._rows-2)  # man anything is enough
        ypos = random.randint(int((screen_no-1)*global_stuff.screen_length),
                              int(screen_no*global_stuff.screen_length))  # 1st screen
        if(global_stuff.debug == 1):
            print(ypos)
        for i in range(h):
            for j in range(w):
                c = coins(xpos+i, ypos+j)
                try:
                    c.write_self_on_board(self)
                except:
                    continue

    def put_beam_block(self, ty, screen_no):
        '''
        Puts a beam block (of the given type) at a random position on the given screen_no
        The counting of the screen_no starts from 1
        Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it
        100 attempts are made before giving up(since the game must go on)
        '''
        attempt = 0
        while (attempt <= 100):
            try:
                if(ty == 'h'):
                    xpos = random.randint(2, self._rows-4)
                elif(ty in ['d1', 'd2', 'v']):
                    xpos = random.randint(
                        2, self._rows-int(global_stuff.length_of_beam/2)+2*global_stuff.safe_region-3)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))
                beami = beam(xpos, ypos, ty)
                ifp = 1
                for I in range(beami._h):
                    for J in range(beami._w):
                        if(self.check_if_permissible(xpos+I, ypos+J) == 0):
                            ifp = 0
                            break
                    if(ifp == 0):
                        break
                if(ifp == 1):
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                    beami.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug == 1):
                    print('Error')
                attempt += 1

    def put_powerup(self, ty, screen_no):
        '''
        Puts a powerup (of the given type) at a random position on the given screen_no
        The counting of the screen_no starts from 1
        Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it
        100 attempts are made before giving up(since the game must go on)
        '''
        attempt = 0
        while (attempt <= 100):
            try:
                xpos = random.randint(5, self._rows-5)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))
                pu = powerup(xpos, ypos, ty)
                if(self.check_if_permissible(xpos, ypos) != 0):
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                    pu.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug == 1):
                    print('Error')
                attempt += 1

    def randomly_add_coins_everywhere(self):
        '''
        Generate coins randomly on the board based on the following metric
        Screen 1    : 2 blocks (need not be distinct)
        Screen 2 - 9: 4 blocks (need not be distinct)
        '''
        if(global_stuff.debug == 1):
            print('Generating coins...')
        # SCREEN 1
        for _ in range(2):
            # only the y position i.e. the horizontal position of the coin set keeps changing so...
            self.put_coins_block(1)
        # SCREEN 2 - 9
        for screen in range(2, global_stuff.total_no_screens):  # screen loop
            for _ in range(4):  # count loop
                # only the y position i.e. the horizontal position of the coin set keeps changing so...
                self.put_coins_block(screen)

    def randomly_add_beams(self):
        '''
        Generate all kinds of beams randomly on the board based on the following metric
        Screen 0.5 - 5    : 2 blocks (placing if permissible) per beam type
        '''
        for typ in ['h', 'v', 'd1', 'd2']:
            if(global_stuff.debug == 1):
                print('Generating '+typ+' beams....')
            for i in range(1, 5):
                for _ in range(2):
                    self.put_beam_block(typ, i+0.5)

    def randomly_add_powerups(self):
        '''
        Generate all types of powerups randomly on the board based on the following metric
        Extra Life :     1-10:         1 (placing if permissible)
        Speed Up   :     1- 5:         1 (placing if permissible)
        Extra Time :     1-10:         1 (placing if permissible) 
        Snek       :     1- 2:         1 (placing if permissible)
        '''
        if(global_stuff.debug == 1):
            print('Generating extra life powerups...')
        for screen in range(1, global_stuff.total_no_screens):
            self.put_powerup('ExtraLife', screen)
        if(global_stuff.debug == 1):
            print('Generating Speed Up powerups...')
        for screen in range(1, 5):
            self.put_powerup('SpeedBoost', screen)
        if(global_stuff.debug == 1):
            print('Generating Extra Time powerups...')
        for screen in range(1, global_stuff.total_no_screens):
            self.put_powerup('ExtraTime', screen)
        if(global_stuff.debug == 1):
            print('Generating Snake powerups...')
        for screen in range(1, 2):
            self.put_powerup('Snek', screen+0.5)

    def add_magnet(self):
        '''
        Generate a magnet and place it on the screen randomly
        Screen number 3
        '''
        if(global_stuff.debug == 1):
            print('Generating magnet...')
        if(global_stuff.powerUpTesting == 1):
            kdd = 0
        else:
            kdd = 3
        while(True):
            xpos = random.randint(3, 4)
            ypos = random.randint(
                (kdd-1)*global_stuff.screen_length, kdd*global_stuff.screen_length)
            m = magnet(xpos, ypos)
            try:
                ok = 1
                for i in range(m._h):
                    for j in range(m._w):
                        if(self.check_if_permissible(xpos+i, ypos+j) == 0):
                            ok = 0
                            if(global_stuff.debug == 1):
                                print('Not ok at ', xpos+i, ypos+j)
                            break
                    if(ok == 0):
                        break
                if(ok == 1):
                    m.write_self_on_board(self)
                    global_stuff.magnet_y_pos_fullboard = ypos
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                    return
                else:
                    if(global_stuff.debug == 1):
                        print('occupied', xpos, ypos)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def prepare_board(self):
        '''
        Prepares the board :)
        '''
        self.generate_background()
        self.randomly_add_coins_everywhere()
        self.randomly_add_beams()
        self.randomly_add_powerups()
        self.add_magnet()
