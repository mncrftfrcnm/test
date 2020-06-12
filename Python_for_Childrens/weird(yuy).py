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
t.speed(1)
t.pu()
f = 1
e = Turtle()
e.speed(1)
e.pu()
e.forward(100)
def ata1():
    
    tre = t.distance(e)
    if tre <= 100:
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
            
                t1 = t.clone()
                x,y = e.pos()
                t1.goto(x,y)
                tre = t1.distance(e)
                if tre <= 10:
                    print("you win")
                    
        beep  = beeper()
        beep.start()
        
def ata2():
    
    tre = e.distance(t)
    if tre <= 10000:
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
            
                t1 = e.clone()
                x,y = t.pos()
                t1.goto(x,y)
                tre = t1.distance(t)
                if tre <= 4:
                    print("you lose")
                    
        beep  = beeper()
        beep.start()
        
def u():
    x,y = t.pos()
    t.goto(x,y+1)
def d():
    x,y = t.pos()
    t.goto(x,y-1)
def l():
    x,y = t.pos()
    t.goto(x-1,y)
def r():
    x,y = t.pos()
    t.goto(x+1,y)
def u2():
    x,y = t.pos()
    t.goto(x,y+1)
def d2():
    x,y = e.pos()
    e.goto(x,y-1)
def l2():
    x,y = e.pos()
    e.goto(x-1,y)
def r2():
    x,y = e.pos()
    e.goto(x+1,y)
listen()
#q.onkeypress(ata1,'.')
q.onkey(ata1,'.')
q.onkey(ata2,'q')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkey(u,'Up')
q.onkey(d,'Down')
q.onkey(l2,'a')
q.onkey(r2,'d')
q.onkey(u2,'w')
q.onkey(d2,'s')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')
q.onkeypress(u,'Up')
q.onkeypress(d,'Down')
mainloop()