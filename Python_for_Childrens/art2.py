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
q = Screen()
t = Turtle()
t.pu()
t2 = Turtle()
t2.pu()
t2.speed(0)
t1 = Turtle()
t1.pu()
t1.forward(2)
listen()
def g():
    t2.forward(500)

def lh():
    ytj = randint(-50,50)
    if ytj == 0:
        t5 = t.clone()
        t5.forward(4)
        tre = t5.distance(t2)
        if tre <= 10:
            t.speed(0)
            t.ht()
            t.forward(-100)
            g()
            t.forward(100)
            t.speed(1)
            t.st()
        t5.ht()
q.onkey(lh,'i')
def ui():
    x,y = t1.pos()
    t1.goto(x,y+1)
def di():
    x,y = t1.pos()
    t1.goto(x,y-1)
g()
def a():
    class beeper(threading.Thread):
        def run(self):

            x,y = t1.pos()
            a = t.clone()
            a.goto(x,y)
            x2 = y/2
            a.goto(x2,0)
            x,y = t.pos()
            tre = a.distance(t2)
            if tre <= 8:
                g()
            a.ht()
    beep  = beeper()
    beep.start()
    #print(x)

                
#q.onkey(j,'Up')
q.onkey(a,'w')
q.onkey(di,'Down')
q.onkey(ui,'Up')

class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t2.forward(-1)
            tre = t2.distance(t)
            if tre <= 10:
                print("you lose")
                
               # beep.keeprunning = False
                self.keeprunning = False
            
beep2  = beeper2()
beep2.start()

mainloop()