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
t.speed(0)
#t.left(90)
listen()
t.pu()
t2 = Turtle()
#t.left(90)
t2.pu()
t2.speed(0)
t2.forward(300)
t2.left(180)
def ret():
    t.left(10)
    t2.right(10)
def ret2():
    t.left(-10)
    t2.right(-10)
def f():
    t.forward(1)
    t2.forward(1)
screen.onkeypress(ret,'Left')
screen.onkeypress(ret2,'Right')
screen.onkeypress(f,'w')

mainloop()