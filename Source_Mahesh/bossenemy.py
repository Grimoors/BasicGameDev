from people import *
class boss(player):
    def __init__(self):
        self._strength=50
        self._up=0
        f = open('dragon.txt','r') 
        text=f.read()
        matrix=[[]]
        text[0].strip('\n')
        j=0
        for i in range(0,len(text)):
            if text[i]=='\n':
                matrix.append([])
                j=j+1
            else:
                matrix[j].append(text[i])
        player.__init__(self,3,670,j,0,matrix)
    def playermove(self,s,matrix,head,yboard):    
        mat=matrix
        ranges=0
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                    mat[self._x+i][self._y+j]=' '
        ranges=int((s-3)/3)
        if self._x-3 > ranges and self._x > 3: 
            self._x-=1
        elif self._x-3 < ranges and self._x < 10:
            self._x+=1
        if self._y < 4870:
            self._y+=1
        return mat
    def getallpositionmatrix(self):
        mat=[]
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                if self._person[i][j]!=' ':
                    mat.append([self._x+i,self._y+j])
        return mat
    def changestrength(self):
        if self._strength==0:
            print("You won")
            print("Thank You for rescuing Yodha")
            quit()
        else:
            self._strength-=1
    def printplayertoboard(self,matrix):
        mat=matrix
        for i in range(0,self._length):
            for j in range(0,len(self._person[i])):
                if self._person[i][j]!=' ':
                    matrix[self._x+i][self._y+j]=Fore.BLACK+self._person[i][j]
        return matrix
