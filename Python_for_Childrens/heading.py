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
screen = Screen()
t = Turtle()
t.pu()
listen()
t.speed(0)
t.forward(200)
def ret():
    t.left(1)
   # t2.right(1)
def ret2():
    t.left(-1)
  #  t2.right(-1)
def h():
    t.forward(1)
#   t2.forward(1)
def f():
    g = t.heading()
    clear()
    write(g)
screen.onkeypress(ret,'Left')
screen.onkeypress(ret2,'Right')
screen.onkey(f,'w')
mainloop()