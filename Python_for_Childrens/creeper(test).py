from turtle import *
screen = Screen()
t = Pen()
t.pu()
screen.onscreenclick(t.goto)          
t.speed(0)
t2 = Turtle()
t2.pu()
t2.forward(-100)
from tkinter import *
from random import *
import tkinter.messagebox
import time
import random                                                                                                                                              
import winsound
from turtle import *
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
wait_seconds = 1
WinWidth=750

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            t2.goto(x,y)
            
beep  = beeper()
beep.start()

class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            x2,y2 = t2.pos()
            if x == x2 and y == y2:
                t.hideturtle()
                t2.hideturtle()
            
beep2  = beeper2()
beep2.start()
mainloop()