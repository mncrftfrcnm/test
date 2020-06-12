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
from PIL import Image
q = Screen()
t = Turtle()
t.speed(0)
t2 = Turtle()
t2.speed(0)
t3 = Turtle()
t3.speed(0)
t.pu()
t.forward(10)
t.pd()
time.sleep(1)
def w(x,y):
    print('you win')
def l(x,y):
    print('you lose')
t.onclick(w)
t2.onclick(l)
t3.onclick(l)

for h in range(10):
    u = randint(-450,450)
    v = randint(-450,450)
    t.goto(u,v)
    u = randint(-450,450)
    v = randint(-450,450)
    t2.goto(u,v)
    u = randint(-450,450)
    v = randint(-450,450)
    t3.goto(u,v)
    time.sleep(0.3)
mainloop()