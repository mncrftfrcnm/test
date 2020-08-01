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
q = Screen()
t = Turtle()
t.pu()
t.speed(0)
t.goto(500,0)
t2 = Turtle()
t2.pu()
t2.speed(0)
t2.color('white')
t2.forward(-200)
t3 = Turtle()
t3.pu()
t3.speed(0)
t3.color('white')
t3.goto(-300,300)
def f():
    t.forward(-1)
    tre = t.distance(t2)
    if tre <= 10:
        for a in range(30):
            x,y = t.pos()
            t.goto(x,y - 1)

        t.goto(500,0)
    x,y = t.pos()
    x2,y2 = t3.pos()
    if x == x2:
        t2.goto(x,y)
listen()
q.onkey(f,'Left')
q.onkeypress(f,'Left')

mainloop()
