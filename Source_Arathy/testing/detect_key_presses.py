import getch

while(True):
    a = getch.getch()
    if(a == 'w'):
        msg = 'up'
    elif(a == 's'):
        msg = 'down'
    elif (a == 'a'):
        msg = 'left'
    elif(a == 'd'):
        msg = 'right'
    print(msg)
