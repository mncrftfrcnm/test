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
t.speed(0)
t2 = Turtle()
t2.pu()
t2.speed(1)
t2.forward(-10)
def tele():
    tre = randint(0,3)
    if tre == 0:
        y = randint(-500,500)
        x = 500
    if tre == 1:
        y = randint(-500,500)
        x = -500
    if tre == 2:
        x = randint(-500,500)
        y = 500
    if tre == 3:
        x = randint(-500,500)
        y = -500
    teleport.teleport(t2,1,x,y)
tele()


class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            time.sleep(56)
            x,y = t.pos()
            t2.goto(x,y)
            tre = t2.distance(t)
            if tre <= 10:
                tele()
                     
            
beep  = beeper()
beep.start()
def ata():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            t1 = t.clone()
            while True:
    
                t1.forward(3)
                tre = t1.distance(t2)
                if tre <= 10:
                    t1.ht()
                    beep.keeprunning = False
                    tele()
                    beep.keeprunning = True
        
                    break           
                x,y = t1.pos()
                if x <= -500 or y <= - 500 or x >= 500 or y >= 500:
                    t1.ht()
                    break 

                
    beep  = beeper()
    beep.start()
def r():
    t.left(10)
def l():
    t.left(-10)

listen()
q.onkey(ata,'w')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')
mainloop()