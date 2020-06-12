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
import sys
from PIL import Image
q = Screen()
t = Turtle()
t.speed(0)
t.pu()
f = 1
def go(item):
    item.goto(450,450)
go(t)
e = Turtle()
e.speed(0)
e.pu()
go(e)
e.forward(100)
e.shape("turtle")

mainloop()