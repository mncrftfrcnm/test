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
def g(i):
    i.goto(-400,-400)
g(t)
#q = Screen()
t2 = Turtle()
t2.speed(0)

t2.pu()
g(t2)
t2.forward(100)
e = Turtle()
e.speed(0)

e.pu()
#g(t2)
e.forward(100)
t3 = Turtle()
t3.speed(0)
t3.pu()
g(t3)
t3.forward(200)
t4 = Turtle()
t4.speed(0)
t4.pu()
g(t4)
t4.forward(300)
uyyu = 1
def ft4(x,y):
    global uyyu

    t1 = t4.clone()
    uyyu = 1
    def tre(x,y):
        global uyyu
        if uyyu == 1:
            t1.goto(x,y)
            uyyu = 0
    q.onscreenclick(t1.goto)

    class beeper(threading.Thread):
        
        def run(self):
            global h
            self.ph = 10
            self.keeprunning = True
            while self.keeprunning:



                yu = t1.distance(e)
                if yu <= 40:
                    t5 = t1.clone()
                    x,y = e.pos()
                    t5.speed(1)
                    t5.goto(x,y)
                    uy = t5.distance(e)
                    if uy <=10:
                        print(h)
                        t5.ht()
                        h = h - 1
                        if h <= 0:
                            print('you win')
                    t5 = t1.clone()
                    x,y = e.pos()
                    t5.speed(1)
                    t5.goto(x,y)
                    uy = t5.distance(e)
                    if uy <=10:
                        print(h)
                        t5.ht()
                        h = h - 1
                        if h <= 0:
                            print('you win')
                if yu <= 60:
                    t7 = e.clone()
                    t7.speed(1)

                    x,y = t1.pos()
                    t7.goto(x,y)
                    t7.ht()
                    ertr = t7.distance(t1)
                    if ertr <=10:

                        self.ph = self.ph - 1
                        if self.ph <=0:
                            t1.ht()
                            self.keeprunning = False
                
    beep  = beeper()
    beep.start()
        

def ft3(x,y): 
    t1 = t3.clone()

    class beeper(threading.Thread):
        
        def run(self):
            global h
            self.ph = 10
            self.keeprunning = True
            while self.keeprunning:


                tre = randint(1,7)
                
                if tre == 1 or tre == 5:
                    t1.forward(10)
                
                if tre == 2:
                    t1.forward(-10)
                if tre == 3 or tre == 6:
                    x,y = t1.pos()
                    t1.goto(x,y+10)
                if tre == 4:
                    x,y = t1.pos()
                    t1.goto(x,y-10)
                yu = t1.distance(e)
                if yu <= 40:
                    t5 = t1.clone()
                    x,y = e.pos()
                    t5.speed(1)
                    t5.goto(x,y)
                    uy = t5.distance(e)
                    if uy <=10:
                        print(h)
                        t5.ht()
                        h = h - 1
                        if h <= 0:
                            print('you win')
                    t5 = t1.clone()
                    x,y = e.pos()
                    t5.speed(1)
                    t5.goto(x,y)
                    uy = t5.distance(e)
                    if uy <=10:
                        print(h)
                        t5.ht()
                        h = h - 1
                        if h <= 0:
                            print('you win')
                if yu <= 60:
                    t7 = e.clone()
                    t7.speed(1)

                    x,y = t1.pos()
                    t7.goto(x,y)
                    t7.ht()
                    ertr = t7.distance(t1)
                    if ertr <=10:

                        self.ph = self.ph - 1
                        if self.ph <=0:
                            t1.ht()
                            self.keeprunning = False
                
    beep  = beeper()
    beep.start()
    


h = 100
def ft2(x,y):
    global h
    t1 = t2.clone()
    def dj(x,y):
        global h
        
        t1.goto(x,y)
        trt = t1.distance(e)
        
        if trt <= 30:
            t1.ht()
            h = h -5
            if h <= 0:
                print("you win")
        
    q.onscreenclick(dj)

    
def ft(x,y):

    t1 = t.clone()
    class beeper(threading.Thread):
        def run(self):
            global h
            self.ph = 10
            self.keeprunning = True
            while self.keeprunning:
                tre = randint(1,7)
                if tre == 1 or tre == 5:
                    t1.forward(10)
                
                if tre == 2:
                    t1.forward(-10)
                if tre == 3 or tre == 6:
                    x,y = t1.pos()
                    t1.goto(x,y+10)
                if tre == 4:
                    x,y = t1.pos()
                    t1.goto(x,y-10)
                yu = t1.distance(e)
                if yu <= 50:
                    t5 = t1.clone()
                    x,y = e.pos()
                    t5.speed(1)
                    t5.goto(x,y)
                    uy = t5.distance(e)
                    if uy <=10:
                        print(h)
                        t5.ht()
                        h = h - 1
                        if h <= 0:
                            print('you win')
                if yu <= 60:
                    t7 = e.clone()
                    t7.speed(1)

                    x,y = t1.pos()
                    t7.goto(x,y)
                    t7.ht()
                    ertr = t7.distance(t1)
                    if ertr <=10:

                        self.ph = self.ph - 1
                        if self.ph <=0:
                            t1.ht()
                            self.keeprunning = False


                
                
                
    beep  = beeper()
    beep.start()
    

listen()
t.onclick(ft)
t2.onclick(ft2)
t3.onclick(ft3)
t4.onclick(ft4)

mainloop()
