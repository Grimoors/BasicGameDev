import numpy as np
hero=[['▄', '['], ['|', '|']]
# ▄[
# ||
snake_generator=[
  [' ',' ',' ',' ','.','-','-','-',',',' '],
  ['-','-','-','/',' ',' ',' ',' ',' ','\\']
      ]

hw=2
hh=2
sgh=2
sgw=10
width=30



main_snake=np.full((2,width),' ')
j=0
start_ind=1

# put hero at its location in the beginning
for i in range(2):
    for j in range(2):
        main_snake[i][j]=hero[i][j]
# fill in the remaining
for column in range(width-2):
    for i in range(2): 
        main_snake[i][column+2]=snake_generator[i][(column+start_ind)%10]

for i in main_snake:
    for j in i:
        print(j,end="")
    print("")