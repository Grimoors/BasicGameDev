# scoring objects like coins and enemies objects and score array
import  random
from colorama import *
class scoringobject():
    def __init__(self):
        # object contains all obstacles
        self._obstacles={
            'coin'     :[['$']],
            'horbeams' : [['0','-','-','-','-','-','0']],
            'verbeams' : [['0'],['|'],['|'],['|'],['0']],
            '45beams'  : [['\\','\\'],[' ','\\','\\'],[' ',' ','\\','\\'],[' ',' ',' ','\\','\\'],[' ',' ',' ',' ','\\','\\']],
            'magnet'   :[["|",'|','X','X','|','|'],["|",'|','X','X','|','|'],['|','|','X','X','|','|']],
            'iceball'   :[['O']],
            'bullet'    :[['*']]
        }
        #height width strength
        self._class_types = {    
            'horbeams'  : [1,7,1],
            'verbeams'  : [5,1,1],
            '45beams'   : [5,6,2],
            'magnet'    : [3,8,3],    
            'iceball'   : [1,1,1],
            'coin'      : [1,1,0],
            'bullet'    :[[1,1,0]]
        }
        self._class_positions ={
            
            '45beams' : [],
            'verbeams': [],
            'magnet'  : [[7,75],[10,225],[17,310]],
            'horbeams': [],
            'iceball' : [],
            'bullet'  : [],
            'coin'    : []
        }
        self._class_allpositions=[]


    def getclasspositions(self,str):
            return self._class_positions[str]
    def setclasspositions(self,str,mat):
            self._class_positions[str]=mat
    def getclassmatrix(self):
            return self._obstacles
    def printobject(self,matrix,str):
        mat = matrix 
        if str !='coin':
            for i in range(0,len(self._class_positions[str])):
                y_cor=self._class_positions[str][i][1]
                x_cor=self._class_positions[str][i][0]
                for j in range(self._class_types[str][0]):
                    for k in range(0,len(self._obstacles[str][j])):
                        mat[x_cor+j][y_cor + k] = Fore.BLACK + self._obstacles[str][j][k]
        else:
            for i in range(0,len(self._class_positions[str])):
                y_cor=self._class_positions[str][i][1]
                x_cor=self._class_positions[str][i][0]
                for j in range(self._class_types[str][0]):
                    for k in range(0,len(self._obstacles[str][j])):
                        mat[x_cor+j][y_cor + k] = Fore.YELLOW + self._obstacles[str][j][k]
        return mat



    def moveobjects(self,str,matrix,velocityy,head,bossenemy):
        mat=matrix
        mat2=[]
        bossenemymatrix=bossenemy.getallpositionmatrix()
        for i in range(0,len(self._class_positions[str])):
            x_cor=self._class_positions[str][i][0]
            y_cor=self._class_positions[str][i][1]
            mat[x_cor][y_cor]=' '
            if str =='bullet':
                if [x_cor,y_cor+1] in self._class_allpositions :
                    self._class_allpositions.remove([x_cor,y_cor+1])
                    if [x_cor,y_cor+1] in self._class_positions['iceball']:
                        self._class_positions['iceball'].remove([x_cor,y_cor+1])
                    mat2.append([x_cor,y_cor])
                    mat[x_cor][y_cor+1]=' '
                    head.changescore('enemy')

                elif [x_cor,y_cor+2] in self._class_allpositions:
                    if [x_cor,y_cor+2] in self._class_positions['iceball']:
                        self._class_positions['iceball'].remove([x_cor,y_cor+2])
                    self._class_allpositions.remove([x_cor,y_cor+2])
                    mat2.append([x_cor,y_cor])
                    mat[x_cor][y_cor+2]=' '
                    head.changescore('enemy')
                
                elif mat[x_cor][y_cor+2]==Fore.YELLOW+ Back.CYAN+'$':
                     if self._class_positions[str][i][1]+velocityy+1 > 0 and self._class_positions[str][i][1]+ velocityy < 900 :
                            self._class_positions[str][i][1]+=velocityy+1                    
                
                elif [x_cor,y_cor+1] in bossenemymatrix:
                    bossenemymatrix.remove([x_cor,y_cor+1])
                    head.changescore('enemy')
                    mat[x_cor][y_cor+1]=' '  
                    mat2.append([x_cor,y_cor])
                    bossenemy.changestrength()
                
                elif [x_cor,y_cor+2] in bossenemymatrix:
                    bossenemymatrix.remove([x_cor,y_cor+2])
                    head.changescore('enemy')
                    mat[x_cor][y_cor+2]=' '  
                    mat2.append([x_cor,y_cor])
                    bossenemy.changestrength()

                else:
                    if self._class_positions[str][i][1]+velocityy > 0 and self._class_positions[str][i][1]+ velocityy < 900 :
                        self._class_positions[str][i][1]+=velocityy
            if str =='iceball':
                if [self._class_positions[str][i][0],self._class_positions[str][i][1]] in self._class_allpositions:
                    self._class_allpositions.remove([self._class_positions[str][i][0],self._class_positions[str][i][1]])
                if self._class_positions[str][i][1]+velocityy > 0 and self._class_positions[str][i][1]+ velocityy < 1200 :
                    self._class_positions[str][i][1]+=velocityy
                self._class_allpositions.append([self._class_positions[str][i][0],self._class_positions[str][i][1]])
        for i in range(0,len(mat2)):
            self._class_positions[str].remove(mat2[i])
        return mat    
    
    
    # printbullets
    # printbullets
    def bulletprinting(self,str,matrix):
        mat = matrix    
        if str == 'bullet':
            for i in range(0,len(self._class_positions[str])):
                x_cor=self._class_positions[str][i][0]
                y_cor=self._class_positions[str][i][1]
                mat[x_cor][y_cor]=Fore.RED+self._obstacles[str][0][0]
        else:
            for i in range(0,len(self._class_positions[str])):
                x_cor=self._class_positions[str][i][0]
                y_cor=self._class_positions[str][i][1]
                mat[x_cor][y_cor]=Fore.BLACK+self._obstacles[str][0][0]
        return mat
    
    def listofobjectsingame(self,str):
        for l in range(0,len(self._class_positions[str])):
            for j in range(0,len(self._obstacles[str])):
                for k in range(0,len(self._obstacles[str][j])):
                    if self._obstacles[str][j][k]!=' ':
                        self._class_allpositions.append([self._class_positions[str][l][0]+j,self._class_positions[str][l][1]+k])
    
    def places(self):
        self.listofobjectsingame('45beams')
        self.listofobjectsingame('horbeams')
        self.listofobjectsingame('verbeams')
        
    def addpositions(self,x,y,str):
        self._class_positions[str].append([x,y])
        if str =='iceball':
            self._class_allpositions.append([x,y])
    
    def getallpositionmatrix(self):
        return self._class_allpositions
    def setallpositionmatrix(self,mat):
        self._class_allpositions=mat
    def createpositions(self):
        x=random.randint(17,24)
        self.createselfpositions('coin',x,12,10)
        self.createselfpositions('verbeams',4,23,10)
        self.createselfpositions('horbeams',4,25,10)
        self.createselfpositions('45beams',4,23,10)
    def createselfpositions(self,str,len,x_cor,y_cor):
        for i in range(0,len):
            x_cor1=random.randint(3,x_cor)
            y_cor1=random.randint(150*i,150*i+75)
            x_cor2=random.randint(3,x_cor)
            y_cor2=random.randint(150*i+75,150*i+150)
            if str=='coin':
                y_cor2=int(y_cor2/4)
                y_cor1=int(y_cor1/4)
            if [x_cor1,y_cor1] in self._class_positions[str]:
                i=i-1
            else:
                self._class_positions[str].append([x_cor1,y_cor1])
            if [x_cor2,y_cor2] in self._class_positions[str]:
                i=i-1
            else:
                self._class_positions[str].append([x_cor2,y_cor2])