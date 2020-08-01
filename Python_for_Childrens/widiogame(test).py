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
t2 = Turtle()
t2.speed(1)
t2.pu()
t2.forward(400)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            ty = random.randint(0,67)
            if ty != 1:
                x,y = t.pos()
                t2.goto(x,y)
                tre = t2.distance(t)
                if tre <= 10:
                    print('you lose')
            if ty == 1:
                class beeper2(threading.Thread):
                    def run(self):
                        x,y = t.pos()
                        t1 = t2.clone()
                        t1.color('green')
                        t1.goto(x,y)
                        tre = t1.distance(t)
                        if tre <= 10:
                            print('you lose')
                beep2  = beeper2()
                beep2.start()                    
beep  = beeper()
beep.start()

def ata(x,y):
    t1 = t.clone()               
    t1.speed(0)
    t1.goto(x,y)
    tre = t1.distance(t2)
    
    if tre <= 10:
        print('you win')
        beep.keeprunning = False
    time.sleep(0.1)
    t1.ht()
def got(x,y):
    t.goto(x,y)
q.onscreenclick(ata,btn=3)
q.onscreenclick(got,btn=2)
mainloop()