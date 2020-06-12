from turtle import *
from random import *
screen = Screen()
t=Pen()

t.speed(1)
t.shape("square")
t.pu()
t.goto(-400,0)
t3=Pen()
t3.speed(1)
t3.shape("square")
t3.pu()
w = 2
t3.forward(400)
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
def ata():
    global w
    t1 = t.clone()
    t1.forward(800)
    t1.hideturtle()
    t1 = t3.clone()
    t1.shapesize(w/2)
    t2 = t3.clone()
    t2.shapesize(w/2)
    t1.forward(w*10)
    t2.forward(-w*10)
    t3.hideturtle()
    t1.forward(-w*10)
    t2.forward(w*10)
    t3.shapesize(w)
    t3.showturtle()
    t1.hideturtle()
    t2.hideturtle()
    w = w*2
listen()
screen.onkey(ata,'w')
mainloop()
