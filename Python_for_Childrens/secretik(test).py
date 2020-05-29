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
ert = "circle"
screen = Screen()
tre = 0
tr = 1
rt = 1
t4 = 0
t = Pen()
t.speed(1)
t.pu()
t2 = Turtle()
image = 'tree.gif'
screen.addshape(image)
t2.shape(image)
t3 = Turtle()
image = 'tree.gif'
screen.addshape(image)
t3.shape(image)
t3.penup()
t3.goto(0,-200)
t3.speed(1)

#t2.shape("square")
t2.penup()
t2.goto(0,200)
t2.speed(1)
def f():
    t2.forward(-1)
    t3.forward(-1)
#    t.forward(1)
def b():
    t2.forward(1)
    t3.forward(1)
#    t.forward(1)
listen()
screen.onkey(b,'Left')
screen.onkeypress(b,'Left')
listen()
screen.onkey(f,'Right')
screen.onkeypress(f,'Right')
mainloop()