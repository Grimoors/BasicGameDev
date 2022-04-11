class scenery:
    def __init__(self):

        f = open('scenery.txt','r') 
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
        self.__matrix=matrix