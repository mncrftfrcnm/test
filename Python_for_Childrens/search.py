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
q = Screen()
t = Turtle()
rt = ['square','circle','classic']
yt = choice(rt)
t.shape(yt)
print("found the yellow",yt)
t.color('yellow')
t.shapesize(1.01)
t.pu()
t.speed(0)
u = randint(-450,450)
v = randint(-450,450)
t.goto(u,v)
def yw(x,y):
    print("you win")
t.onclick(yw)
for x in range(600):
    t1 = Turtle()
    t1.shape(choice(rt))
    t1.pu()
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t1.color(clrname.upper())

    t1.speed(0)
    u = randint(-450,450)
    v = randint(-450,450)
    t1.goto(u,v)
mainloop()
