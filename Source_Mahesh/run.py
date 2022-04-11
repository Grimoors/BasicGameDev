''' The run file instances of other classes are used here to run game '''
import os
import random,sys,time
import threading
from inp import *
from os import system
from colorama import *
from header import header 
from board import board
from people import *
from objects import *
from mandolorian import *
from bossenemy import *
print("Welcome to the Jetpack Joyride ")
print("Press Enter to start" , end = "")
inp = input()
system('clear')
head = header(1000,0,3)
Board= board(5000,30)
objects=scoringobject()
objects.createpositions()
objects.places()
Board.printobjects(objects)
mando=mandolorian()
bossenemy=boss()
#bossenemy.addtoobstacles(objects)
getch = Get()
i = 0
# for shield
shield = 0
powerup=0
dragonactivation=0
powerupactivation=0
shieldactivation=0
poweruptime=0
shieldtime=0
dragonstuff=0
dragontime=0
while True:
    print(Style.RESET_ALL) 
    dragonstuff=0
    collision=Board.checkcollisions(head,mando,objects,bossenemy)
    Board.printmagnet(objects,'magnet')
    if collision == 1:
        Board.printobjects(objects)
        time.sleep(2)
        Board.sety()
    print("\033[0;0H")
    input=input_to(getch)
    shield= mando.getshieldraisevalue()
    dragon=mando.getdragoncheck()
    if mando.getplayery()>220 and dragon==0:
        dragonactivation=1
    else:
        dragonactivation=0
    if mando.getshieldraisevalue()==0:
        shieldactivation=1
    else:
        shieldactivation=0
    if input == " " and shield == 0 and dragon!=1:
        mando.shieldfunction(board)
        shieldtime= i
        shieldstatus=1
    elif input == "q":
        system('clear')
        quit()
    elif input == "s" and powerup==0:
        Board.createbullets(mando,objects,"bullet")
    elif input == "x" and powerup==0:
        powerup=1
        poweruptime=i
    elif input=="h":
        Board.dragoncheck(mando)
        dragontime=i
    #if dragon==1 and input=="d":
    #    Board.setdragonstuff(mando)
    elif dragon!=1:
        Board.playermove(input,mando,head)
    Board.printbullets('bullet',objects)
    Board.printbullets('iceball',objects)
    head.printhead(shieldactivation,1-powerup,dragonactivation)
    #Board.update_y()
    print(Style.RESET_ALL) 
    i = i + 1
    if i%5==0:
        if dragon==1:
            for j in range(0,4):
                Board.createbullets(mando,objects,"bullet")
            Board.setdragonstuff(mando)
        if powerup!=1 :
            Board.update_y(mando,head)
        x=mando.getplayerx()
        Board.playermove(x,bossenemy,head)
        Board.moveobjects('iceball',objects,-1,head,bossenemy)
        Board.moveobjects('bullet',objects,2,head,bossenemy)
        magnetattractvalue=Board.magnetattraction('magnet',mando,objects,head)
        if magnetattractvalue == 1:
            Board.checkplayer(mando)
    if i%10==0:
        head.changetime()
    if  i%10==0 and Board.gety()>600:
        Board.createbullet(bossenemy,objects,mando)
    if shield == 1 and i - shieldtime == 100:
        mando.removeshield(Board)
    if shield == 1 and i-shieldtime ==600:
        mando.raiseshield()
        shieldstatus=1
    if powerup==1 and i-poweruptime==100:
        powerup=-1
    if powerup==-1 and i-poweruptime==300:
        powerup=0
    if powerup == 1 and (i-poweruptime)%1==0: 
        Board.update_y(mando,head)
    if dragon==1 and i-dragontime==200:
        Board.removedragon(mando)
    dragon=mando.getdragoncheck()
    if dragon==-1 and i-dragontime==300:
        mando.setdragoncheck(0)
    print(Style.RESET_ALL)
    Board.printboard(30,mando,bossenemy,dragon)
    print(Style.RESET_ALL) 
    
