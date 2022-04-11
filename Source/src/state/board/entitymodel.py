import math
from re import X
from typing import Type
from numpy import true_divide

# from ..draw.screen import screen as screen


class Entity:
    def __init__(self,drawDimentions,boardDimentions,entityPixels,entitytype, entityname) -> None:
        self.drawdim=drawDimentions
        self.boarddim=boardDimentions
        self.entityPixels = entityPixels 
        self.entitytype= entitytype
        self.entityname= entityname

    def CheckCollision(id1, id2, Board):
        if (Board.ids[id1].x > Board.ids[id2].x2 and Board.ids[id1].x2 < Board.ids[id2].x):
            return False
        if (Board.ids[id1].y > Board.ids[id2].y2 and Board.ids[id1].y2 < Board.ids[id2].y):
            return False
        return True
    
    def MoveChecks(id , Board):
        if Board.ids[id].y == 0 :
            Board.ids[id].y+=1
            Board.ids[id].y2+=1
        if Board.ids[id].y2 == Board.ymax :
            Board.ids[id].y2-=1
            Board.ids[id].y2-=1
        if Board.ids[id].x == 0 :
            Board.ids[id].x+=1
            Board.ids[id].x2+=1
        if Board.ids[id].x2 == Board.xmax :
            Board.ids[id].x2-=1
            Board.ids[id].x2-=1
    
    # def getPixelScreen(id, Board):
    #         Screen = screen.Vscreen( (Board.ids[id].y2 - Board.ids[id].y) , (Board.ids[id].x2 - Board.ids[id].x) )
    #         Screen.screenGrid = Board.ids[id].entityPixels.screenGrid[Board.ids[id].y*Board.ids[id].x:Board.ids[id].y2*Board.ids[id].x2]
    #         return Screen


class EntityId :
    def __init__(self,x,y,x2,y2,id,entityName) -> None:
        self.x = x
        self.y = y 
        self.x2= x2 
        self.y2 = y2
        self.id = id 
        self.name = entityName
        self.attriDict = dict()
        self.attriDict = {
            "hp":"",
            "atk":"",
            "def":"",
            "atkfreq":"",
            "type":""
        
        }
        self.setValues(self, self.Name)
    
    def setValues(self, TypeName):
        from . import TypeName as Type
        self.attriDict=Type.attriDict
        self.currHp = self.attriDict.get("hp")

