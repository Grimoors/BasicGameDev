#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://rosettacode.org/wiki/Keyboard_input/Keypress_check

#from __future__ import absolute_import, division, unicode_literals, print_function

import tty
import termios
import sys
import _thread
import time
#from getch import getch

try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def keypress():
    global char
    char = getch()


def main():
    global char
    char = None
    _thread.start_new_thread(keypress, ())

    while True:
        if char is not None:
            print("Key pressed is " + char)
            _thread.start_new_thread(keypress, ())
            if char == 'q':
                exit()
            char = None
        print(".")
        time.sleep(0.5)


if __name__ == "__main__":
    main()
