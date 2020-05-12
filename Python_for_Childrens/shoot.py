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
e = Turtle()
e.pu()
e.setpos(-190,89)
e.shape("circle")
def l():
    t.left(10)
def r():
    t.right(10)
def l2():
    x,y = t.pos()
    t.goto(x-10,y)
def r2():
    x,y = t.pos()
    t.goto(x+10,y)
def u():
    x,y = t.pos()
    t.goto(x,y+10)
def d():
    x,y = t.pos()
    t.goto(x,y-10)

def s():
    t1 = t.clone()
    t1.shape("circle")
    def l3():
        x,y = t1.pos()
        t1.goto(x-10,y)
    def r3():
        x,y = t1.pos()
        t1.goto(x+10,y)
    def u2():
        
        x,y = t1.pos()
        t1.goto(x,y+10)
    def d2():
        x,y = t1.pos()
        t1.goto(x,y-10)
    listen()
    screen.onkeypress(d2,"h")
    screen.onkeypress(l3,"g")
    screen.onkeypress(r3,"j")
    screen.onkeypress(u2,"y")
#    t1.pd()
    t1.speed(1)
    for x in range(60):
        t1.forward(10)
        x,y = e.pos()
        x2,y2 = t1.pos()
        if x == x2 and y == y2:
            print(":")

#    print("vova")
screen.onscreenclick(t.goto)
listen()
screen.onkeypress(s,"o")
screen.onkeypress(l,"Left")
screen.onkeypress(r,"Right")
screen.onkeypress(l2,"a")
screen.onkeypress(r2,"d")
screen.onkeypress(u,"Up")
screen.onkeypress(d,"Down")

mainloop()