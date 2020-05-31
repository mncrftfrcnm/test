
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
screen = Screen()
t = Turtle()
t.pu()
y = 1
t2 = Turtle()
t2.pu()
t2.goto(300,300)
t3 = Turtle()
t3.pu()
t3.goto(0,300)

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            x2,y2 = t2.pos()
            x3,y3 = t3.pos()
            if x == x2 and y == y2:
                y = y + 1
#dddsjdlwksjfc                 t.shapesize(y)
                t2.color("white")
                t2.goto(6000,6000)
            if x == x3 and y == y3:
                y = y + 1
#                t.shapesize(y)
                t3.color("white")
                t3.goto(6000,6000)
beep = beeper()
beep.start()                                
screen.onscreenclick(t.goto)
def u1():
    x,y = t.pos()
    t.goto(x,y+10)
def u2():
    x2,y2 = t2.pos()
    t2.goto(x2,y2+10)
def d1():
    x,y = t.pos()
    t.goto(x,y-10)
def d2():
    x2,y2 = t2.pos()
    t2.goto(x2,y2-10)
def do():
    x2,y2 = t2.pos()
    x,y = t.pos() 
    if x == x2:
        print("1p.win")
def do2():
    x2,y2 = t2.pos()
    x,y = t.pos() 
    if y == y2:
        print("2p.win")
    if x == x2:
        print("2p.win")
def l1():
    x,y = t.pos()
    t.goto(x-10,y)
def l2():
    x2,y2 = t2.pos()
    t2.goto(x2-10,y2)
def r1():
    x,y = t.pos()
    t.goto(x+10,y)
def r2():
    x2,y2 = t2.pos()
    t2.goto(x2+10,y2)
listen()
screen.onkey(u1, "Up")
screen.onkey(d1, "Down")
screen.onkey(l1, "Left")
screen.onkey(r1, "Right")

mainloop()



























