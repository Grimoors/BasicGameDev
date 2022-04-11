'''
Has the different colors used in the game
Contains the following global function:

color_text(text,color)

Colors the text according to the given color
The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
'''

COLORS = {
    'Normal': '\x1b[40;37m',
    'Bg1': '\x1b[40;37m',
    'Bg2': '\x1b[40;100m',
    'Bg3': '\x1b[40;47m',
    'Top Bar': '\x1b[1;97;44m',
    'Bottom Bar': '\x1b[1;97;44m',
    'Life': '\x1b[31;1;100m',
    'Time': '\x1b[32;1;100m',
    'Progress': '\x1b[1;100m',

    'Hero': '\x1b[1;36;47m',
    'ShieldedHero': '\x1b[1;32;47m',
    'SpeededHero': '\x1b[1;35;47m',
    'SnekHero': '\x1b[0;33;42m',
    'ShieldSnekHero': '\x1b[0;37;42m',
    'Bullet': '\x1b[38;5;208m',

    'Hbeam': '\x1b[1;31;40m',
    'Vbeam': '\x1b[1;31;40m',
    'Dbeam1': '\x1b[1;31;40m',
    'Dbeam2': '\x1b[1;31;40m',

    'Enemy': '\x1b[1;31;40m',
    'Ice Ball': '\x1b[1;36;40m',
    'Fire': '\x1b[1;31;40m',

    'Coin': '\x1b[1;33;40m',
    'ExtraLife': '\x1b[41;1;37m',
    'ExtraTime': '\x1b[46;1;37m',
    'ShieldPU': '\x1b[46;1;37m',
    'SpeedBoost': '\x1b[42;5;37m',
    'Snek': '\x1b[0;37;42m',
    'Magnet': ''
}
END_COLOR = '\033[m'


def color_text(text, color):
    ''' 
    Colors the text according to the given color
    The color can be one of the 'COLORS' in the array 'COLORS' or can be explicitly mentioned using ASCII color codes.
    '''
    if '\x1b' in color:
        return color + text + END_COLOR
    else:
        try:
            return COLORS[color] + text + END_COLOR
        except:
            return text
