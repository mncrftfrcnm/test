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


y = 100
t = Pen()
t.speed(0)
#t.ondrag(t.goto)
t.hideturtle()
for x in range(3):
    
    t.circle(100)
    t.pu()
    t.home()
    t.forward(y)
    t.pd()
    y = y + 100
t.pu()
t.home()
t.left(90)
t.forward(50)
t.right(90)
t.pd()
y = 200
for x in range(2):
    t.pu()
    
    t.forward(50)
    t.pd()
        
    t.circle(-100)
y = y + 100

mainloop()