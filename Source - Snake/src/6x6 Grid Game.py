position = 0
print ('Press r to roll')
print ('Press q to quit')

import ossaudiodev
from pdb import post_mortem
import random
from turtle import pos
def roll(position):
    imp = str(input("->"))
    while imp != 'q':
        x = random.randint(1,6)
        position += x
        print("The dice rolled",x,"steps forward")
        print("You were at postiion ",position)
        if (position == 2):
            position =22
        if( position == 10):
            position = 5
        if( position == 17 ):
            position = 7
        if( position == 18):
            position=32
        if( position == 28):
            position = 16
        if( position == 24):
            position = 11
        if( position == 35):
            position = 1
        if( position == 36 ):
            print("You won!")
            break
        if(position<36):
            print ("Your current position is ",position)
        if(position>36):
            print("ERROR - INVALID POS - Subtacting 36")
            position= position - 36
            print("NEW POS = ",position)
        inp =str(input('->'))
        continue

roll(position)
