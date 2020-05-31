from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import turtle
from turtle import *
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
tre = 10
ert = 1
s = Screen()
t1 = Pen()
t1.pu()
while True:

    x,y = t1.pos()
    t = t1.clone()
    t.goto(x+tre,y)
    yt = randint(7,10)
    if yt == 10:
        t.color('yellow')
    if yt == 7:
        t.color('red')
    x,y = t1.pos()
    t = t1.clone()
    t.goto(x-tre,y)
    if yt == 10:
        t.color('yellow')
    if yt == 7:
        t.color('red')
    x,y = t1.pos()
    t = t1.clone()

    t.goto(x,y+tre)
    yt = randint(7,10)
    if yt == 10:
        t.color('yellow')
    if yt == 7:
        t.color('red')
    x,y = t1.pos()
    t = t1.clone()
    t.goto(x,y-tre)
    yt = randint(7,10)
    if yt == 10:
        t.color('yellow') 
    if yt == 7:
        t.color('red') 
    tre = tre+10
    time.sleep(0.0000000001)
#    t1.color('red')
