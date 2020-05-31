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
import teleport
import all_my_commands
e = 0
x = 0
screen = Screen()
t = Pen()
t.pu()
t.right(90)
t.shape("square")
def uo():
    t.forward(1)

def do():
    t.forward(-1)
def le():
    x,y = t.pos()
    t.goto(x+1,y)

def ri():
    x,y = t.pos()
    t.goto(x-1,y)

def ata():
    t1 = t.clone()
    t1.shape("classic")
    while True:
        x,y = t1.pos()
        if y < -600:
            break
        t1.forward(1)

listen()
screen.onkey(uo,"Up")
screen.onkey(do,"Down")
screen.onkey(le,"Left")
screen.onkey(ri,"Right")
screen.onkey(ata,"w")
screen.onkeypress(uo,"Up")
screen.onkeypress(do,"Down")
screen.onkeypress(le,"Left")
screen.onkeypress(ri,"Right")
mainloop()