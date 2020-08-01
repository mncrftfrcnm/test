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
import sys
#from PIL import Image
q = Screen()
t = Turtle()
t.speed(0)
t.pu()
f = 0
e = Turtle()
e.speed(0)
e.pu()
e.forward(100)
#e.right(080)
def cd():
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    e.color(clrname.upper())
def j():
    e.speed(0)
    t.speed(0)
    e.right(-45)
    t.right(-45)
    e.speed(0)
    t.speed(0)
    e.forward(00)
    t.forward(00)
    e.speed(0)
    t.speed(0)
    e.right(90)
    t.right(90)
    e.speed(0)
    t.speed(0)
    e.forward(00)
    t.forward(00)
    t.right(-45)
    e.right(-45)
listen()
q.onkey(j,'Up')
q.onkey(cd,'i')
q.onkeypress(cd,'i')
while True:
    
    e.forward(1) 
    x,y = e.pos()
    if x >=500:
        e.goto(-x,y)        
    t.forward(1)
    x,y = t.pos()
    if x >=500:
        t.goto(-x,y)