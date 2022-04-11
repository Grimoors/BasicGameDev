# FILES USED

## CLASSES USED

### NBInput

#### File: inputs.py

This class deals with non-blocking input.  
This was obtained from a stack overflow website (moss have mercy)

### full_board

#### File: full_board.py

This class denotes the entire board of the game that is pre-generated.  
Also known as the canvas of the game  
It has a height of only screen_height-5 as 2 of the rows are taken for the top bar and 3 for the bottom bar

#### Playable area

height: 2, screen_height-3
width: screen_length * total_no_screens

#### Data Members

- rows

Denotes the number of rows (horizontal things)

- columns

Denotes the number of columns (vertical things)

- board

Denotes the canvas were we would draw everything

#### Member Functions

- Constructor

Initialises the full board with the length, width and the board matrix  
Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it  
Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot

- getrows

A getter function for getting the number of rows in the full_board

- generate_background

generate a background of modern art up to the point where the enemy comes. Once the enemy comes, then the background is black and dismal

- check_if_permissible

returns 0 if the given coordinates of (X,Y) is not permissible  
That is, there is something else already at that location

- put_coins_block

Puts a coin block (of random height and width) at a random position on the given screen_no  
The counting of the screen_no starts from 1

- put_beam_block

Puts a beam block (of the given type) at a random position on the given screen_no  
The counting of the screen_no starts from 1  
Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it  
100 attempts are made before giving up(since the game must go on)

- put_powerup

Puts a powerup (of the given type) at a random position on the given screen_no  
The counting of the screen_no starts from 1  
Here the placement is done based on the condition: is_permissible, that is, check if there is nothing at the place where it will be placed and then place it  
100 attempts are made before giving up(since the game must go on)

- randomly_add_coins_everywhere

Generate coins randomly on the board based on the following metric

| Screen no | No of blocks             |
| --------- | ------------------------ |
| 1         | 2 (need not be distinct) |
| 2 - 9     | 4 (need not be distinct) |

- randomly_add_beams

Generate all kinds of beams randomly on the board based on the following metric

| Screen no | No of blocks                                    |
| --------- | ----------------------------------------------- |
| 0.5 - 5   | 2 blocks (placing if permissible) per beam type |

- randomly_add_powerups

Generate all types of powerups randomly on the board based on the following metric

| Powerup    | Screens applicable | Number per screen          |
| ---------- | ------------------ | -------------------------- |
| Extra Life | 1-10               | 1 (placing if permissible) |
| Speed Up   | 1- 5               | 1 (placing if permissible) |
| Extra Time | 1- 5               | 2 (placing if permissible) |
| Snek       | 1- 2               | 1 (placing if permissible) |

- add_magnet

Generate a magnet and place it on the screen randomly  
Screen number 3

- def prepare_board

Prepares the board :)

### gameboard

#### File: gameboard.py

This class denotes the game board that is currently being displayed on the screen.

#### Data Members

- rows

Denotes the number of rows (horizontal things) : 50

- columns

Denotes the number of columns (vertical things) : 200

- board

Denotes the canvas were we would draw everything

#### Member Functions

- Constructor

Initialises the full board with the length, width and the board matrix  
Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it  
Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot  
Also sets up the top bar(the first two rows), bottom bar(the last three rows) and prints all the accessories of the game board  

- gamename_display

Displays the game name on the top left corner of the game board on the top bar

- score_update

Displays the score on the top right corner of the game board on the top bar  
The score is left padded with 0s

- coins_collected_update

Displays the number of coins collected by the hero on the top right corner of the bottom bar

- life_display

Displays the life remaining of the hero on the top left corner of the bottom bar  
The life remaining is drawn using black blocks like a progress bar

- time_display

Displays the time remaining for the hero to save Baby Yoda on left side of the bottom bar  
The time remaining is drawn using black blocks like a progress bar

- game_progress_display

Displays the progress, i.e. how close the hero is to see the boss, on left side of the bottom bar  
The progress is drawn using black blocks like a progress bar

- bullets_display

Displays the number of bullets that are ready to be deployed but not deployed yet on the right side of the bottom bar

- display_powerups_active

Displays those powerups that are active on the right side of the bottom bar

- print_enemy_life

Displays the life remaining of the enemy on the top bar when the enemy comes  
The life remaining is drawn using black blocks like a progress bar

- prepare_board(self):

Prepares, i.e. updates the board before printing it on the screen

- print(self):

Prints the gameboard onto the screen

- write_full_on_board(self, full_board, start_in):

Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled

- shift_right(self, full_board, line_to_add):

Shift everything to right every .5 seconds

- is_magnet_on_screen(self):

Returns the y coordinate of the magnet if it is on the screen, otherwise return -1

- destroy_object(self, X, Y):

Destroys whatever object is there at position X,Y completely and returns the object type  
This function deals only with coins, beams and powerups  
However since magnets cannot be destoyed, if the current position has a magnet, then it does not destroy it

### obj

#### File: obj.py

This class denotes any object, be it an obstacle or a person, that can be rasterised on the board, or can be directly printed to the screen

This is a base class, from which obstacle and person are inherited

#### Data Members

- x

denotes the starting x coordinate of the object  
Note that x axis is the vertical axis and y axis is the horizontal axis

- y

denotes the starting y coordinate of the object

- h

denotes the height of the object along the x (vertical) axis

- w

denotes the width of the object along the y (horizontal) axis

- style

denotes the 2D matrix of ASCII characters to fill the h x w width

- type

denotes the type of the object; used later for painting the board.  
Responsible for handling colors and the collisions

#### Member Functions

- Constructor

Just assigns the parameters to its 'protected' variables

- write_self_on_board

Draw the style of the object onto the game board and make its type ty  
Also casterise the object onto the baord (make it one with the board)

- print_direct

Prints the object directly on the screen without disturbing the board

- destroy_self

Destroys itself from the board.

- change_type

Change the type of the object (used for changing the colors of the object mid-game)

- get_coord

Gets the coordinates of the current object in (x,y) format

- get_dim

Gets the dimensions of the current object in (h,w) format

### person

#### File: person.py

This class denotes the charcters in the game.

It is the base class for hero and enemy

It inherits from obj.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- constructor

It just calls the constructor of the parent class object.

- move

Moves the hero according to the direction given  
The direction can be given either in wasd or up down left right

### obstacle

#### File: obstacle.py

This class denotes every object on the screen that has been rasterized on the board  
It has no extra features.

It inherits from object.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- Constructor

It just calls the constructor of the parent class object.


### magnet

#### File: magnet.py

This class denotes the magnet that attracts the hero at a rate of one movement per screen go-back.

It inherits from obstacle.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- Constructor

This fixes the shape of the magnet.

Shape:

```less
███████
█░░░░░█
█░░░░░█
█░░░░░█
```

NOTE: TOUCHING THE MAGNET KILLS YOU!

```less
This is a magnet
This is cute
Be like a magnet
Attract the hero
Make him trust you
Betray his trust
Let him die
```




### powerup

#### File: powerUp.py

This class denotes the following power-ups:

- ExtraTime +
- speed-boost A
- extra life +
- snake $

It inherits from obstacle.

#### Additional Data Members

- type

Denotes the type of the powerup

#### Additional/Re-written Member Functions

- Constructor

The obstacle is initialised as a powerup of whatever type you want it to be

- collect

Collect the powerup and make the powerup active

### coins

#### File: coins.py

This class denotes money!! :)  
It looks like this: 0 in yellow

It inherits from obstacle.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- Constructor

It is initialised as an obstacle with 0 as its shape. (well, a coin is never an obstacle right?)

- collect

This is supposed to be called when the coin is collected  
Sadly, noone called it...

### beam

#### File: beam.py

This class denotes the yellow/red laser/fire beams.  
Note that the width of the beam is always one. Also, while defining the beam, we have put some extra space around the beam just for safety reasons (so that I would not print one beam next to the other)

It inherits from obstacle.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- Constructor

Here, an additional parameter, orientation, is passed to the constructor. This parameter determines the overall orientation of the beam  
The beam can be :

- Horizontal (h): -
- Vertical (v): |
- Diagonal 1 (d1): \
- Diagonal 2 (d2): /
Each of these orientations have their own height, width and shape.

Refer to the code for more details.

### hero

#### File: hero.py

This class denotes the Mandalorian who is controlled by the player.  
He is small; he is cute.  
He looks different based on the powerups he is on

It inherits from person class.

#### Additional Data Members

NONE

#### Additional/Re-written Member Functions

- Constructor

Initialises the person with the characteristics of a hero

Style:

```less
[▄
||
```

- print_direct

Checks how high the hero is currently (that is, which all power-ups are active atm)  
Then prints the hero directly onto the screen

- collision_manager

Manages the collision of the hero with the beams, coins, magnet and powerups on the board

- magnet_attraction

Manages the attraction of the hero towards the magnet if the magnet is on the screen

### bullet

#### File: bullet.py

This class denotes the orange-ish color bullets sent by the hero  
It moves foreward at a speed of 2 forward moves per screen go-backs. The hero can never ever shoot backwards

It inherits from obstacle.

#### Additional Data Members

- exist

This variable is 1 if the bullet is already deployed, 0 otherwise

- deployable

This variable is 1 if the bullet can be deployed, that is if the hero wants, he can deploy it; 0 otherwise (if it needs to be reloaded)

#### Additional/Re-written Member Functions

- Constructor

This fixes the shape of the bullet.  
Shape: `≡>`  
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

### enemy

#### File: enemy.py

This class denotes the boss enemy Viserion, the flying dragon  
He is small; he is a tiny squishy squirrel-like dragon; but why did he want to take Baby Yoda?

It inherits from person class. The enemy is also a person, remember that while shooting bullets at him

#### Additional Data Members

- state

Tells which state he is in  
He has three states:

State 0: Normal state 1 where he looks like this

```less
|\_//|   /_(
_/(o)/  /_(
/o_.-. \/__(
__/__/___(
¨-¨-¨-¨-¨
```

State 1: Normal state 2 where he looks like this

```less
|\_//|   /_(
_/(o)/  /_(
/__.-. \/__(
__/__/___(
¨-¨-¨-¨-¨
```

State DEAD: The dragon looks dead in this state

```less
|\_//|   /_(
_/xxx/  /_(
/__.-. \/__(
__/__/___(
¨-¨-¨-¨-¨
```

- ball

Denotes the beautiful ice balls he likes to deploy at the hero  
But since he is dumb, he does not deploy it properly at the hero

#### Additional/Re-written Member Functions

- Constructor

Initialises the person with the characteristics of an enemy and gives it two additional attributes: state and ball

- print_direct

Checks the state of the dragon and prints him accordingly directly onto the screen; also prints his ball (if it exists)

- follow

Make the dragon follow the hero along the x axis

- release_balls

release those balls, filled with ice if it is not already deployed

- move_balls

Moves the balls left

- check_collision

Checks if the hero is colliding with the boss
Decrease the boss health if bullet hits the boss and increase the score by 10 per pain inflicted to the enemy
Also checks if his ball is colliding with anything

### ball

#### File: ice_balls.py

This class denotes the Bullet of the dragon enemy  
Ice ball is an obstacle with the ability to move only backward (the BOSS is backward in both thinking and working)

It inherits from obstacle class.

#### Additional Data Members

- exist

This variable is 1 if the ball has already been deployed by the enemy and is currently on the screen

#### Additional/Re-written Member Functions

- Constructor

Fixes the shape of the ball
Style: █▓▒░·
Makes its existence 0

- check_if_exists

Returns 1 if the ball is already deployed, that is the ball is currenly on the screen

- check_collision

Manages the collision of the ball with the coins and obstacles, and the hero

- move_left

Move the ball left after destroying everything in its path

- deploy(self, x, y):

Deploy the ball

## OTHER FILES

### term.py

Has those functions related to the terminal

- clrscr

Clears the terminal screen

- next_play

Repositions the pointer to the top left corner of the screen for the next game

### global_stuff.py

- DEBUG MODE
- THE PLAYER PERSONAL STUFF
- GAME CONSTANTS
- GAME RELATED GLOBAL VARIABLES
- POWER UP RELATED VARIABLES
- ENEMY STYLES
- STUFF TO BE DONE BEFORE THE START OF THE GAME
- CHECKING IF DEAD VARIABLES

### colored_printing.py

Has the different colors used in the game
Contains the following global function:

#### color_text(text,color)

Colors the text according to the given color
The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
