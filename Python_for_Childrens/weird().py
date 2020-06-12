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
from PIL import Image
q = Screen()
t = Turtle()
listen()
t2 = Turtle()
t.pu()
t2.pu()
t.speed(0)
t2.speed(0)
t.goto(-450,-450)
t2.goto(-450,-50)
ret = input('what image do you wanna: ')
q.addshape(ret)
t.shape(ret)
rt = input('what image do you wanna: ')
q.addshape(rt)
t2.shape(rt)
fo = 0
def fk(x,y):
    global fo
    t1 = Turtle()
    t1.pu()
    t1.goto(0,500)
    t1.pd()
    t1.shape(ret)
    t1.speed(0)
    t1.forward(-fo)             
    fo = fo + 100

def fk2(x,y):
    global fo
    t1 = Turtle()
    t1.pu()
    t1.goto(0,500)
    t1.pd()
    t1.shape(rt)
    t1.speed(0)
    t1.forward(-fo)
    fo = fo + 100
t.onclick(fk)
t2.onclick(fk2)
mainloop()