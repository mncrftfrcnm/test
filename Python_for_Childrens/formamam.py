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
t = Turtle()
t.speed(0)
#t.pu()
def f(x,y):
    ht()
    pu()
    goto(x,y)
    write(x,y)
def s():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="duck.gif")

q.onscreenclick(t.goto)
q.onscreenclick(f,btn= 3)
q.onkey(s,'w')
mainloop()