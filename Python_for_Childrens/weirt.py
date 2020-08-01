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
ph = 100
ch = 100
ret = input('what item do you wanna: gun or hammer: ')
if ret == 'gun':
    tr = 1
if ret == 'hammer':
    tr = 0
ret2 = input('what wheel do you wanna: faster or +health: ')
if ret2 == 'faster':
    r = 1
if ret2 == '+health':
    r = 0
    ph = ph+50
print(ph,'item-',ret,'health-',ph)
#ert = "circle"
screen = Screen()
tre = 0
rt = 1
t4 = 0
t = Pen()
t.speed(1)
t.pu()
t.shape('square')
t2 = t.clone()
if tr == 1:

    t2.shape('triangle')
if tr == 0:

    t2.shape('turtle')
t2.forward(10)
t3 = t.clone()
if r == 1:
    t3.shape('circle')
    t3.shapesize(3)
    x,y = t3.pos()
    t3.goto(x,y-40)
if r == 0:
    t3.shape('circle')
    t3.shapesize(1)
    x,y = t3.pos()
    t3.goto(x,y-10)
def f():
    global r
   # print(r)
    t3.right(10)
    if r == 1:
        x,y = t3.pos()
        t3.goto(x+10,y)
        x,y = t2.pos()
        t2.goto(x+10,y)
        x,y = t.pos()
        t.goto(x+10,y)
    if r == 0:
        x,y = t3.pos()
        t3.goto(x+1,y)
        x,y = t2.pos()
        t2.goto(x+1,y)
        x,y = t.pos()
        t.goto(x+1,y)
listen()
screen.onkey(f,'Right')
screen.onkeypress(f,'Right')

mainloop()