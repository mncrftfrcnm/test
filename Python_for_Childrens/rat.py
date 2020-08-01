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
from se import *
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
            if tre <= 10:
                g()
            a.ht()
    beep  = beeper()
    beep.start()
    #print(x)

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
                #tyyk = t.clone()
                #t.home()
                
                
            x,y = t1.pos()
            t1.goto(x,y+400)
            x,y = t1.pos()
            t1.goto(x,y-400)

                
#q.onkey(j,'Up')
q.onkey(a,'w')

beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t2.forward(-1)
            tre = t2.distance(t)
            if tre <= 10:
                print("you lose")
                
                beep.keeprunning = False
                self.keeprunning = False
            
beep2  = beeper2()
beep2.start()

mainloop()