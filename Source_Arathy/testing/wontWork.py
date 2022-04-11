'''
Contains the initialization of the game board
has the following components:

rows: height of the board   : Here I fix it as 50
columns: width of the board : Here I fix it as 200

The rows can be divided into the following parts
0 -> 2: The top bar that contains the name of the game colored with blue
rows-3 -> rows: the bottom bar containing the lives left and the time remaining
'''
import numpy as np
from colorama import Fore, Back, Style
#from colored_printing import print_coloured
from termcolor import colored
class gameboard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = np.full((rows, columns,3), " "*10) # the structure of each element of the 2D matrix of triplets is: {ASCII CHAR, FGCOLOR, BGCOLOR}
        
        # The upper part
        for i in range(0, 2):
            for j in range(self.columns):
                self.board[i][j][0]=" "
                self.board[i][j][1]="white"
                self.board[i][j][2]="on_blue"
        # put the game name
        gamename = "THE MANDALORIAN"
        leng = len(gamename)
        startat = int(columns/2-leng/2)
        for i in range(leng):
            self.board[0][i+startat][0] = gamename[i] # put the game name
        # The game body
        for i in range(1, self.rows-3):
            for j in range(self.columns):
                self.board[i][j][0]=" "
                self.board[i][j][1]="white"
                self.board[i][j][2]="on_magenta"
        # the lower part
        for i in range(self.rows-3, self.rows):
            for j in range(self.columns):
                self.board[i][j][0]=" "
                self.board[i][j][1]="white"
                self.board[i][j][2]="on_blue"


    def print(self):
        # The top menu
        print(Back.BLUE+Fore.WHITE+"", end="")
        for i in range(self.rows):
            for j in range(self.columns):
                #k=self.board[i][j][0]
                #l=self.board[i][j][1]
                #print(self.board[i][j])
                #print(i,j,k,l,self.board[i][j][2])
                print(colored(self.board[i][j][0],(self.board[i][j][1]),self.board[i][j][2]),end="")
            print()
