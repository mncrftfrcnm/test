from turtle import *
from random import *

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
t = Turtle()
t.pu()
screen = Screen()
q = 0
e = turtle.Turtle()
class beeper1(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            screen.onscreenclick(t.goto)            
beep1  = beeper1()
beep1.start()
#screen.onscreenclick(t.goto)
e.pu()
e.goto(100,100)
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = e.pos()
            x2,y2 = t.pos()
            if x == x2 or y == y2:
                print("you lose")
beep2  = beeper2()
beep2.start()
class beeper3(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = e.pos()
            x2,y2 = t.pos()
            e.speed(3)
            e.goto(x2,y2)
beep3  = beeper3()
beep3.start()

def db():
    global q
    if q == 0:
        t1 = t.clone() 
        q = 1
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                        x,y = e.pos()
                        x2,y2 = t1.pos()
                        if x == x2 or y == y2:
                            print("you win")
                            self.keeprunning = False    
        beep  = beeper()
        beep.start()
listen()
screen.onkeypress(db,"w")
mainloop()

