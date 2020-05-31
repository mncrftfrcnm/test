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
screen = Screen()
t = Pen()
t.speed(1)
listen()
#t.pu()
screen.onscreenclick(t.goto)
def d():
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pu()
    
    t.right(10)
def u():

    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pd()
    t.pu()
    
    t.right(-10)

screen.onkey(u,'Left')
screen.onkeypress(u,'Left')
screen.onkey(d,'Right')
screen.onkeypress(d,'Right')
while True:    
#    t.pu()
    t.forward(1)
mainloop()
