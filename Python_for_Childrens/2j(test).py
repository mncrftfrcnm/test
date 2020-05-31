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
def j1():
    global t4,tr
    if tr == 1:
        tr = 0
        t4 = 1
        x,y = t.pos()
        t.goto(x,y+50)
        t.goto(x,y)
        t.shape("classic")
        t4 = 0
        tr = 1
def j2():
    global t4
    if t4 == 1:
        t.shape("circle")
        t4 = 0
        x,y = t.pos()

        t.goto(x,y+40)
        t.goto(x,y)
        t4 = 0
listen()
screen.onkey(j1,'w')
screen.onkey(j2,'q')
mainloop()