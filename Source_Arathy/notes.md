# NOTES

## CLEARING THE TERMINAL SCREEN

### os.system(cmd)

Executes the command mentioned

### os.system('tput reset')

Basically clear all, reset the terminal and do not display the prompt  

## PUTTING COLOR

Color can be put using the following:

```py
from colorama import init
from termcolor import colored
print(colored('Hello, World!', 'green', 'on_red'))
```

### DOC on `colored`

#### Available text colors

red, green, yellow, blue, magenta, cyan, white.

#### Available text highlights

on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

#### Available attributes

bold, dark, underline, blink, reverse, concealed.

#### Example

colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])

### IF COLORED IS NOT ALLOWED TO BE USED, THEN USE THE FOLLOWING

```py
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text') # to set foreground RED
print(Back.GREEN + 'and with a green background') # To set background green
print(Style.DIM + 'and in dim text') # to put some style
print(Style.RESET_ALL) # reset all changes
```

## WELL I REFERRED THE FOLLOWING SITE: <https://github.com/shiena/ansicolor> for colors

## FOR CLEARING THE SCREEN USE

- <http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x361.htm>
- <https://rosettacode.org/wiki/Terminal_control/Cursor_positioning#Python>

## FOR TAKING INPUT USE <https://rosettacode.org/wiki/Keyboard_input/Keypress_check>

## PADDING ZEROS: <https://stackoverflow.com/questions/339007/how-to-pad-zeroes-to-a-string>
