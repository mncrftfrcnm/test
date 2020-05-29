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
import turtle
from turtle import *
from PIL import Image 

wait_seconds = 1
WinWidth=750

screen = Screen()
t2 = Turtle()
t2.pu()
t = Turtle()
t.pu()
'''c = int(input("choose wearpon: 1)sniper 2)laser"))
if c == 1:
    t.shape("circle")
    screen.onscreenclick(t.goto)
    evil = Turtle()
    evil.pu()
#    evil.goto(-300,-300)
    evil.shape("circle")
    def u():
        x,y = t.pos()
        t.goto(x,y+1)
    def d():
        x,y = t.pos()
        t.goto(x,y-1)
    listen()
    screen.onkey(u,"Up")
    screen.onkey(d,"Down")
    screen.onkeypress(u,"Up")
    screen.onkeypress(d,"Down")
    def r():
    #    global sco
        x,y = t.pos()
        t.goto(x+1,y)
    def l():
        x,y = t.pos()
        t.goto(x-1,y)
    screen.onkey(l,"Left")
    screen.onkey(r,"Right")

    def ata():
        x,y = t.pos()
        x2,y2 = t.pos()
        if x == x or y == y:
            print("you win")
        listen()
        screen.onkey(ata,"w")
        screen.onkeypress(ata,"w")
        
mainloop()'''
tr = 0
sco = 1
ret = 1
def do():
    global tr,sco,ret
    t1 = t.clone()
    t1.shapesize(ret)
    if sco == 0:
        clr = randint(0x0,0xFFFFFF)
    
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t1.color(clrname.upper())
#        sco = 1
    
    if tr == 0:
        t1.shape("square")
    if tr == 1:
        t1.shape(tre)
    # def fl():
    #     t1.left(10)
    # def fr():
    #     t1.left(-10)
    # listen()
    # screen.onkey(fl,"d")
    # screen.onkey(fr,"a")

    
tryo = 20
def u():
    global tryo
    x,y = t.pos()
    t.goto(x,y+tryo)
def d():
    global tryo
    x,y = t.pos()
    t.goto(x,y-tryo)
listen()
screen.onkey(u,"Up")
screen.onkey(d,"Down")
def r():
#    global sco
    global tryo
    x,y = t.pos()
    t.goto(x+tryo,y)
def l():
    global tryo
    x,y = t.pos()
    t.goto(x-tryo,y)
def c():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="duck.ps")
screen.onkey(l,"Left")
screen.onkey(r,"Right")
screen.onkey(do,"=")
screen.onkey(c,"1")
def u2():
    global tryo
    x,y = t2.pos()
    t2.goto(x,y+tryo)
def d2():
    global tryo
    x,y = t2.pos()
    t2.goto(x,y-tryo)
listen()
screen.onkey(u2,"w")
screen.onkey(d2,"s")
def r2():
#    global sco
    global tryo
    x,y = t2.pos()
    t2.goto(x+tryo,y)
def l2():
    global tryo
    x,y = t2.pos()
    t2.goto(x-tryo,y)
def do2():
    global tr,sco,ret
    t3 = t2.clone()
    t3.shapesize(ret)
    if sco == 0:
        clr = randint(0x0,0xFFFFFF)
    
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t1.color(clrname.upper())
#        sco = 1
    
    if tr == 0:
        t3.shape("square")
    if tr == 1:
        t3.shape(tre)
    # def fl2():
    #     t3.left(10)
    # def fr2():
    #     t3.left(-10)
    # listen()
    # screen.onkey(fl2,"d")
    # screen.onkey(fr2,"a")
screen.onkey(l2,"a")
screen.onkey(r2,"d")
screen.onkey(do2,"q")
mainloop() 