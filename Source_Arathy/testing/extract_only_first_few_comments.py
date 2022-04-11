import os
for filename in os.listdir(os.getcwd()):
    try:
        f = open(filename, 'r')
        content = f.read()
        cont=content.split('\'\'\'')
        print (filename,'\n', cont[1],'\n\n')
    except Exception as e:
        print (e)