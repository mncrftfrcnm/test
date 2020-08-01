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
shapes = ['triangle','turtle','square','circle','classic','arrow']
t.pu()
t2 = Turtle()
t2.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t2.pu()
t2.forward(100)
t3 = Turtle()
t3.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t3.pu()
t3.forward(200)
t3.left(90)
def techer_attack():
    for x in range(3):
        tre = randint(0,1)
        if tre == 0:
            tre = randint(0,7)
            tre2 = randint(0,7)
            ftree = tre,'-',tre2
            tree = int(input(ftree))
            an = tre-tre2
            
            if an == tree:
                print('right')
            else:
                print('bad')
                break
        if tre == 1:
            tre = randint(0,7)
            tre2 = randint(0,7)
            ftree = tre,'+',tre2
            tree = int(input(ftree))
            an = tre+tre2
            if an == tree:
                print('right')
            else:
                print('bad')
                print('you lose')
                break
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            for f in range(100):
                t2.forward(1)
                tre = t2.distance(t)
                if tre <= 10:
                    techer_attack()
                    t2.forward(100)
            for f in range(100):
                t2.forward(-1)
                tre = t2.distance(t)
                if tre <= 10:
                    techer_attack()
                    t2.forward(100)
beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            for f in range(100):
                t3.forward(1)
                tre = t3.distance(t)
                if tre <= 10:
                    techer_attack()
                    t3.forward(100)
            for f in range(100):
                t3.forward(-1)
                tre = t3.distance(t)
                if tre <= 10:
                    techer_attack()
                    t3.forward(100)
beep2  = beeper2()
beep2.start()

sa = 0

def s_techer_attack():
    for x in range(3):
        tre = randint(0,1)
        if tre == 0:
            tre = randint(0,10)
            tre2 = randint(0,10)
            ftree = tre,'+',tre2
            tree = int(input(ftree))
            an = tre-tre2
            if an == tree:
                print('right')
            else:
                print('bad')
                break
        if tre == 1:
            tre = randint(0,10)
            tre2 = randint(0,10)
            ftree = tre,'+',tre2
            tree = int(input(ftree))
            an = tre+tre2
            if an == tree:
                print('right')
            else:
                print('bad')
                print('you lose')
                break
def u():
    global sa
    if sa == 0:
        sa = 1
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                    t.right(50)
        beep  = beeper()
        beep.start()
        for xyt in range(20):



            x,y = t.pos()
            t.goto(x,y+7)
        #beep.keeprunning = False
        for xyt in range(20):



            x,y = t.pos()
            t.goto(x,y-7)
        beep.keeprunning = False
        tre = t.heading()
        t.setheading(0)
        t.setheading(0)
        t.setheading(0)
        t.setheading(0)
        sa = 0
def f():
  
    class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                x,y = t2.pos()
                t2.goto(x-2,y)
                x,y = t3.pos()
                t3.goto(x-2,y)
    beep  = beeper()
    beep.start()
    
def b():
  
    class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                x,y = t2.pos()
                t2.goto(x+2,y)
                x,y = t3.pos()
                t3.goto(x+2,y)
    beep  = beeper()
    beep.start()
    
listen()
q.onkey(u,'Up')
q.onkey(f,'Right')
q.onkeypress(f,'Right')
q.onkey(b,'Left')
q.onkeypress(b,'Left')

mainloop()