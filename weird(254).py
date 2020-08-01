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
gh = 7
q = Screen()
t = Pen()
t.speed(0)
#t.pu()
while True:
    t.left(-10)
    t1 = t.clone()
    t1.forward(100)
    time.sleep(0.7)
    t1.color('white')
    t1.forward(-100)
    time.sleep(1)

    