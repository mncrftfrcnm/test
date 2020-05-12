
from turtle import *
import turtle
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
screen = Screen()
head = turtle.Turtle()
head.speed(1)
tr = 0
head.pu()
#s = ["turtle","circle","arrow","square","triangle"]
head.color("white")
head.setpos(0,-300)
head.color("black")
t = Turtle()
c = 0
#Screen = turtle.Screen()

def up():
    global c
    if c == 0:
        x,y = head.pos()
        head.goto(x,y+30)
        x,y = head.pos()
        head.goto(x,y-30)
listen()
screen.onkey(up,"Up")
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            
            t.pu()
            t.goto(400,-300)

            t.goto(-500,-300)
            x,y = head.pos()
            x2,y2 = t.pos()
            t.goto(0,0)            
beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = head.pos()
            x2,y2 = t.pos()
            if x == x2 and y == y2:
                print("game over")
            x,y = head.pos()
            x2,y2 = t.pos()
            if x2 == x and y2 == y :
                print("game over")
                        
beep2  = beeper2()
beep2.start()

mainloop()
#class beeper3(threading.Thread):
#    def run(self):
