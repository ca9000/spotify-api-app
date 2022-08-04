#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.5
#  in conjunction with Tcl version 8.6
#    Aug 04, 2022 04:06:48 PM EEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import SpotifyAPIGuiV2_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+660+210")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("Spotify History")
        top.configure(background="#191414")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#ffffff")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.517, rely=0.222, height=33, width=126)
        self.Button1.configure(activebackground="#ffffff")
        self.Button1.configure(activeforeground="#ffffff")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#191414")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Search''')
        self.Button1.bind('<Button-1>',lambda e:SpotifyAPIGuiV2_support.Past5YearsButton(e))

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.083, rely=0.044, height=56, width=132)
        self.Label1.configure(activebackground="#191414")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#191414")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Insert artist name:''')

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.333, rely=0.067, height=44, relwidth=0.59)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.output = tk.Label(self.top)
        self.output.place(relx=0.083, rely=0.378, height=246, width=502)
        self.output.configure(activebackground="#ffffff")
        self.output.configure(anchor='w')
        self.output.configure(background="#d9d9d9")
        self.output.configure(compound='left')
        self.output.configure(disabledforeground="#a3a3a3")
        self.output.configure(foreground="#000000")

def start_up():
    SpotifyAPIGuiV2_support.main()

if __name__ == '__main__':
    SpotifyAPIGuiV2_support.main()




