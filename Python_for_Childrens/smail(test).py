from turtle import *

from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from turtle import *
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep

t = Pen()
t.hideturtle()
t.forward(100)
t.pu()
t.left(90)
t.forward(30)
t.right(90)
t.pd()
t.circle(10)
t.pu()
t.left(90)

t.forward(10)
t.right(90)
t1 = t.clone()
t1.showturtle()
t.forward(-100)
t.begin_fill()
t.circle(10)
t.end_fill()
t.pu()
t.goto(0,0)
t.forward(50)
t.left(90)
t.forward(25)
t.right(90)
t.showturtle()
mainloop()