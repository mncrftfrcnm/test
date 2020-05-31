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
t1.speed(1)
t1.pu()
# t1.shapesize(120)
# t1.ondrag(t1.goto)
t4 = Pen()
t4.pu()
t4.goto(100,100)
t4.pu()

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            PlaySound("C:\windows\media\Ring02.wav",False)
            
beep  = beeper()
beep.start()

def da():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                for xrt in range(5): 
                    t2 = t1.clone()
                    x,y = t4.pos()
                    yt = randint(0,2)
                    
                    if yt == 0:
                        t2.goto(x/2,y*2)
                        t2.goto(x,y)
                    if yt == 1:
                        t2.goto(x/2,-y*2)
                        t2.goto(x,y)
                    if yt == 2:
                        t2.speed(0)
                        t2.goto(100,400)
                        t2.speed(1)
                        t2.right(90)
                        t2.forward(300)
                        t2.hideturtle()
                break
                
    beep  = beeper()
    beep.start()

listen()
s.onkey(da,'w')
mainloop()