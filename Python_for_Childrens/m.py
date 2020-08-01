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
import se
q = Screen()
t = Turtle()
t.speed(0)
listen()
t.pu()
def r():
    se.r(t)
q.onkey(r,'Right')

def l():
    se.l(r)
q.onkey(l,'Left')

t1 = t.clone()
t1.ht()
t1.shape('square')
x,y = t1.pos()
t1.goto(x+20,y)
t1.st()
def fu():
    print("P")
def ata():
    se.ata(t,t1,fu)
q.onkey(ata,'w')
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            x2,y2 = t1.pos()
            tre = t1.distance(t)
            


def u():
    x,y = t.pos()
    t.goto(x,y+1)
def d():
    x,y = t.pos()
    t.goto(x,y-1)

q.onkey(u,'Up')
q.onkey(d,'Down')
  
beep  = beeper()
beep.start()

mainloop()