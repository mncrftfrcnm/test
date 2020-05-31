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
t = Turtle()
def c():
    tre = int(input("input radius of circle"))
    t.circle(tre)
def u():
    x,y = t.pos()
    t.goto(x,y + 10)
def d():
    x,y = t.pos()
    t.goto(x,y - 10)
def l():
    x,y = t.pos()
    t.goto(x-10,y)
def r():
    x,y = t.pos()
    t.goto(x+10,y)
def c2():
    ts = t.getscreen()
    ts.getcanvas().postscript(file="duck.ps")
screen.onkey(c2,"s")
listen()
screen.onkey(c,"c")
screen.onkey(u,"Up")
screen.onkey(d,"Down")
screen.onkey(l,"Left")
screen.onkey(r,"Right")
screen.onkeypress(u,"Up")
screen.onkeypress(d,"Down")
screen.onkeypress(l,"Left")
screen.onkeypress(r,"Right")
while True:
    t.begin_fill()
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    t.fillcolor(clrname)
    t.color(clrname.upper())
    screen.onscreenclick(t.end_fill())
#    hg = input("do this?:")
    
mainloop()