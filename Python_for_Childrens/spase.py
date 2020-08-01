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
t2.speed(0)
t2.forward(100)
r = 1
r2 = 0
h = 3

sha = ['classic','turtle','triangle','circle','square']
def ns():
    global h
    if h > 0:
        t.home()
    else:
        print('you lose')
def ata2():
    global r2
    t1 = t2.clone()
    
    if r2 == 1:
        o = 0
    if r2 == 0:
        o = 1
    r2 = o
    class beeper34(threading.Thread):
        def run(self):
            self.keeprunning = True
            global r2
            for sd in range(50):
                #print(';kb')
                t1.forward(-2)
                
                tre = t1.distance(t)
                x,y = t1.pos()
                
                if tre <= 10:
                    ns()

            t1.ht()
    beep34 = beeper34()
    beep34.start()

    
ata2()
class beeper2(threading.Thread):
    def run(self):
        global r2
        self.keeprunning = True
        while self.keeprunning:
            if r2 == 1:
                x,y = t2.pos()
                t2.goto(x,y - 3)
                x,y = t2.pos()
                if y <= -500:
                    r2 = 0
                x2,y2 = t2.pos()
                x,y = t.pos()
                if y2 == y:
                    ata2()
                    #print('p')
                    #self.keeprunning = False
            if r2 == 0:
                x,y = t2.pos()
                t2.goto(x,y + 3)
                x,y = t2.pos()
                if y >= 500:
                    r2 = 1
                x2,y2 = t2.pos()
                x,y = t.pos()
                if y2 == y:
                    ata2()
                    
                    #self.keeprunning = False

beep2  = beeper2()
beep2.start()
class beeper(threading.Thread):
    def run(self):
        global r
        self.keeprunning = True
        while self.keeprunning:
            if r == 1:
                x,y = t.pos()
                t.goto(x,y - 3)
                x,y = t.pos()
                if y <= -500:
                    r = 0
            if r == 0:
                x,y = t.pos()
                t.goto(x,y + 3)
                x,y = t.pos()
                if y >= 500:
                    r = 1
beep  = beeper()
beep.start()
def ata():
    global r
    t1 = t.clone()
    
    if r == 1:
        o = 0
    if r == 0:
        o = 1
    r = o
    for iu in range(50):
        t1.forward(2)
        tre = t1.distance(t2)
        if tre <= 10:
            t2.shape(random.choice(sha))
            t2.goto(100,0)
    t1.ht()

listen()
q.onkey(ata,'w')
mainloop()