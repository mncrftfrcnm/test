from turtle import *

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
y = 100

screen = Screen()
t = Pen()
t.speed(0)
t.ondrag(t.goto)
#t.ondrag(t.dot)
t.onclick(t.write)
#t.onclick(t.shapesize)

def u():
    t.pu()
def d():
    t.pd()
listen()
screen.onkey(u,'Up')
screen.onkey(d,'Down')
#def u():
#    t.goto()
#t.onrelease(u)
screen.onscreenclick(t.goto)
while True:
# #    screen.setup(y,y)
#     x,y = t.pos()
#     if x > y:
#         print("O")
#         y = y + 10000000000000000000000000000000000
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())
#     tre = randint(1,20)
# #    t.pensize(tre)
mainloop()