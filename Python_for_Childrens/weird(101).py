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
e.speed(0)
e.pu()
e.forward(100)
e.right(180)
mn = 0
def cd():
    global f
    f2 = f
    if f <2:
        e.right(180)
        f2 = f2 +1

    if f>=2:
        f2 = 0
        e.right(180)
    f = f2
def destroyt(ytem):
    yu = randint(0,1)
    if yu == 0:
        ytem.goto(500,0)
    if yu == 1:
        ytem.goto(-500,0)
def ata(k):
    if k == 1:
        t.speed(0)       
        t.forward(100)
        t.speed(1)
    if k == 2:
        t1 = t.clone()
        e.right(180)
        t1.shape('circle')
        class beeper(threading.Thread):
            def run(self):
                global mn
                self.keeprunning = True
                while self.keeprunning:
                    t1.forward(1)
                    rte = t1.distance(e)
                    if rte <= 4:
                        destroyt(e)
                        self.keeprunning = False
                        x,y = t1.pos()
                        if x >= 500:
                            t1.goto(-x,y)
                        if x <= 500:
                            t1.goto(-x,y)

                            
                    
        beep  = beeper()
        beep.start()
def at():
    global f
    ata(f)
listen()
q.onkey(at,'w')
q.onkey(cd,'q')
class beeper(threading.Thread):
    def run(self):
        global mn
        self.keeprunning = True
        while self.keeprunning:
            e.forward(1)
            tre = e.distance(t)
            if tre <=10:
                print("P")

            x,y = e.pos()
            if x >= 500:
                e.goto(-x,y)
            x,y = e.pos()
            if x <= -500:
                e.goto(-x,y)

                    
beep  = beeper()
beep.start()

mainloop()


