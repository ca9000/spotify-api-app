#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 04, 2022 04:07:04 PM EEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import SpotifyAPIGuiV2
import spotify_api

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = SpotifyAPIGuiV2.Toplevel1(_top1)
    root.mainloop()

def Past5YearsButton(*args):
    _w1.output.configure(text="Hello")

if __name__ == '__main__':
    SpotifyAPIGuiV2.start_up()




