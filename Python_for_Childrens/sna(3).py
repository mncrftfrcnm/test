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
t2.forward(-10)
io = 1
def n():
    global io
    class beeper(threading.Thread):
        def run(self):
            po = 0
            self.keeprunning = True
            while self.keeprunning:
                if po == 1:
                    break

                
                io = 1
                t1 = t2.clone()
                #t2.ht()
                t3 = t1.clone()
                t3.forward(-10)
        
           #    while True:
                t1.forward(10)
                t3.forward(10)
                x,y = t1.pos()
                if x >= 500 or y >= 500 or y<= -500 or x<= -500:
                    x,y = t.pos()
                    t2.goto(x,y)
                    t2.forward(-10)
                    t2.st()
                    t1.ht()
                    t3.ht()
                    io = 1
                    po = 1
                    break

                time.sleep(0.1)
    beep  = beeper()
    beep.start()

def ata():
    t.forward(10)
    t2.forward(10)
  #  t2.forward(10)
def l():
    t.left(90)
    t.forward(10)
    t2.forward(10)
    t2.left(90)
    t2.forward(0)

#    t4.forward(4)
def r():
    t.left(-90)
    t2.forward(10)
    t2.left(-90)
    t.forward(10)
listen()
q.onkey(ata,'w')
q.onkey(n,'q')
q.onkey(l,'Left')
q.onkey(r,'Right')
mainloop()