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
from PIL import Image
q = Screen()
t = Turtle()
t2 = Turtle()
t.pu()
t2.pu()
t.speed(0)
t2.speed(0)
x,y = t2.pos()
t2.goto(x,y+20)
ui = 0
class beeper(threading.Thread):
    def run(self):
        global ui
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            if ui == 0:
                t.right(1)
             #   print('p')

            
            
beep  = beeper()
beep.start()
def ata():
    global ui
    ui = 1
    t.forward(1)
    x,y = t.pos()
    x2,y2 = t.pos()
    if x2 >= 450:
        print('1p.lose')
    if x2 <= -450:
        print('1p.lose')
    if y2 >= 450:
        print('1p.lose')
    if y2 <= -450:
        print('1p.lose')
    x,y = t2.pos()
    x2,y2 = t.pos()
    yu = t.distance(t2)
    if yu <= 6:
        x,y = t.pos()
        t2.goto(x-10,y-10)
        x2,y2 = t2.pos()
        if x2 >= 450:
            print('2p.lose')
        if x2 <= -450:
            print('2p.lose')
        if y2 >= 450:
            print('2p.lose')
        if y2 <= -450:
            print('2p.lose')
def re1():
    global ui
    ui = 0
ui2 = 0
class beeper2(threading.Thread):
    def run(self):
        global ui2
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            if ui2 == 0:
                t2.right(1)
             #   print('p')

            
            
beep2  = beeper2()
beep2.start()
def ata2():
    global ui2
    ui2 = 1
    t2.forward(1)
    x,y = t2.pos()
    x2,y2 = t2.pos()
    if x2 >= 450:
        print('1p.lose')
    if x2 <= -450:
        print('1p.lose')
    if y2 >= 450:
        print('1p.lose')
    if y2 <= -450:
        print('1p.lose')
    x,y = t.pos()
    x2,y2 = t2.pos()
    yu = t2.distance(t)
    if yu <= 6:
        x,y = t2.pos()
        t.goto(x-10,y-10)
        x2,y2 = t.pos()
        if x2 >= 450:
            print('1p.lose')
        if x2 <= -450:
            print('1p.lose')
        if y2 >= 450:
            print('1p.lose')
        if y2 <= -450:
            print('1p.lose')
def re2():
    global ui2
    ui2 = 0
listen()
q.onkey(ata2,'i')
q.onkeypress(ata2,'i')
q.onkeyrelease(re2,'i')
listen()
q.onkey(ata,'w')
q.onkeypress(ata,'w')
q.onkeyrelease(re1,'w')
mainloop()