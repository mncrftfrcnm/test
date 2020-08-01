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
import teleport
import all_my_commands
q = Screen()
t = Turtle()
t.pu()
t2 = Turtle()
t2.speed(0)
t2.pu()
t2.goto(500,0)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            t.goto(x,y-3)
            x,y = t.pos()
            if y<=-500:
                print('you lose')
                self.keeprunning = False
            
beep  = beeper()
beep.start()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            t2.goto(300,y)
            for f in range(150):
                t2.forward(-3)
                tre = t2.distance(t)
                if tre <= 10:
                    print('you lose')
            
            
beep  = beeper()
beep.start()

def u(x,y):
    x,y = t.pos()
    t.goto(x,y+50)
    x,y = t.pos()
    if y>=500:
        print('you lose')
        
q.onscreenclick(u)
    
mainloop()