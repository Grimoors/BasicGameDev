# class to print self line of score ,lives and time we are playing 
from colorama import *

class header:

    ''' main class to manage score,lives '''
    def __init__(self,time,score,lives):
        self.__score = score
        self.__lives = lives
        self.__time = time

    # Function to print self(score,time,lives)
    
    def printhead(self,sheildactivation,powerupactivation,dragonactivation):
        
        ''' prints the self '''
        print("")
        print(Fore.GREEN +"TIME REMAINING : "+ str(self.__time) + " \t\t\t SCORE : " + str(self.__score)+ "\t\t\t  LIVES LEFT : " + str(self.__lives) )
        print("")
        string=""
        if sheildactivation==1:
            string+= " shield can be activated : "+" Yes "
        else:
            string+= " shield can be activated : "+" No "   
        if powerupactivation==1:
            string+=" powerup can be activated : "+" Yes "
        else:
            string+=" powerup can be activated : "+" No "
        if dragonactivation==1:
            string+=" dragon can be activated : "+" Yes "
        else:
            string+=" dragon can be activated : "+" No "

        print(Fore.GREEN+string)
    # Function to change lives

    def changelives(self):
        
        if self.__lives != 0:
            self.__lives -= 1
        
        else:
            print("GAMEOVER")
            print("Your Final Score is : " + str(self.__score) + " Play time is :" + str(1000-self.__time))
            print('')
            quit()

    # for time changing
    def changetime(self):
        if self.__time == 0:
            print("Sorry, You ran out of time")
            print("GAMEOVER")
            quit()
        else:
           self.__time-=1
        
    # for score changing
    
    def changescore(self,killed):
        if killed == 'enemy':
            self.__score += 10
    
        if killed == 'coin':
            self.__score+=5


