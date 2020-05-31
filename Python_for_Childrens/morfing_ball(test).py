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
x = 0
screen = Screen()
t = Pen()
t.shapesize(4)
def morf():
    global x
    if x == 0:
        print("P")
        t.shapesize(1)
        t.shape("circle")
        x2 = 1

    if x == 1:
        print("O")
        t.shapesize(4)
        t.shape("classic")
        x2 = 0
    x = x2
listen()
screen.onkey(morf,'o')
mainloop()

