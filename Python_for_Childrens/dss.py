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
t2 = Turtle()
t2.speed(0)

t2.pu()

t8 = Turtle()
#t2 = Turtle()
t8.speed(0)

t8.pu()
t8.goto(900,900)

fg = 0
def g(i):
    i.goto(-400,-400)
g(t2)

def tih():
    global fg
    t8.goto(0,-400)
    fg = 1
    def f():
        t8.forward(10)
    def b():
        t8.forward(-10)
    def u():
        x,y = t8.position()
        t8.goto(x,y+10)
        x,y = t8.pos()
        if y >= 400:
            print("you win")

    def d():
        x,y = t8.position()
        t8.goto(x,y-10)
    listen()
    q.onkey(f,'Right')
    q.onkey(b,'Left')
    q.onkey(u,'Up')
    q.onkey(d,'Down')

    
    
        

def ft2(x,y):
    global fg
    if fg == 0:
        t1 = t2.clone()
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                    tre = t1.distance(t8)
                    if tre <= 60:
                        tt = t1.clone()
                        tt.speed(1)
                        x,y = t8.pos()
                        tt.goto(x,y)
                        tre = tt.distance(t8)
                        if tre <= 10:
                            print("you lose")
        q.onscreenclick(t1.goto)
                    

                    
        beep  = beeper()
        beep.start()
t2.onclick(ft2)
listen()
q.onkey(tih,'w')
mainloop()