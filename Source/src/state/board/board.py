from distutils.log import error
# from tkinter import Grid
from entities.entitymodel import entitymodel as entitymodel
from numpy import empty
import numpy as np


if "__name__" != "__main__":
    import numpy as np
    class GridCell:
        def __init__(self) -> None:
            self.occupied = False
            self.occpancyType = dict()
            self.occpancyType.__init__(dict(building=None, entity = None, obstacle = None))
            pass
        def __init__(self,props) -> None:
            pass
        
        def cell_empty_check(Cells):
            empty = bool()
            if not (Cells[:].occupied):
                empty = False
            return empty
            pass


    class BoardGrid:
        
        def __init__(self, width , height) -> None:
            self.width = width
            self.height = height
            self.ids=np.array(dtype=entitymodel.EntityId)
            self.ymax = self.height
            self.xmax = self.width 

            # lattice = np.empty( (3,3), dtype=object)
            # lattice.flat = [site(3) for _ in lattice.flat]
            self.grid=np.empty( (self.width,self.height), dtype = GridCell() )
            # self.grid.flat = [ GridCell() for cell in self.grid.flat ]
        
        def place_in_grid (self,x1, y1,x2,y2, object):
            
            
            if not GridCell.cell_empty_check( self.grid.flat[ (x1*self.width+y1):(x2*self.width+y2 ) ] ):
                for cell in self.grid.flat[ (x1*self.width+y1):(x2*self.width+y2 ) ]:
                    cell.occupied = True
                    if():
                        object.type="building"
                        cell.occupancyType={"building":True}
                        pass
                    if():
                        object.type="entity"
                        cell.occupancyType={"entity":True}
                        pass
                    if():
                        object.type="obstacle"
                        cell.occupancyType={"obstacle":True}
                        pass
                    
                    self.ids = np.append(self.ids, entitymodel.EntityId (x1,y1,x2,y2,len(self.ids),object.name) )
                    continue
                pass
            else:
                error("Cells Not Empty at (",x1,",",y1,") : (",x2,",",y2,")")

            pass
        
        def find_in_grid(self):
            
            pass
        
        def read_grid(self):
            pass

        def colorify_grid(self):
            pass
            
        



else:
    print("This module at \"/src/board/board.py\" cannot run standalone")