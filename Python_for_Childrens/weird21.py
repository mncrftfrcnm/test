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
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t.forward(1)
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
t2 = Turtle()
t2.speed(0)

shapes = ['triangle','turtle','square','circle','classic','arrow']
t2.pu()
t2.forward(-300)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t2.forward(1)
beep  = beeper()
beep.start()

def r2():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            t2.right(10)
    beep  = beeper()
    beep.start()
def l2():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            t2.right(-10)
    beep  = beeper()
    beep.start()
def ata2():
    t1 = t2.clone()
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                tre = t1.distance(t)
                if tre <=10:
                    print('1p.win')
    beep  = beeper()
    beep.start()

listen()
q.onkey(r2,'d')
q.onkeypress(r2,'d')
q.onkey(l2,'a')
q.onkey(ata2,'q')
q.onkeypress(l2,'a')

listen()
q.onkey(r1,'Right')
q.onkeypress(r1,'Right')
q.onkey(l1,'Left')
q.onkeypress(l1,'Left')

mainloop()