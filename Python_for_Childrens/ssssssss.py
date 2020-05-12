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
screen = turtle.Screen()
t = Turtle()
t.right(90)
t.hideturtle()
t.pu()
while True:
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    p = randint(1,11)
    t.pensize(p)
    t.color(clrname.upper())
    x = randint(-300,300)
    y = randint(-300,300)
    t.goto(x,y)
    ret = randint(10,100)
    t.pd()
    x,y = t.pos()
    t.goto(x+ret,y+ret*2)

    t.left(90)
    t.forward(ret/2)
    t.right(90)
    t.forward(ret)
    t.pu()
