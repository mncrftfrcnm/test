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
t.forward(300)
a1 = 1
a2 = 1
j1 = 1       
j2 = 1

def ata1():
    global a1
    if a1 == 1:
        a1 = 0
        t1 = t.clone()
        class beeper(threading.Thread):
            def run(self):
                global a1
                self.keeprunning = True
                while self.keeprunning:
                    t1.forward(1)
                    x,y = t1.pos()
                    tre = t1.distance(t2)
                    if tre <= 10:
                        print('1p win!')
                        self.keeprunning = False
                        a1 = 1
                    if x < -500 or x > 500:
                        self.keeprunning = False
                        t1.ht()
                        a1 = 1
                
                
        beep  = beeper()
        beep.start()
def ata2():
    global a2
    if a2 == 1:
        a2 = 0
        t1 = t2.clone()
        class beeper(threading.Thread):
            def run(self):
                global a2
                self.keeprunning = True
                while self.keeprunning:
                    t1.forward(1)
                    x,y = t1.pos()
                    tre = t1.distance(t)
                    if tre <= 10:
                        print('2p win!')
                        a2 = 1
                        self.keeprunning = False
                    if x < -500 or x > 500:
                        self.keeprunning = False
                        t1.ht()
                        a2 = 1
                
                
        beep  = beeper()
        beep.start()
def u2():
    global j2
    if j2 == 1:
        j2 = 0
        #t1 = t2.clone()
        class beeper(threading.Thread):
            def run(self):
                global j2
                self.keeprunning = True
                for uy in range(30):
                    x,y = t2.pos()
                    t2.goto(x,y + 1)
                for uy in range(30):
                    x,y = t2.pos()
                    t2.goto(x,y - 1)
                j2 = 1
                
                        
                
                
        beep  = beeper()
        beep.start()
def u1():
    global j1
    if j1 == 1:
        j1 = 0
        #t = t.clone()
        class beeper(threading.Thread):
            def run(self):
                global j1
                self.keeprunning = True
                for uy in range(30):
                    x,y = t.pos()
                    t.goto(x,y + 1)
                for uy in range(30):
                    x,y = t.pos()
                    t.goto(x,y - 1)
                j1 = 1
                
                        
                
                
        beep  = beeper()
        beep.start()
def f1():
    # class beeper(threading.Thread):
    #     def run(self):
    #         global j2
    #         self.keeprunning = True
    #         for uy in range(30):
    #             x,y = t2.pos()
    #             t2.goto(x,y + 1)
    #             for uy in range(30):
    #             x,y = t2.pos()
    #             t2.goto(x,y - 1)
    #         j2 = 1
                
                        
                
                
    # beep  = beeper()
    # beep.start()
    t.setheading(180)
    t.forward(3)
def f2():
    t2.setheading(180)
    t2.forward(3)
def b1():
    t.setheading(0)
    t.forward(3)
def b2():
    t2.setheading(0)
    t2.forward(3)
listen()
q.onkey(ata1,'.')
q.onkey(ata2,'q')
q.onkey(u2,'w')
q.onkey(u1,'Up')
q.onkey(f1,'Left')
q.onkey(f2,'a')
q.onkey(b1,'Right')
q.onkey(b2,'d')

mainloop()