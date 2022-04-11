import random
import threading
from people import *
import numpy as np
class mandolorian(player):
    # intialise mandorian
    def __init__(self):
        self.__mand2=[['|',"0",' ','|'],['|','|','-','|'],['|',"|",'\\'," "]]
        self.__mand=[["0"],['|','-'],["|",'\\']]
        self._dragoncheck=0
        self.__mand3=[['*','*','*','*',' ',' ',' '],['*','*','*','*','*',' ',' '],['*','*','*','*','*','*','0'],['*','*','*','*','*',' ',' '],['*','*','*','*',' ',' ',' ']]
        #self.__mand3 = np.array(self.__mdand3)
        #self.
        self._updatedragonstuff=7
        self._flag=0
        player.__init__(self,25,620,3,2,self.__mand)
   
    # raise shield
    def removeshield(self,obj):
        self._shield=0
        mat=obj.getmatrixinboard()
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                mat[self._x+i][self._y+j]=' '
        self._person=self.__mand
        obj.editmatrix(mat)

    # remove shield
    def raiseshield(self):
        self._shieldraise =0

    #shieldfunction shield 0 means valid
    def shieldfunction(self,obj):    
        self._shield = 1
        self._shieldraise=1
        self._person = self.__mand2
    def setmatrix(self,matrix,Y):
        mat=matrix
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                matrix[self._x+i][self._y+j]=' '
        self._person=self.__mand3
        self._length=len(self.__mand3)
        self._x=6
        self._y=Y
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                    matrix[self._x+i][self._y+j]=Fore.BLACK+self._person[i][j]
        self._dragoncheck=1
        return matrix
    def getdragoncheck(self):
        return self._dragoncheck
    def setdragoncheck(self,a):
        self._dragoncheck=a
    def removedragon(self,matrix):
        self._dragoncheck=-1
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                matrix[self._x+i][self._y+j]=' '
        self._person=self.__mand
        self._length=3
        return matrix
    def getdragonstuff(self):
        return self._updatedragonstuff
    ''''def setdragonstuff(self,matrix):
        if self._flag==0:
                if self._updatedragonstuff>0:
                    self._updatedragonstuff-=1
                else:
                    self._flag=1
                for i in range(len(self._person)):
                    for j in range(0,len(self._person[i])):
                        matrix[self._x+i-1][self._y+j-3]=' '
                        matrix[self._x+i][self._y+j-3]=' '
                self._x+=1
                self._y+=1
        else:
            if self._x<=6:
                self._flag=0
            else:
                if self._updatedragonstuff<7:
                    self._updatedragonstuff+=1
                else:
                    self._flag=0
                for i in range(len(self._person)):
                    for j in range(0,len(self._person[i])):
                        matrix[self._x+i+1][self._y+j-3]=' '
                        matrix[self._x+i][self._y+j-3]=' '
                self._y+=1
                self._x-=1
        return matrix'''
    def setdragonstuff(self,matrix):
        if self._flag==0:
            if self._x > 20:
                self._flag=1
            else:
                if self._updatedragonstuff>0:
                    self._updatedragonstuff-=1
                else:
                    self._updatedragonstuff=7
                for i in range(len(self._person)):
                    for j in range(0,len(self._person[i])):
                        matrix[self._x+i-1][self._y+j-3]=' '
                        matrix[self._x+i][self._y+j-3]=' '
                self._x+=1
                self._y+=1
        else:
            if self._x<=6:
                self._flag=0
            else:
                if self._updatedragonstuff<7:
                    self._updatedragonstuff+=1
                else:
                    self._updatedragonstuff=0
                for i in range(len(self._person)):
                    for j in range(0,len(self._person[i])):
                        matrix[self._x+i+1][self._y+j-3]=' '
                        matrix[self._x+i][self._y+j-3]=' '
                self._y+=1
                self._x-=1
        return matrix

    
    def getflag(self):
        return self._flag
    def setflag(self,a):
        self._flag=a
