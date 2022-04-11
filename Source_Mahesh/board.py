from colorama import *
from people import *
import random
from objects import *
from collections import Counter
''' Board class containing background board
It also comprises of printing functions'''
class board():
    ''' Board class''' 
    def __init__(self,length,height):
        self.__length = length
        self.__height = height
        self.__matrix = []
        self._Y=0
        self.__matrxi2=[]
        #matrix creation
        for y in range(0, self.__height):
            self.__matrix.append([])
            for x in range(0,self.__length):
                if y < (self.__height-2) and y > 2:
                    self.__matrix[y].append(Back.CYAN+' ')
                elif  y <= 2:
                    self.__matrix[y].append(Back.YELLOW+' ')
                else:
                    self.__matrix[y].append(Back.RED+' ')

    def getmatrixinboard(self):
        return self.__matrix

    def editmatrix(self,mat):
        self.__matrix = mat
    
    # print coins in board
    def printobjects(self,obj):
        self.__matrix=obj.printobject(self.__matrix,'45beams')
        self.__matrix=obj.printobject(self.__matrix,'horbeams')
        self.__matrix=obj.printobject(self.__matrix,'verbeams')
        self.__matrix=obj.printobject(self.__matrix,'coin')

    # printing board
    def printboard(self,height,obj,obj2,dragonstuff):
        mat = self.__matrix
        y=obj.getplayery()
        x=obj.getplayerx()
        if y > self._Y + 150:
            self._Y+=150
        print(dragonstuff)
        if dragonstuff!=1:
            self.__matrix=obj.printplayertoboard(self.__matrix)
        else:
            self.updatedragon(obj)
        self.__matrix=obj2.printplayertoboard(self.__matrix)
        for x in range (0,height):
            for j in range(self._Y,self._Y+150):
                    print(self.__matrix[x][j],end="")
            print("")

    # moving mandolorian on board using object
    def playermove(self,s,obj,head):    
        self.__matrix=obj.playermove(s,self.__matrix,head,self._Y)
    # creatingbullets
    def createbullets(self,mand,obj,str):

            y=mand.getplayery()
            x=mand.getplayerx()
            mat=mand.getplayermatrix()
            dragon=mand.getdragoncheck()
            if dragon!=1:
                obj.addpositions(x+1,y+3,str)
            else:
                obj.addpositions(x,y+20,str)
    def createbullet(self,boss,obj,mando):
            x=mando.getplayerx()
            y=boss.getplayery()
            obj.addpositions(x+1,y+25,'iceball')


    def printbullets(self,str,obj):
        self.__matrix=obj.bulletprinting(str,self.__matrix)
    # checkng gravity for mandolorian
    def checkplayer(self,obj):
        self.__matrix=obj.checkplayer(self.__matrix)

    # moving board at 1 m/sec
    def update_y(self,mando,head):
        if self._Y < 4870:
            self._Y+=1
            mando.playermove("d",self.__matrix,head,self._Y)
    def moveobjects(self,str,obj,velocity,head,bossenemy):
        self.__matrix=obj.moveobjects(str,self.__matrix,velocity,head,bossenemy)    
    
    def checkcollisions(self,head,player,objects,bossenemy):
        x_cor=player.getplayerx()
        y_cor=player.getplayery()
        shield=player.getshieldvalue()
        length=player.getplayerlength()
        mat=player.getplayermatrix()
        f=0
        a=player.getshieldvalue()
        listofobjects=objects.getallpositionmatrix()
        list2=objects.getclasspositions('coin')
        list3=bossenemy.getallpositionmatrix()
        dragon=player.getdragoncheck()
        matrix=[]
        for i in  range(0,length):
            for j in range(0,len(mat[i])):
                if [x_cor+i,y_cor+j] in listofobjects  and shield ==0:  
                    if dragon!=1:
                        head.changelives()
                        f=1
                        player.changecordinates(25,0)
                        break
                    #else:
                    #    self.__matrix=player.removedragon(self.__matrix)
                    #    break 
                elif [x_cor+i,y_cor+j] in list3  and shield ==0:
                    if dragon!=1: 
                        head.changelives()
                        f=1
                        player.changecordinates(25,0)
                        break
                    #else:
                    #    self.__matrix=player.removedragon(self.__matrix)
                    #    break 
                elif [x_cor+i,y_cor+j] in list2:
                    list2.remove([x_cor+i,y_cor+j])
                    head.changescore('coin')
        if f==1:
            for i in  range(0,length):
                for j in range(0,len(mat[i])):
                    self.__matrix[x_cor+i][y_cor+j] =' '
        objects.setclasspositions('coin',list2)
        return f

    def printmagnet(self,obj,str):
        obj.printobject(self.__matrix,str)    
    
    def magnetattraction(self,str,mando,objects,head):
        matrix=objects.getclasspositions(str)
        x_cor=mando.getplayerx()
        y_cor=mando.getplayery()
        for i in range(0,len(matrix)):
            if  matrix[i][1]-50 <=y_cor   and  y_cor  <= matrix[i][1]+50 and matrix[i][1]> self._Y:
                if x_cor > matrix[i][0]:
                    mando.playermove('w',self.__matrix,head,self._Y)
                if x_cor < matrix[i][0]:
                    mando.playermove('n',self.__matrix,head,self._Y)
                if y_cor < matrix[i][1]:
                        mando.playermove('d',self.__matrix,head,self._Y)
                if y_cor > matrix[i][1] and y_cor > matrix[i][1]+8:
                        mando.playermove('a',self.__matrix,head,self._Y)
                        mando.playermove('a',self.__matrix,head,self._Y)
                        mando.playermove('a',self.__matrix,head,self._Y)

                return 0
            
        return 1

    def sety(self):
        self._Y=0
    def dragoncheck(self,mando):
        dragon=mando.getdragoncheck()
        y_cor=mando.getplayery()
        if y_cor > 450 and dragon==0:
            self.__matrix=mando.setmatrix(self.__matrix,self._Y)
    def gety(self):
        return self._Y
    def updatedragon(self,mando):
        matrix=mando.getplayermatrix()
        updatething=mando.getdragonstuff()
        x=mando.getplayerx()
        y=mando.getplayery()
        flag=mando.getflag()
        if flag==0:
            '''for i in range(len(matrix)):
                for j in range(0,len(matrix[i])):
                    self.__matrix[x+i-1][y-3+j]=' '
                    self.__matrix[x+i][y-3+j]='''
            for i in range(len(matrix)):
                for j in range(0,7):
                    if j>=updatething:
                        self.__matrix[x+i+1][y+j]=Fore.BLACK+matrix[i][j]
                    else:
                        self.__matrix[x+i][y+j]=Fore.BLACK+matrix[i][j]
        else:
            '''for i in range(len(matrix)):
                for j in range(0,len(matrix[i])):
                    self.__matrix[x+i+1][y-3+j]=' '
                    self.__matrix[x+i][y-3+j]='''
            for i in range(len(matrix)):
                for j in range(0,7):
                    if j<updatething:
                        self.__matrix[x+i-1][y+j]=Fore.BLACK+matrix[i][j]
                    else:
                        self.__matrix[x+i][y+j]=Fore.BLACK+matrix[i][j]
        #mando.changecordinates(x,y+1)

    def setdragonstuff(self,mando):
        self.__matrix=mando.setdragonstuff(self.__matrix)

    def removedragon(self,mando):
        self.__matrix=mando.removedragon(self.__matrix)