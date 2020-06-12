from turtle import *
from random import *

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
wait_seconds = 1
WinWidth=750


s = Screen()
t=Pen()
t.pu()
t.speed(1)
t.shape('circle')
y = 0


def ata():
    global y
    y = y + 1
def ata2():
    global y
    x,i = t.pos()
    t.goto(x+y,i)
    y = 0
listen()
s.onkeypress(ata,'w')
s.onkeyrelease(ata2,'w')
while True:
    t.right(10)
mainloop()