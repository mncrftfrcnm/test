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
q.setup(1500,1500)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t2.pu()
bombs = -1
ti = 0
def telr():
    tyr = randint(3,3)
    if tyr == 3:
        x = 500
        y = randint(-500,500)

    teleport.teleport(t2,1,x,y)    
#telr()
class beeper(threading.Thread):
    def run(self):
        global ti
        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            ti = ti + 1

f = 0
beep  = beeper()
beep.start()
class beeper(threading.Thread):
    def run(self):
        global bombs
        self.keeprunning = True
        while self.keeprunning:
            
            t2.forward(-1)
            tre,u = t2.pos()
            if tre <= -500:
                pu()
                write('you  lose    noob')
                x,y = pos()
                goto(x,y-10)
                write('kills:')

                x,y = pos()
                goto(x,y-10)
                write(bombs)
                x,y = pos()
                goto(x,y-10)
                write('time:')
                x,y = pos()
                goto(x,y-10)
                write(ti)
                x,y = pos()
                goto(x,y-10)
                write(ti+bombs)
                self.keeprunning = False
beep  = beeper()
beep.start()
class beeper(threading.Thread):
    def run(self):
        global bombs,f
        self.keeprunning = True
        while self.keeprunning:
            if f == 0:
                t.forward(3)
                tre = t.distance(t2)
                if tre <= 10:
                    telr()
                    bombs = bombs + 1
            else:
                t.forward(-3)
                tre = t.distance(t2)
                if tre <= 10:
                    telr()
                    bombs = bombs + 1
                #print(bombs)

beep  = beeper()
beep.start()
def r1():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            t.right(10)
    beep  = beeper()
    beep.start()
def l1():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            t.right(-10)
    beep  = beeper()
    beep.start() 

def ata():
    global bombs
    if bombs >=-1:
        t1 = t.clone()
        t1.shape('circle')  
    
        class beeper(threading.Thread):
            def run(self):
                global bombs
                self.keeprunning = True
                while self.keeprunning:
                    tre = t1.distance(t2)
                    if tre <= 10:
                        t1.ht()
                        bombs = bombs + 1
                        print(bombs)
                        telr()
                        self.keeprunning = False



        beep  = beeper()
        beep.start()
def fo():
    global f
    f = 0
def ba():
    global f
    f = 1
listen()
q.onkey(r1,'Right')
q.onkeypress(r1,'Right')
q.onkey(l1,'Left')
q.onkeypress(l1,'Left')
q.onkey(fo,'Up')
q.onkey(ba,'Down')

#q.onkey(ata,'w')
mainloop()
