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
q = Screen() 
t = Turtle()
t.speed(1)
t.pu()
t2 = Pen()
t2.pu()
t2.hideturtle()
x = randint(-400,400)
y = randint(-400,400)
t2.goto(x,y)
t2.dot()
t2.shape("circle")
t2.forward(100)
def r():
    t.forward(1)
    x,y = t2.pos()
    x2,y2 = t.pos()
    if x == x2 and y == y2:
        t2.showturtle()
        time.sleep(0.1)
        t2.hideturtle()
        t.hideturtle()
def l():
    t.forward(-1)
    x,y = t2.pos()
    x2,y2 = t.pos()
    if x == x2 and y == y2:
        t2.showturtle()
        time.sleep(0.1)
        t2.hideturtle()
        t.hideturtle()
def u():
    x2,y2 = t.pos()
    t.goto(x2,y2+1)
    x,y = t2.pos()
    x2,y2 = t.pos()
    if x == x2 and y == y2:
        t2.showturtle()
        time.sleep(0.1)
        t2.hideturtle()
        t.hideturtle()
def d():
    x2,y2 = t.pos()
    t.goto(x2,y2-1)
    x,y = t2.pos()
    x2,y2 = t.pos()
    if x == x2 and y == y2:
        t2.showturtle()
        time.sleep(0.1)
        t2.hideturtle()
        t.hideturtle()
listen()
q.onkey(r,'Right')
q.onkeypress(r,'Right')
q.onkey(l,'Left')
q.onkeypress(l,'Left')
q.onkey(u,'Up')
q.onkeypress(u,'Up')
q.onkey(d,'Down')
q.onkeypress(d,'Down')

mainloop()