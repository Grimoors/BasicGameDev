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
                    if [x_cor,y_cor+1] in self._class_positions['iceball']:
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