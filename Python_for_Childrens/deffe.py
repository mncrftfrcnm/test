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
t.speed(0)

t.pu()
f = 1
e = Turtle()
#q.onscreenclick(t.goto)
e.speed(0)

e.pu()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            
            e.forward(1)
            rhhhhhj = e.distance(t)
            if rhhhhhj <= 10:
                print("you lose")
            

def c(item):
    y = randint(-400,400)
    w = randint(0,1)
    if w == 0:
        item.goto(-400,y)
        beep2  = beeper2()
        beep2.start()

    if w == 1:
        item.goto(400,y)
        beep2  = beeper2()
        beep2.start()

def ata():
    t1 = t.clone()
    t1.shape('square')
    class beeper(threading.Thread): 









        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                x,y = t1.pos()
                tr = t1.distance(e)
                if tr <= 10:
                    c(e)
                    t1.ht()
                    self.keeprunning = False

                
    beep  = beeper()
    beep.start()
def ru():
    beep2  = beeper2()
    beep2.start()

def l():
    t.forward(-10)    
def r():
    t.forward(10)
def d():
    x,y = t.pos()
    t.goto(x,y-10)    
def u():
    x,y = t.pos()
    t.goto(x,y+10)
listen()
q.onkey(ata,'w')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkey(u,'Up')
q.onkey(d,'Down')
q.onkey(ru,'q')
mainloop()