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
import datetime
wait_seconds = 1
WinWidth=750
screen = Screen()
t = Turtle()
t.pu()

t.speed(0)
t2 = Turtle()
t2.pu()

t2.speed(0)
t2.forward(50)
t3 = Turtle()
t3.pu()

t3.speed(0)
t3.forward(100)
t0 = Turtle()
t0.pu()

t0.speed(0)
t0.forward(-50)
t01 = Turtle()
t01.pu()

t01.speed(0)
t01.forward(-100)
t02 = Turtle()
t02.pu()

t02.speed(0)
t02.forward(-150)
t02.ht()
t01.ht()
t0.ht()
t.ht()
t2.ht()
t3.ht()

while True:
    ti = datetime.datetime.now()
    t.write(ti.hour)
    
    
    t3.write(ti.second)
    t2.write(ti.minute)
    t0.write(ti.day)
    t01.write(ti.month)
    t02.write(ti.year)
    time.sleep(1)
    t.clear()
    t2.clear()
    t3.clear()
    t0.clear()
    t01.clear()
    t02.clear()