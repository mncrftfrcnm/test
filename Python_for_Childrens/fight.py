from tkinter import*
from random import *
import turtle
import turtledemo.planet_and_moon
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
yty = 0
tre = ["turtle","circle","classic","arrow"]
t3 = Turtle()
t3.pu()
t3.goto(300,300)
t = Turtle()

t.shape(choice(tre))

t2 = Turtle()
t2.shape(choice(tre))
t.pu()
t2.pu()
t.goto(100,100)
t.speed(1)
t2.speed(1)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning1 = True
        while self.keeprunning1:
            h,j = t3.pos()
            x,y = t.pos()
            x2,y2 = t2.pos()
            if x == h and y == j:
                screen.onscreenclick(t.goto)
            if x2 == h and y2 == j:
                screen.onscreenclick(t2.goto)
beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while True:
            while self.keeprunning == True:
                h,j = t3.pos()
                x,y = t.pos()
                x2,y2 = t2.pos()
                if x == x2 and y2 == y:
                    print("Draw")
beep2  = beeper2()
beep2.start()
class beeper3(threading.Thread):
    def run(self):
        self.keeprunning2 = True
        while self.keeprunning2:
            h,j = t3.pos()
            x,y = t.pos()
            x2,y2 = t2.pos()
            if x == x2 and y == y2:
                print("2p.win")
            if x2 == x and y2 == y:
                print("2p.win")

beep3  = beeper3()
beep3.start()
beep3.keeprunning2 = False
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
    if x == x2 or y == y2:
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
def sr():
    beep3.keeprunning2 = True
    x2,y2 = t2.pos()
    t2.speed(0)
    
    beep2.keeprunning = False
    
    t2.goto(x2+30,y2)
#    beep3._stop()

    beep2.keeprunning = True
    beep3.keeprunning2 = False
    t2.speed(1)
listen()
screen.onkey(u2, "w")
screen.onkey(u1, "Up")
screen.onkey(d1, "Down")
screen.onkey(d2, "s")
screen.onkey(do, "l")
screen.onkey(do2, "e")
screen.onkey(l1, "Left")
screen.onkey(l2, "a")
screen.onkey(r1, "Right")
screen.onkey(r2, "d")

screen.onkey(sr, "q")
#yt = input("""""""""""")
mainloop()

