'''
Has the different colors used in the game
Contains the following global function:

color_text(text,color)

Colors the text according to the given color
The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
'''
COLORS = {
    'Bg1': '\x1b[48;2;0;0;0m',
    'Bg2': '\x1b[48:2:128;128;128m',
    'Bg3': '\x1b[48:2:m',
    'Top Bar': '\x1b[48:2:47;79;79m',
    'Bottom Bar': '\x1b[48:2:47;79;79m',
    'Life': '\x1b[48:2:m',
    'Time': '\x1b[48:2:m',
    'Progress': '\x1b[48:2:m',
}
END_COLOR = "\033[0m"