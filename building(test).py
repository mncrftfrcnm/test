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

screen =  Screen()
y = 1

def dob():
#    t = y
#    print(t)
    t = Turtle()
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

    print(t)
    t.shape("square")
    t.shapesize(4)
    t.pu()
    t.ondrag(t.goto)
#    y = y+1
listen()
screen.onkey(dob,'w')    
mainloop()