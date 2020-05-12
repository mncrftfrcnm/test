from turtle import *
import turtle
import threading
from threading import *
import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
Screen = turtle.Screen()
Screen.bgcolor("black")
t = Pen()
t.hideturtle()
t.color("blue")
t.speed(0)
while True:
    t.pu()
    ty = randint(-500,500)
    y = randint(-500,500)
    t.setpos(ty,y)
    t.pd()
    ew = randint(0,1)
    if ew == 0:
        t.dot()
    if ew == 1:
        for i in range(5):
            t.forward(150)
            t.right(144)
    







