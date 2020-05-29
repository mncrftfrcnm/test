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
e = 0
x = 0
screen = Screen()
t = Pen()
t.pu()
def ata():
    global e
    e = e+ 1
def ata2():
    global e
    if e < 90:
        t1 = t.clone()
        for y in range(500):
            t1.forward(1)
    
    if e >= 90 and e < 150:
        t1 = t.clone()
        t1.shape("square")
        for y in range(500):
            t1.forward(1)
    
    if e >=150:
        t1 = t.clone()
        t1.shapesize(10)
        for y in range(500):
            t1.forward(1)
    
#release
listen()
screen.onkey(ata,'w')
screen.onkeypress(ata,'w')
screen.onkeyrelease(ata2,'w')
mainloop()