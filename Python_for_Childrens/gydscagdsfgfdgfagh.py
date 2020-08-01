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
t.speed(0)
t.pu()
t2 = Turtle()
t2.pu()
t2.goto(200,-200)
h = t.clone()
h.goto(500,500)
ch = 1
tre = 1
typ = 1
fch = 2
def tele():
    global ch,tre,typ,fch
    teleport.random_teleport(t2,1)
    tro = randint(0,2)
    typ = tro
    ch = 0
    ch = ch + fch
    fch = fch + 1
    print(ch)
def ata():
    global tre

    tre = tre + 1
    print(tre)
def at():
    global tre,ch
    #fg = 1
    class beeper(threading.Thread):
        def run(self):
            global tre,ch
            self.keeprunning = True
            if tre >= 50 and tre < 100:
                
                t1 = t.clone()
                t1.shape('triangle')
                while True:

                    t1.forward(1)
                    tr = t1.distance(t2)
                    if tr <= 10:
                        ch = ch -5
                        break
                        if ch <= 0:
                            tele()
                            t1.ht()
                            break
                    x,y = t1.pos()
                    if x > 500 or y > 500 or x < -500 or y < -500:
                        t1.ht()
                        break
            if tre < 50:
                tre = 1
                t1 = t.clone()
            # t1.shape('triangle')
                while True:
                    t1.forward(1)
                    tr = t1.distance(t2)
                    if tr <= 10:
                        ch = ch -1
                        break
                        if ch <= 0:
                            tele()
                            t1.ht()
                            break
                    x,y = t1.pos()
                    if x > 500 or y > 500 or x < -500 or y < -500:
                        t1.ht()
                        break
            if tre > 100:
                t1 = t.clone()
                t1.shape('arrow')
                while True:
                    t1.forward(1)
                    tr = t1.distance(t2)
                    if tr <= 10:
                        ch = ch -10
                        if ch <= 0:
                            tele()
                            t1.ht()
                            break
                    x,y = t1.pos()
                    if x > 500 or y > 500 or x < -500 or y < -500:
                        t1.ht()
                        break
            tre = 1

                
    beep  = beeper()
    beep.start()

def r():
    t.seth(0)
    t.forward(3)
def l():
    t.seth(180)
    t.forward(3)
def u():
    t.seth(90)
    t.forward(3)
def d():
    t.seth(-90)
    t.forward(3)
listen()
q.onkey(d,'Down')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkeypress(u,'Up')
q.onkeypress(d,'Down')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')
q.onkeypress(ata,'w')
q.onkeyrelease(at,'w')
mainloop()