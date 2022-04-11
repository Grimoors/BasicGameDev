'''
beam
====

This class denotes the yellow/red laser/fire beams. 
Note that the width of the beam is always one. Also, while defining the beam, we have put some extra space around the beam just for safety reasons (so that I would not print one beam next to the other)

It inherits from obstacle.

Additional Data Members
-----------------------

NONE

Additional/Re-written Member Functions
--------------------------------------

- Constructor

Here, an additional parameter, orientation, is passed to the constructor. This parameter determines the overall orientation of the beam
The beam can be :
- Horizontal (h): -
- Vertical (v): |
- Diagonal 1 (d1): \
- Diagonal 2 (d2): /
Each of these orientations have their own height, width and shape.

Refer to the code for more details.
'''

from obstacle import obstacle
from global_stuff import length_of_beam, safe_region
import numpy as np


class beam(obstacle):

    def __init__(self, xpos, ypos, orientation):
        '''
        Here, an additional parameter, orientation, is passed to the constructor. This parameter determines the overall orientation of the beam
        '''
        # Horizontal beam : (2*safe_region+1 x length_of_beam+2*safe_region)
        if(orientation == 'h'):
            k = np.full((2*safe_region+1, length_of_beam+2*safe_region), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+length_of_beam-1):
                k[safe_region][i] = '-'
            k[safe_region][safe_region+length_of_beam-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, 2*safe_region+1,
                             length_of_beam+2*safe_region, sh, 'Hbeam')

        # Vertical beam: (length_of_beam/2+2*safe_region x 2*safe_region)
        elif(orientation == 'v'):
            k = np.full((int(length_of_beam/2)+2 *
                         safe_region, 2*safe_region+1), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/2)-1):
                k[i][safe_region] = '|'
            k[safe_region+int(length_of_beam/2)-1][safe_region] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/2) +
                             2*safe_region, 2*safe_region+1, sh, 'Vbeam')

        # Diagonal 1 beam: (length_of_beam/1.5+2*safe_region)^2
        elif(orientation == 'd1'):
            k = np.full((int(length_of_beam/1.5)+2*safe_region,
                         int(length_of_beam/1.5)+2*safe_region), ' ')
            k[safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/1.5)-1):
                k[i][i] = '\\'
            k[safe_region+int(length_of_beam/1.5) -
              1][safe_region+int(length_of_beam/1.5)-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/1.5)+2*safe_region,
                             int(length_of_beam/1.5)+2*safe_region, sh, 'Dbeam1')

        # Diagonal 2 beam: (length_of_beam/1.5+2*safe_region)^2
        elif(orientation == 'd2'):
            k = np.full((int(length_of_beam/1.5)+2*safe_region,
                         int(length_of_beam/1.5)+2*safe_region), ' ')
            k[safe_region+int(length_of_beam/1.5)-1 -
              safe_region][safe_region] = '█'
            for i in range(safe_region+1, safe_region+int(length_of_beam/1.5)-1):
                k[safe_region+int(length_of_beam/1.5)-1-i][i] = '/'
            k[safe_region+int(length_of_beam/1.5)-1-safe_region-int(
                length_of_beam/1.5)+1][safe_region+int(length_of_beam/1.5)-1] = '█'
            sh = k.tolist()
            super().__init__(xpos, ypos, int(length_of_beam/1.5)+2*safe_region,
                             int(length_of_beam/1.5)+2*safe_region, sh, 'Dbeam2')
