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
e = 0
tre = ['turtle','circle','square','classic']
x = 0
screen = Screen()
t = Pen()
t.pu()
t.speed(0)
while True:
    #t.circle(x)
    x = x+1
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())
    
    x = randint(-400,400)
    y = randint(-400,400)
    t.goto(x,y)
    t1 = t.clone()
    t1.shape(choice(tre))

    t1.shapesize(3)