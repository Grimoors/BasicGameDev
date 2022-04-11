'''
bullet
======

This class denotes the orange-ish color bullets sent by the hero
It moves foreward at a speed of 2 forward moves per screen go-backs. The hero can never ever shoot backwards

It inherits from obstacle.

Additional Data Members
-----------------------

- exist

This variable is 1 if the bullet is already deployed, 0 otherwise

- deployable

This variable is 1 if the bullet can be deployed, that is if the hero wants, he can deploy it; 0 otherwise (if it needs to be reloaded)

Additional/Re-written Member Functions
--------------------------------------

- Constructor

This fixes the shape of the bullet.
Shape: ≡>
Also makes exist and deployable 0

- check_if_exist

Returns 1 if the bullet exists (that is, it is already deloyed)

- check_if_deployable

Returns 1 if the bullet can be deployed by the hero

- make_deployable(self):

Makes the bullet deployable 
This function is called once in a few frame passes

- delete_from_board

makes its existance 0

- move_right

Moves the bullet right (on the board) if it is already deployed
Also destroys coins, powerups and beams, the bullet touches 
However it does not destroy the magnet
If the bullet hits a beam or a magnet, it gets destroyed
Also takes care of the bullet getting destroyed if it goes out of the screen

- deploy

Responsible for deploying the bullet
Returns 1 on successful deployment 

- display

Displays the bullet if it exists

'''
import global_stuff
from obstacle import obstacle


class bullet(obstacle):
    def __init__(self):
        '''
        Initialises an obstacle with the length and width and shape of the bullet
        Shape: ≡>
        Also makes exist and deployable 0
        '''
        super().__init__(0, 0, 1, 2, [['≡', '>']], 'Bullet')
        self.__exist = 0
        self.__deployable = 0

    def check_if_exist(self):
        '''
        returns 1 if the bullet exists (that is, it is already deloyed)
        '''
        return self.__exist

    def check_if_deployable(self):
        '''
        returns 1 if the bullet can be deployed by the hero
        '''
        return self.__deployable

    def make_deployable(self):
        '''
        Makes the bullet deployable 
        This function is called once in a few frame passes
        '''
        self.__deployable = 1

    def delete_from_board(self):
        '''
        makes its existance 0
        '''
        self.__exist = 0

    def move_right(self, board):
        '''
        Moves the bullet right (on the board) if it is already deployed
        Also destroys coins, powerups and beams, the bullet touches 
        However it does not destroy the magnet
        If the bullet hits a beam or a magnet, it gets destroyed
        Also takes care of the bullet getting destroyed if it goes out of the screen
        '''
        if(self.check_if_exist() == 1):  # move it right if and only if the bullet has already been deployed
            is_magnet = 0  # 1 if what has been collided is a magnet or not
            try:
                for i in range(-1, 4):
                    what_is_destroyed = board.destroy_object(
                        self._x, self._y+i)
                    if(what_is_destroyed == 'Coin'):
                        global_stuff.score += 5  # 5 for coin collection by bullet
                    elif what_is_destroyed in ['Hbeam', 'Vbeam', 'Dbeam1', 'Dbeam2']:
                        global_stuff.score += 20  # 20 per beam destroyed
                        self.delete_from_board()  # after hitting a beam, the bullet ceases to exist
                    elif(what_is_destroyed == 'Magnet'):
                        self.delete_from_board()
                        is_magnet = 1
            except:
                pass
            try:
                # remove all traces of the earlier position of the bullet
                board.remove_from_board(self._x, self._y)
                if(is_magnet == 0):
                    board.remove_from_board(self._x, self._y+1)
                board.remove_from_board(self._x, self._y-1)

                # move it left
                self._y += 2
                # if it crosses the right end of the screen, it ceases to exist
                if(self._y+1 >= global_stuff.screen_length):
                    self.delete_from_board()
                elif(self.check_if_exist() == 1):  # if and only if the bullet still exists, print it
                    self.write_self_on_board(board)
                    if(global_stuff.debug == 1):
                        print('BULLET', self._x, self._y)
            except Exception as e:
                # if there is any error while displaying the bullet, just remove its existence
                print(e)
                self.delete_from_board()

    def deploy(self, hero):
        '''
        Responsible for deploying the bullet
        Returns 1 on successful deployment 
        '''
        if(self.check_if_deployable() == 0):
            return 0
        else:
            try:
                (self._x, self._y) = hero.get_coord()
                self._y += 4
                self.__exist = 1
                self.__deployable = 0
                global_stuff.bullets_left -= 1
                return 1
            except Exception as e:
                print(e)
                return 0

    def display(self, board):
        '''
        Displays the bullet if it exists
        '''
        if(self.check_if_exist() == 1):
            self.write_self_on_board(board)
