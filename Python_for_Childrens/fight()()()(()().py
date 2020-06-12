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
t2.forward(100)
def cd():
    Screen().bgcolor('black')
    t.goto(900,900)
    t2.goto(900,900)
    Screen().bgcolor('white')
def cd2():
    global ch,ph,p
    ch = 5
    ph = 10
    Screen().bgcolor('black')
    t.goto(0,0)
    t2.goto(100,0)
    Screen().bgcolor('white')
p = 0
ph = 10
ch = 5
def fight(c):
    global p,ph,ch
    if c == 't':
        ch = 5
        ph = 10
        rt = 1
        cd()
        u = Turtle()
        u.pu()
        u.speed(1)
        e = Turtle()
        e.pu()
        e.color("red")
        e.speed(1)
        e.forward(100)

        def j():
            global ch,rt
            x,y = u.pos()
            u.goto(x,y+100)
            u.goto(x,y)
            ert = u.distance(e)
            if ert <= 10:
                ch = ch - 1
                if ch <= 0:
                    e.ht()
                    rt = 0
                    cd2()
                    u.ht()
                    p = 2
        def f():
            u.forward(1)
        def b():
            u.forward(-1)
        def ata():
            global p
            #print(p)
            if p == 0:
               # print("O")
                t1 = u.clone()
                
                class beeper(threading.Thread):
                    def run(self):
                        global ch,ph,p
                        self.keeprunning = True
                        while self.keeprunning:
                            #print("PO")
                            t1.forward(1)
                            ert = t1.distance(e)
                            if ert <=10:
                                ch = ch - 1
                            #    print(ch)
                                t1.ht()
                                self.keeprunning = False

#                                self.keeprunning = False
                                if ch <= 0:
                                    e.ht()
                                    rt = 0
                                    cd2()
                                    u.ht()
                                    p = 2
                                    self.keeprunning = False
                            x,y = t1.pos()
                            if x >= 500:
                                self.keeprunning = False

                beep = beeper()
                beep.start()
        class beeper(threading.Thread):
            def run(self):
                global ch,ph,p
                self.keeprunning = True
                while self.keeprunning:
                    for yuyy in range(7):
                        x,y = e.pos()
                        e.goto(x,y+100)
                        x,y = u.pos()
                        e.goto(x,y)
                        te = e.distance(u)
                        if te <= 10:
                            ph = ph - 1
                            if ph <=0:
                                e.ht()

                                rt = 0
                                cd2()
                                u.ht()
                            
                        time.sleep(0.01)
                    time.sleep(3)
                    
        beep  = beeper()
        beep.start()

        listen()
        q.onkey(j,'Up')
        q.onkeypress(f,'Right')
        q.onkeypress(b,'Left')
        q.onkey(ata,'w')

    if c == 't2':
        rt = 1
        cd()
        u = Turtle()
        u.pu()
        u.speed(1)
        e = Turtle()
        e.pu()
        e.color("red")
        e.speed(1)
        e.forward(-100)

        def j():
            global ch,rt
            x,y = u.pos()
            u.goto(x,y+100)
            u.goto(x,y)
            ert = u.distance(e)
            if ert <= 10:
                ch = ch - 1
                if ch <= 0:
                    e.ht()
                    rt = 0
                    cd2()
                    u.ht()
                    p = 1
        def f():
            u.forward(1)
        def b():
            u.forward(-1)
        def ata2():
            global ch,p
            if p == 2:
                x,y = u.pos()
                u.goto(x,y+200)
                x2,y2 = e.pos()
                u.goto(x2,y2)
                x,y = u.pos()
                ert = u.distance(e)
                if ert <= 10:
                    ch = ch - 1
                    if ch <= 0:
                        e.ht()
                        rt = 0
                        cd2()
                        u.ht()
                        p = 1
        class beeper2(threading.Thread):
            def run(self):
                global ph,rt
                self.keeprunning = True
                #self.running = True
        
                while self.keeprunning:
                    
                    t1 = e.clone()      
                    for akjld in range(500):
                        #print()
                       # print("OU")
                        t1.forward(1)
                        ert = t1.distance(u)
                        if ert <= 10:
                            ph = ph - 1
                            if ph <= 0:

                                t1.ht()
                                self.keeprunning = False
    #                   self.keeprunning = False
                                if ph <= 0:
                                    e.ht()
                                    rt = 0
                                    cd2()
                                    u.ht()
                                # p = 2
                                    self.keeprunning = False
                            
                        x,y = t1.pos()
                        if x >= 500:
                            t1.ht()
                       #     self.keeprunning = False
                    #  time.sleep(3)

                    
        beep2  = beeper2()
        beep2.start()

        listen()
        q.onkey(j,'Up')
        q.onkeypress(f,'Right')
        q.onkeypress(b,'Left')
        q.onkey(ata2,'q')
def ft1(x,y):
    fight('t')

            
t2.onclick(ft1)
def ft2(x,y):
    fight('t2')
t.onclick(ft2)


mainloop()