import turtle
from turtle import *
screen = Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(900)
t.shapesize(100)
from random import *

from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
wait_seconds = 1
WinWidth=750
y = 900
class beeper(threading.Thread):
    
    def run(self):
        global y
        self.keeprunning = True
        while self.keeprunning:
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')
            t.color(clrname.upper())
            t.pensize(y)
            y = y + 1
beep = beeper()
beep.start()
screen.onscreenclick(t.goto)
#screen.mainloop()
turtle.done()