from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import turtle
from turtle import *
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep

s = Screen()
t = Pen()
#t.hideturtle()
t.circle(10)
t.pu()
x,y = t.pos()
t.goto(x-4,y+2)
t.pd()
x,y = t.pos()
t.goto(x+8,y)
x,y = t.pos()
t.goto(x-4,y+9)
x,y = t.pos()
t.goto(x-4,y-9)
t.pu()

t.home()

x,y = t.pos()
t.goto(x-11,y-1)
t.pd()
t.forward(23)
t.left(90)
t.forward(23)
t.left(90)
t.forward(23)
t.left(90)
t.forward(23)
t.left(90)

mainloop()