'''
Has those functions related to the terminal

- clrscr

Clears the terminal screen

- next_play

Repositions the pointer to the top left corner of the screen for the next game
'''

import subprocess as sp
import global_stuff


def clrscr():
    '''
    Clears the terminal screen
    '''
    sp.call('clear', shell=True)


def next_play():
    ''' 
    Repositions the pointer to the top left corner of the screen for the next game
    '''
    print('\033[0;0H', end='')


def setup(difficulty):
    if(difficulty == 1):
        print("Hi TA!")
        global_stuff.TO_SHIFT_SCREEN_TIME = 0.5  # put difficulty levels
    elif(difficulty == 2):
        print("Good choice")
        global_stuff.TO_SHIFT_SCREEN_TIME = 0.2
    elif(difficulty == 3):
        print("Practice makes man perfect")
        global_stuff.test_enemy = 1
    global_stuff.TO_SHIFT_SCREEN = global_stuff.TO_SHIFT_SCREEN_TIME / \
        global_stuff.FRAME_TIME
    # TOTAL TIME THINGS
    global_stuff.TOTAL_TIME = global_stuff.enemy_comes_after*2 * \
        global_stuff.screen_length*global_stuff.TO_SHIFT_SCREEN_TIME
    global_stuff.MAXIMUM_NO = global_stuff.TOTAL_TIME / global_stuff.FRAME_TIME
    # GRAVITY
    global_stuff.GRAVITY_TIME_START = global_stuff.TO_SHIFT_SCREEN*4
    global_stuff.GRAVITY_STEP = 1
    # SCORES
    global_stuff.SCORE = 0
    global_stuff.COINS = 0
    global_stuff.BEAMS = 0
