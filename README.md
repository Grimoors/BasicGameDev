# Basic Game in Terminal in Python
---
## Basic Details

1. This game is to be run on a device with minimum resolution of 1280x720
2. The terminal that this game is run in is to be fullscreen.
3. This is a very minimal game and should not require much graphical processing power
---
## Concepts of Game Development
### 1. Game Loop
http://gameprogrammingpatterns.com/game-loop.htmlgame-loop-simple.png

[![Game Loop Slide](http://gameprogrammingpatterns.com/images/game-loop-simple.png)](http://gameprogrammingpatterns.com/game-loop.html)

A Game loop has -> 
1. An Input Processing Phase
2. A Game Update Phase
3. A Render Phase

### 2. Coordinate System
While rendering a 2D game -> We use a Coordinate Plane.
The 2D Coordinate System used is initialized as follows : 

http://rbwhitaker.wdfiles.com/local--files/monogame-introduction-to-2d-graphics/2DCoordinateSystem.png

[![Alt text](http://rbwhitaker.wdfiles.com/local--files/monogame-introduction-to-2d-graphics/2DCoordinateSystem.png)](http://rbwhitaker.wikidot.com/introduction-to-2d-graphics)

### 3. Coloring in the Terminal.

#### 4-bit Colours
The standards implementing terminal colours began with limited (4-bit) options. The table below lists the RGB values of the background and foreground colours used for these by a variety of terminal emulators:

https://i.stack.imgur.com/9UVnC.png
[![Table of Colors](https://i.stack.imgur.com/9UVnC.png)](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#:~:text=the%20standards%20implementing%20terminal%20colours%20began%20with%20limited%20(4-bit)%20options.%20the%20table%20below%20lists%20the%20rgb%20values%20of%20the%20background%20and%20foreground%20colours%20used%20for%20these%20by%20a%20variety%20of%20terminal%20emulators%3A)

<!-- [![Alt text](https://assets.digitalocean.com/articles/alligator/boo.svg)](https://digitalocean.com) -->

#### ANSI Escape Sequences in Python and Bash
The ANSI escape sequences we're looking for are the Select Graphic Rendition subset. All of these have the form

```
\033[XXXm
```

Where ``` XXX ``` is a series of semicolon-seperated parameters

To say, make text red, bold, and underlined (we'll discuss many other options below) in Python3 you might write:

```
print("\033[31;1;4mHello\033[0m")
```
and in Bash you'd use
```
echo -e "\033[31;1;4mHello\033[0m"

```
where the first part makes the text red (`31`), bold (`1`), underlined (`4`) and the last part clears all this (`0`).

(Refer to the table in the linked article for all the Properties that can be set.)

It is Simpler for everyone to just use RGB and hence we will use : 
```
\033[38;2;<r>;<g>;<b>m     #Select RGB foreground color
\033[48;2;<r>;<g>;<b>m     #Select RGB background color
``` 

---
## Files and Member Functions

