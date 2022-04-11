import random
import threading
from colorama import *
''' class containing all objects'''
class player(object):
    def __init__(self,x_cor,y_cor,length,height,matrix):
        self._x=x_cor
        self._y=y_cor
        self._length=length
        self._height=height
        self._shield=0
        self._shieldraise=0
        self._person=matrix
        self._velcocity=0
        self._gravity=0.8
        self._impulse=2.5
    # moving mandolorian
    # player things
    def getplayerx(self):
        return self._x

    def getplayery(self):
        return self._y
    
    def getplayermatrix(self):
        return self._person
    
    def getplayerlength(self):
        return self._length
    
    def getplayerheigth(self):
        return self._height
    
    def getshieldvalue(self):
            return self._shield
    def getshieldraisevalue(self):
            return self._shieldraise
    # check gravity
    def checkplayer(self,matrix):
        mat = matrix
        if self._dragoncheck!=1:
            if self._x < 25:
                for i in range(0,self._length):
                    for j in range(0,len(self._person[i])):
                        mat[self._x+i][self._y+j]=' '
                self._velcocity+=self._gravity
                self._x+=self._velcocity 
                self._x=int(self._x)
                if self._x > 25:
                    self._x=25
            else:
                self._velcocity=0
        return mat
    # print player to board

    def printplayertoboard(self,matrix):
        mat=matrix
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                if self._person[i][j]!=' ':
                    matrix[self._x+i][self._y+j]=Fore.BLACK+self._person[i][j]
        return matrix

    # move player
    def playermove(self,str,matrix,head,yboard):    
        x_cor=self._x
        y_cor=self._y
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                    matrix[self._x+i][self._y+j]=' '
        if str == "d"  and self._y< yboard+140: 
            self._y +=1
        if str == "a" and self._y>yboard:
            self._y-=1
        if str == "w" and self._x > 4 :
            self._x=self._x-2
            self._velcocity=0
        if str=="n" and self._x < 25:
            self._x=self._x+1
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                matrix[x_cor+i][y_cor+j]=' '    
        return matrix
    def changecordinates(self,x,y):
        self._x=x
        self._y=y
    