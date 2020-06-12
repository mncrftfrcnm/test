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
from PIL import Image
q = Screen() 
t = Turtle()
t.speed(1)
t.pu()
t2 = Pen()
t2.speed(1)
t2.pu()
t2.goto(100,0)
q.onscreenclick(t.goto)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            PlaySound("C:\windows\media\Ring01.wav",False)
            
beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            w = randint(-400,400)
            e = randint(-400,400)
            t2.goto(w,e)
            
beep2  = beeper2()
beep2.start()

def trrtr():
    ret = distance(t,t2)
    
    if ret < 300:
        t1 = t.clone()
#        t1.hideturtle()
        x,y = t2.pos()
        t1.goto(x,y)
        t1.hideturtle()
        x,y = t1.pos()
        x2,y2 = t2.pos()
        if x == x2 and y == y2:
            t2.hideturtle()


listen()
q.onkey(trrtr,'w')
# if ret > 12:
#     print("K")
#   TurtleGraphicsErrorTurtleGraphicsError print("P")
#t.onclick(t.shapesize)
#t.onclick(t.color)
mainloop()
