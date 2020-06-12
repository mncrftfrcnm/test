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
t2 = Turtle()
t.pu()
t2.pu()
t.speed(1)
t2.speed(0)
t2.goto(670,0)
t2.shapesize(10)
h = 3
def ata():
    global h
    if h > 0:
        h = h - 1
        t1 = t.clone()
        while True:
            print("O")

            re = t1.distance(t2)
            if re <= 60:
                print('o')
                t1.ht()
                break
        

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            for x in range(778):
                
                t2.forward(-1)
                re = t2.distance(t)
                if re <= 60:
                    #sys.exit()
                    
                    print("U")
            x,y = t.pos()
            t2.goto(670,y)
            
            
beep  = beeper()
beep.start()
def u():
    x,y = t.pos()
    t.goto(x,y+1)
def d():
    x,y = t.pos()
    t.goto(x,y-1)
listen()
q.onkey(u,'Up')
q.onkey(ata,'w')
q.onkeypress(u,'Up')
q.onkey(d,'Down')
q.onkeypress(d,'Down')
mainloop()
