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
# t1.shapesize(120)
# t1.ondrag(t1.goto)
t4 = Pen()
t4.pu()
t4.goto(-300,300)
t4.pd()
h = 700
y = 0
class beeper2(threading.Thread):
    def run(self):
        global y,h
        self.keeprunning = True
        while self.keeprunning:
            while True:
                time.sleep(1) 
                y = y+1
                if y >= 1:
                    t18 = Pen()
                    t18.speed(6)
                    t18.pu()
                    t18.hideturtle()
                    t18.goto(300,300)
                    t18.showturtle()
                    t18.goto(0,0)
                    t18.hideturtle()
                    h = h-y
                    h = h - 100
                    if h <= 0:
                        print("game over") 
                    
                    



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
                h = h+1

    beep  = beeper()
    beep.start()
listen()
s.onkey(da,'w')

mainloop()