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
import sys
from PIL import Image
from se import *
q = Screen()
t = Turtle()
t.pu()
t.speed(1)
cm = []
def f():
    cm.append('f')
def b():
    cm.append('b')
def u():
    cm.append('u')
def d():
    cm.append('d')
def cd():
    cm.append('cd')
    
def ru():
    c = len(cm)
    for x in cm:
        if x == 'f':
            t.forward(10)
        elif x == 'b':
            t.forward(-10)
        elif x == 'u':
            x,y = t.pos()
            t.goto(x,y+10)
        elif x == 'd':
            x,y = t.pos()
            t.goto(x,y-10)
        elif x == 'cd':
            
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            t.color(clrname.upper())
        time.sleep(0.1)
    cm.clear()

listen()
q.onkey(f,'Right')
q.onkey(b,'Left')
q.onkey(u,'Up')
q.onkey(d,'Down')
q.onkey(ru,' ')
q.onkey(cd,'p')
mainloop()