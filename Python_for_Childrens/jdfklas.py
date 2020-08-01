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
t.speed(0)
t.pu()
t2 = Turtle()
t2.speed(0)
t2.pu()
t3 = Turtle()
t3.speed(0)
t3.pu()
t4 = Turtle()
t4.speed(0)
t4.pu()
t4.shape('square')
t3.shape('square')
t2.shape('square')
t2.forward(100)
t3.forward(100)
t4.forward(100)
x,y = t3.pos()
t3.goto(x,y+20)
x,y = t4.pos()
t4.goto(x,y+40)

def h():
    t2.ht()
    time.sleep(0.1)
    t3.ht()
    time.sleep(0.1)
    t4.ht()
    time.sleep(0.1)
    t4.st()
    time.sleep(0.1)
    t3.st()
    time.sleep(0.1)
    t2.st()
    time.sleep(0.1)
listen()
q.onkey(h,'w')
mainloop()