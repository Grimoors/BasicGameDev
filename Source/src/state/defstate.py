import imp
import sys as sys
import time as time
import os as os
import random as random
import math as math
from .screen import *

if __name__ == "__main__":
    print("This module at \"/src/\" can NOT run standalone")
    sys.exit(1)
else:
    
    
    #Stack Implementation Program
    #Using Python List
    stack = []
    #Push Operation
    #Using append() Method
    #stack.append("A")
    #Pop Operation
    #Using pop() method
    #//print("Updated Stack:", stack)
    #Item at the top of Stack
    # print("Item at Stack Top:", stack[-1])
    #Stack Size
    #using len() method
    # print("Current Stack Size:", len(stack))
    #Check if stack is empty or not
    # if not stack:
    #     print("Stack is Empty!")
    # else:
    #     print("Stack is Not Empty!")


    class states:

        def __init__(self):
            self.stack = []
            json = {
                "state": "start",
                "screen" : "start",
                "timestep": 0,
                "onPop": "quit",
                "toPop": "-",
            }
            self.stack.append(json)
        
        def push(self, state):
            self.stack.append(state)
            return self.stack
        
        def pop(self):
            self.stack.pop()
            return self.stack

        def peek(self):
            return self.stack[-1]

        def flush(self):
            self.stack = []
            return self.stack
        
        def getState(self):
            return self.stack[-1]["state"]
        
        def getScreen(self):
            return self.stack[-1]["screen"]
        
        def getTimestep(self):
            return self.stack[-1]["timestep"]
    
        def getOnPop(self):
            return self.stack[-1]["onPop"]
        
        def getToPop(self):
            return self.stack[-1]["toPop"]
        
        def getStack(self):
            return self.stack
        
        def getStackSize(self):
            return len(self.stack)
        
        def isEmpty(self):
            if not self.stack:
                return True
            else:
                return False
        
        StateList = ["start", "game", "titlemenu" , "levelselect" , "pausemenu" ,  "quit" , "flush" , "reset"]
        StateJsons = [ { "state": "start",
                "screen" : "start",
                "timestep": 0,
                "onPop": "quit",
                "toPop": "-", }     ,
                
                { "state": "game",
                "screen" : "game",
                "timestep": 1,
                "onPop": "pausemenu",
                "toPop": "~", }     ,

                { "state": "titlemenu",
                "screen" : "titlemenu",
                "timestep": 0,
                "onPop": "start",
                "toPop": "-", }     ,
                
                { "state": "levelselect",
                "screen" : "levelselect",
                "timestep": 0,
                "onPop": "start",
                "toPop": "~", }     ,

                { "state": "pausemenu",
                "screen" : "pausemenu",
                "timestep": 0,
                "onPop": "game",
                "toPop": "~", }     ,

                { "state": "quit",
                "screen" : "quit",
                "timestep": 0,
                "onPop": "",
                "toPop": "", }     ,

                { "state": "flush",
                "screen" : "flush",
                "timestep": 0,
                "onPop": "",
                "toPop": "", }     ,

                { "state": "reset",
                "screen" : "reset",
                "timestep": 0,
                "onPop": "",
                "toPop": "", }     ,
                                        ]   
        
            

        