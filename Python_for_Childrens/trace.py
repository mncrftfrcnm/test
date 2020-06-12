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
t2 = Turtle()
t.pu()
t2.pu()
x,y = t2.pos()
t2.goto(x,y+10)
ui = 0
def f1():
    global ui
    if ui is 0:
     #   t.forward(1)
    
        t.forward(1)
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())

        x,y = t.pos()
        if x > 50:
            print('1 p.win')
            ui = 1
def f2():
    global ui
    if ui is 0:
     #   t.forward(1)
    
        t2.forward(1)
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t2.color(clrname.upper())

        x,y = t2.pos()
        if x > 50:
            print('2 p.win')
            ui = 1
listen()
q.onkey(f1,'Right')
q.onkey(f2,'d')
mainloop()