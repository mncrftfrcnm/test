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
t.speed(0)
t.pu()
t4 = Pen()
t4.speed(0)
t4.shape("square")
t4.penup()
t4.goto(0,200)
t4.ht()
t4.color('yellow')
t3 = Pen()
t3.speed(0)
t3.shape("square")
t3.penup()
t3.color('white')
t3.forward(-500)
f = Pen()
f.speed(0)
f.shape("circle")
f.penup()
f.forward(600)
f.color('white')
t2 = Pen()
t2.speed(0)
t2.shape("square")
t2.penup()
t2.goto(800,200)
t2.speed(1)
yt9 = 1
def aa(x,y):
    global yt9
    if yt9 == 0:
        Screen().bgcolor("black")
        t2.color('white')
        t9y = 1
    if yt9 == 1:
        Screen().bgcolor("white")
        t2.color("black")
        t.color('black')
        t9y = 0
    yt9 = t9y
def f2():
    t2.forward(-1)
    t3.forward(-1)
    f.forward(-1)
    iuu = t.distance(f)
    if iuu <= 10:
        t.color('white')
        t.shape('circle')
        t.shapesize(3)
#    t.forward(1)
def b():
    t2.forward(1)
    t3.forward(-1)
    f.forward(1)
    iuu = t.distance(f)
    if iuu <= 10:
        t.color('white')
        t.shape('circle')
        t.shapesize(3)
def u():
    x,y = t2.pos()
    t2.goto(x,y-1)
    x,y = t3.pos()
    t3.goto(x,y-1)
    x,y = t2.pos()
    t4.goto(x,y-1)
    x,y = f.pos()
    f.goto(x,y-1)
    iuu = t.distance(f)
    if iuu <= 10:
        t.color('white')
        t.shape('circle')
        t.shapesize(3)
def d():
    x,y = t2.pos()
    t2.goto(x,y+1)
    x,y = t3.pos()
    t3.goto(x,y+1)
    x,y = t2.pos()
    t4.goto(x,y+1)
    x,y = f.pos()
    f.goto(x,y+1)
    iuu = t.distance(f)
    if iuu <= 10:
        t.color('white')
        t.shape('circle')
        t.shapesize(3)
def aa2(x,y):
   t4.st() 
def aa3(x,y):
    print('you win')
#    t.forward(1)
listen()
screen.onkey(b,'Left')
screen.onkeypress(b,'Left')
listen()
screen.onkey(f2,'Right')
screen.onkeypress(f2,'Right')
screen.onkey(u,'Up')
screen.onkeypress(u,'Up')
listen()
screen.onkey(d,'Down')
screen.onkeypress(d,'Down')
t2.onclick(aa)
t3.onclick(aa2)
t4.onclick(aa3)
mainloop()