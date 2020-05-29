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
t4 = 1
t = Pen()
t.pu()
print(one)
t.shape("circle")
def morfstate():
    global ert
    ert = "classic"
    t.shape("classic")
#    print(ert)
def morf():
    global ert
    ert = "circle"
    t.shape("circle")
#    print(ert)
def morfspider():
    global ert
    ert = "square"
    t.shape("square")
#    print(ert)
def sd():
    global ert

    if ert == "circle":
        t.forward(50)
def sj():
    global ert
#    print("L")
    if ert == "circle":
        x,y = t.pos()
        t.goto(x,y+50)

        x,y = t.pos()
        t.goto(x,y-50)
        

def sl():
    global ert
    if ert == "circle":
        t.forward(-50)
def sr():
    global ert
    if ert == "circle":
        t.forward(50)
def cs():
    global ert
    if ert == "classic":
        t1 = t.clone()
        for x in range(300):
        
            t1.forward(1)
def qu():
    global ert
    if ert == "square":
        x,y = t.pos()
        t.goto(x,y+10)

def qd():
    global ert
    if ert == "square":
        x,y = t.pos()
        t.goto(x,y-10)
def qr():
    global ert
    if ert == "square":
        x,y = t.pos()
        t.goto(x+10,y)

def ql():
    global ert
    if ert == "square":
        x,y = t.pos()
        t.goto(x-10,y)

listen()
screen.onkey(morf,"p")

screen.onkey(morfspider,"o")
screen.onkey(morfstate,"i")
screen.onkey(sl,"Left")

screen.onkey(sj,"Up")
screen.onkey(sr,"Right")
screen.onkey(cs,"1")

screen.onkey(qu,"q")
screen.onkey(qd,"w")
screen.onkey(ql,"a")

screen.onkey(qr,"s")
mainloop()