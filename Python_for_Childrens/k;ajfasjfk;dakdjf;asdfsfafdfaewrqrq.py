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

t = Pen()
t.speed(0)
t.hideturtle()
while True:
    for x in range(35):
        t.circle(x)
        t.forward(5)

        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
    t.left(10)
    for x in range(35):
        t.circle(x)
        t.forward(-5)

        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
    t.left(10)
    for x in range(35):
        t.circle(10)
        t.forward(20)


        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
    t.left(10)
    for x in range(35):
        t.circle(10)
        t.forward(-20)

        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
    t.left(10)