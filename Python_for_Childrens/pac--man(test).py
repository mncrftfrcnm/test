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
Screen().bgcolor('black')
t.shapesize(4)
t.shape('square')
t.color('yellow')
t.speed(0)
t.pu()
f = 0
e = Turtle()
e.speed(0)
e.pu()
e.forward(20)
e.shape('square')
e.color('white')
e.shapesize(2)
e2 = Turtle()
e2.speed(0)
e2.pu()
#e.forward(30)
e2.shape('square')
e2.color('white')
#e.shapesize(2)
x,y = e2.pos()
e2.goto(x,y+20)
e2.forward(-20)
while True:
    for x in range(500):
        e.ht()
        e2.ht()
        t.forward(5)
        e.forward(5)
        e2.forward(5)
        time.sleep(0.01)
        e.st()
        e2.st()
        time.sleep(0.01)

mainloop()