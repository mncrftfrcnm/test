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
from turtle import *
import turtle
screen = Screen()

t = Turtle()
t.shape("turtle")
t.pu() 
t.speed(1)
#t.write(ret)
screen.onscreenclick(t.goto)

def dr():
    ter = randint(0,1)
    if ter == 0:
        t.write("vova")
    if ter == 1:
        t.pd()
        x2,y2 = t.pos()
        x,y = t.pos()
        t.goto(x,y+30)
        x,y = t.pos()
        t.goto(x+30,y)
        x,y = t.pos()
        t.goto(x,y-30)
        x,y = t.pos()
        t.goto(x-30,y)
        t.pu()
listen()
screen.onkey(dr,"w")
screen.mainloop()        