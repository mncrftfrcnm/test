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

q = Screen()
q.setup(50,50)
t = Turtle()
t.right(-90)
s = 10
t.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t.pu()
def ata():
    global s
    t1 = t.clone()
    t1.shapesize(s,2,3)
    for cvc in range(9):
        for cvf in range(22):
            t1.forward(3)
        s = s - 1
        t1.shapesize(s,2,3)
    s = 10
listen()
q.onkey(ata,'w')
mainloop()