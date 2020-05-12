from tkinter import*
from random import *
import turtle

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
from turtle import *
screen = turtle.Screen()
t = Turtle()
t.pu()
t1 = t.clone()
t1.goto(60,0)
t1.pu()
t1.speed(1)
def u():
    x,y = t1.pos()
    t1.goto(x,y+10)
def d():
    x,y = t1.pos()
    t1.goto(x,y-10)
def r():
    x,y = t1.pos()
    t1.goto(x+10,y)
def l():
    x,y = t1.pos()
    t1.goto(x-10,y)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            x2,y2 = t1.pos()
            if x == x2 and y == y2:
                print("game over")
            
beep  = beeper()
beep.start()
ty = 0
def u2():
    x,y = t.pos()
    t.goto(x,y+10)
def d2():
    x,y = t.pos()
    t1.goto(x,y-10)
def r2():
    x,y = t.pos()
    t.goto(x+10,y)
def l2():
    x,y = t.pos()
    t.goto(x-10,y)

class beeper2(threading.Thread):
    def run(self):
        global ty
        
        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            ty = ty + 1
            if ty > 50:
                print("hurry up")
                t1.speed(10)

            
beep2  = beeper2()
beep2.start()

listen()
screen.onkey(u, "Up")
screen.onkey(d, "Down")
screen.onkey(l, "Left")
screen.onkey(r, "Right")

class beeper3(threading.Thread):
    def run(self):
        global ty
        self.keeprunning = True
        while self.keeprunning:
            
            screen.onkey(u2, "w")
            screen.onkey(d2, "s")
            screen.onkey(l2, "a")
            screen.onkey(r2, "d")
            
beep3  = beeper3()
beep3.start()

#screen.onkey(c, "w")
screen.onscreenclick(t.goto)
mainloop()