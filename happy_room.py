from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import turtle
from turtle import *
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep

s = Screen()
t1 = Pen()
t1.pu()
t1.shapesize(120)
t1.ondrag(t1.goto)
t4 = Pen()
t4.pu()
t4.goto(-300,300)
t4.pd()
h = 700
y = 0
class beeper2(threading.Thread):
    def run(self):
        global y
        self.keeprunning = True
        while self.keeprunning:
            while True:
                time.sleep(1) 
                y = y+1
                print(y)

beep  = beeper2()
beep.start()
def da():
    t = Pen()
    t.pu()
    t.shape('square')
    s.onscreenclick(t.goto)
    class beeper(threading.Thread):
        def run(self):
            global h,y
            self.keeprunning = True
            while self.keeprunning:
                t2 = t.clone()
                x,y2 = t1.pos()
                t2.goto(x,y2)
                t2.hideturtle()
                t2.speed(0)
                t2.goto(x,y2)
                x,y2 = t1.pos()
                x3,y3 = t2.pos()
                if x == x3 and y2== y3:
         #           print('h')
                    t4.forward(1)
                    h = h -1
                    if h <= 0:
                        print("your time is",y)
                        break

    beep  = beeper()
    beep.start()
def dm():
    t = Pen()
    t.speed(0)
    

    t.pu()
    t.goto(-400,-400)
    t.speed(1)
    t.shape('turtle')
#    s.onscreenclick(t.goto)
    class beeper(threading.Thread):
        def run(self):
            global h,y
            self.keeprunning = True
            while self.keeprunning:
                
                x,y2 = t1.pos()
                t.goto(x,y2)
                #t2.hideturtle()
                
                x,y2 = t1.pos()
                x3,y3 = t.pos()
                if x == x3 and y2== y3:
                    t4.forward(1)
                    h = h -1
                    if h <= 0:
                        print("your time is",y)
                        break

    beep  = beeper()
    beep.start()
listen()
s.onkey(da,'w')
s.onkey(dm,'e')
#tre = input('is it all: ')


mainloop()