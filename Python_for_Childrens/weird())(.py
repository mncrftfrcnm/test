from tkinter import*
from random import *
import turtle

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
from turtle import *
from turtle import *
import turtle
screen = Screen()

t = Turtle()
#t.shape("turtle")
#t.pu() 
t.speed(0)
er = Turtle()
er.pu()
er.st()
er.speed(0)
screen.onscreenclick(t.goto)
t.ondrag(t.goto)
ret = 1
def du(x,y):
    t1 = er.clone()
    t1.goto(x,y)
    t1.shape('square')
def du2(x,y):

    t1 = er.clone()
    t1.goto(x,y)
    f,g = t1.pos()
    t1.goto(f,g+10)
    t1.shape('square')
    t1 = er.clone()
    t1.goto(x,y)
    f,g = t1.pos()
    t1.goto(f,g+20)
    t1.shape('square')
    t1 = er.clone()
    t1.left(90)
    t1.goto(x,y)
    f,g = t1.pos()
    t1.goto(f,g+35)
    t1.shape('triangle')
def fl(x,y):
    global ret
    if ret == 1:
        t.begin_fill()
        d = 0
    if ret == 0:
        t.end_fill()
        d = 1
    ret = d
screen.onscreenclick(er.goto,btn=3)
t.onclick(fl)
er.ondrag(du,btn=3)
screen.onscreenclick(er.goto,btn=2)
er.onclick(du2,btn=2)
mainloop()