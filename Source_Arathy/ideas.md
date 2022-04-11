# IDEAS ON IMPLEMENTING THIS

## GLOBAL VARIABLES

- lives
- score
- time left
- power-ups active
- speed of the game

## CLASSES

### 1. PERSON

This is a base class for the charcters in the game  

He has the following attributes:

- x position on the screen
- y position on the screen
- height
- width
- character for filling him/her/it

and the following functions:

- initialize itself
- render itself to the screen
- kill itself

### 2. PLAYER

Denotes the Mandalorian who is controlled by the player.

He inherits from `PERSON` and has the following attributes:

- bullets

and the following functions:

- move left
- move right
- move up
- move down
- gravity
- Shoot bullets
- be attracted by the magnet

### 3. SHIELDED PLAYER

He inherits from `PLAYER` and has the following extra functions:

- remove shield

### 3. BOSS

Denotes the boss enemy Viserion, the flying dragon

He inherits from `PERSON` and has the following attributes:

- ice balls
- lives

and the following functions:

- throw ice balls
- follow along y axis
- die

### 4. OBSTACLES

A base class that denotes all the possible obstacles in the game

It has the following attributes

- length
- width
- x position
- y position
- shape

and the following functions:

- Display it

### 5. FIRE BEAMS

Denotes the large yellow laser/fire beams

It inherits from OBSTACLES and has the following attributes:

- length
- orientation

and has the following functions

- check if it is colliding with the player
- be destroyed

### 6. MAGNET

Denotes a magnet that can appear out of nowhere and attract the player

It inherits from OBSTACLES and has the following attributes

- length
- width
- force of attraction
- is on screen

and the following functions

- attract the player
- be destroyed

### 7. COINS

Denotes moneyy!

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like

and the following functions

- be collected
- display it

### 8. POWER-UPs

Denotes power-ups: shield ░ and speed-boost A and extra life +

It inherits from OBSTACLES and has the following attributes

- value
- how it looks like
- type of the power-up
- time for which it stays active

and the following functions

- be collected
- display it

### 9. SCENE

Creates the background beautiful stuff :)

It has the following attributes

- width
- height
- scene start index

and the following functions

- create env effects (like a beautiful background filled with trees)
- create random obstacles
- create random enemies
- create coins
- create powerups

## FEATURES

(to be built later)

## THINGS DONE

- [x] Collision with beams
- [x] globalize the speed of the game
- [x] bullets
- [x] destroy beams
- [x] display the life remaining
- [x] display the time remaining
- [x] make life red in color with white bg
- [x] make time left green in color with white bg
- [x] bullets (again)
- [x] make the hero white backgrounded with cyan trim color
- [x] limited and displayed the number of bullets
- [x] power-up obstacle declaration
- [x] power-up def
- [x] power-up colors
- [x] display the powerups active
- [x] power-ups
- [x] Death by magnet
- [x] Death by no lives
- [x] Death by time out
- [x] Display the coins collected
- [x] Display the level progress
- [x] globalize the total number of screens in game
- [x] change color of the beams to something acceptable
- [x] Print the number of lives of the boss
- [x] magnet make attract hero
- [x] main boss guy
- [x] rewrite the obstacle generation thingy
- [x] Adjust the game duration
- [x] decrease the length of the game to 5
- [x] Make the duration of the game according to the speed of left movement of the game screen
- [x] Make the boss come later in game

## NOTE

All powerups are single tiled with a symbol denoting it (similar to a coin)

## WALKTHROUGH STEPS

1. Make the gameboard
2. Make the character
3. Make the character moving
4. Make the fullboard
5. Make the board move in the background
6. Define gravity
7. Define coins
8. Make the character collect coins
9. Display the coins collected
10. Define beams
11. Make the character lose life on touching the beam
12. Define a life bar below
13. Define a time left below
14. Define bullets
15. Make the character fire bullets
16. Make the bullets destroy everything on path
17. Make the bullets collect coins
18. Put an upper limit to the number of bullets fired
19. Put a restore after some time effect to bullets
20. Define powerups
21. Make the character collect powerups
22. Globalize the speed of the game, the length of the game

## Discussion regarding the length of the game

The length of the game is now 10 minutes. (It isn't a short game, so TA be warned)
The following calculations were done to reach the above claim:

```less
For each move left screen transition, time taken = 0.5 s
So, time taken for an entire screen transition = 0.5 * screen_length = 0.5 * 200 = 100 s = 1 min 40 sec
Number of screens permissable for a 10 min game = 10 * 60 / 100 = 6 screens
The game gets over within 5 screens (time taken is 100 s * 5 = 500 s = 8 min 20 seconds)
The remaining time is used to kill the boss enemy.
Even as the enemy comes, the screen would continue to move front
The enemy should be killed within a minute or less; that's where your skill lies
```

## PLAN OF PLACING THE OBSTACLES AND POWER-UPS

In each case, `placing if permissible` means that, if we place the item, if it collides, we would retry placing it, till 100 attempts have been made and then give up

| Type of obstacle | Shape                                                                                    | Location | Frequency                             |
| ---------------- | ---------------------------------------------------------------------------------------- | -------- | ------------------------------------- |
| Coins            | Rectangle with dimensions random(2,7)xrandom(10,30)                                      | (0,9)    | 2 on the first screen, 4 per screen   |
| Horizontal Beam  | Rectangle with dimensions (2 x safe_region+1) x (length_of_beam + 2 x safe_region)       | (0.5,5)  | 2 per screen (placing if permissible) |
| Vertical Beam    | Rectangle with dimensions ( (length_of_beam / 2) + 2 x safe_region ) x 2 * safe_region ) | (0.5,5)  | 2 per screen (placing if permissible) |
| Diagonal Beam 1  | Square with dimensions ( ( length_of_beam / 1.5) + 2 x safe_region)                      | (0.5,5)  | 2 per screen (placing if permissible) |
| Diagonal Beam 2  | Square with dimensions ( ( length_of_beam / 1.5) + 2 x safe_region)                      | (0.5,5)  | 2 per screen (placing if permissible) |
| Extra Life PU    | Square with dimension 1                                                                  | (1,9)    | 1 per screen                          |
| Speed up PU      | Square with dimension 1                                                                  | (0,5)    | 1 per screen                          |
| Snake PU         | Square with dimension 1                                                                  | (.5,1.5) | 1 per screen                          |
| Shield PU        | Square with dimension 1                                                                  | (0,5)    | 2 per screen                          |
| Magnet           | Square with dimension 7                                                                  | 3        | 1                                     |

## DURATION OF EACH POWER-UP IN TERMS OF NUMBER OF SCREEN PASSES

- Only one Speed Up can be active at a time; if collected more than once, there is no effect
- Only one Shield Up can be active at a time; if collected more than once, there is no effect; i.e. no stacking of shields
- Care should be taken that the snake does not reach the main boss at any time (won't it be complicated that way?)

| Power-up type | Duration          |
| ------------- | ----------------- |
| Extra life    | NA                |
| Speed up      | 50 screen passes  |
| Snake         | 50 screen passes  |
| Shield        | 100 screen passes |

## WAYS FOR THE GAME TO GET OVER

1. Get hit by a magnet
2. Get hit by beams more than 10 times without getting any extra lives; (also known as kys; come on the game isn't that difficult)
3. Get hit by the boss directly (seriously why do you want to `touch` him?)

## SPECIAL ABILITY OF THE BULLETS

The bullets fired by your Mandalorian has a special ability to continue existing even if it hits the dragon. That is it would continue torturing the dragon after hitting him, thus killing him eventually.

## PRIVATISING THINGS

- [x] beam.py
- [x] bullet.py
- [x] coins.py
- [x] colored_printing.py
- [x] enemy.py
- [x] full_board.py
- [x] gameboard.py
- [x] global_stuff.py
- [x] hero.py
- [x] ice_balls.py
- [x] inputs.py
- [x] magnet.py
- [x] main.py
- [x] obj.py
- [x] obstacle.py
- [x] person.py
- [x] powerUp.py
- [x] term.py

## THINGS LEFT TO DO

- [ ] SNAKE POWERUP
- [x] Correct the shield powerup
- [x] Add an extra powerup called extra time that gives a time of move_left*screenlength/2
- [x] Modify the shield mode of the hero (create another class deriving from it that makes it look beautiful)
- [ ] Create another class called snake that derives from the hero class
- [ ] Make the snake look cute
- [ ] Add random people

## MAJOR UPDATE

So here is the plan of exexution:
Just make the left shifting into the counter type execution:
Each count denotes one frame time (0.05 s) [ Rather than the left shift time ]

- SO COUNT THE NUMBER OF COUNTS
- IF THE NUMBER OF COUNTS MOD TO_SHIFT_SCREEN IS ZERO, LEFT SHIFT

```less
for the time out check,

MAXIMUM_NO = TOTAL_TIME / FRAME_TIME
REMAINING_NO = MAXIMUM_NO - COUNTS

for moving the screen left,
TO_SHIFT_SCREEN = TO_SHIFT_SCREEN_TIME / FRAME_TIME

for checking the powerups,
MAX_SHIELD_ACTIVE = MAX_SHIELD_ACTIVE_TIME / FRAME_TIME
MAX_SHIELD_COOLDOWN = MAX_SHIELD_COOLDOWN_TIME / FRAME_TIME
MAX_SPEED_ACTIVE = MAX_SPEED_ACTIVE_TIME / FRAME_TIME
```

- HERE THE FRAME TIME IS 0.05 i.e. 20 FPS

This update is evolutionary as it removes the need of checking time anywhere in the program.  
Also, gravity can be implemeneted in a good way.

### IMPLEMENTING GRAVITY

- IDK
- ok let me think better
- if it is falling down, say that it is falling down
- make a global variable for that purpose
- once he touches the ground, make the variable 0
- otherwise, the variable contains the no_of_frames for which it is falling down

## TODO

- [ ] Difficulty levels
- [ ] Above mentioned stuff
- [x] Added global variables
