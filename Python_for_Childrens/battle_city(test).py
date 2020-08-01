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
ch = 1
c = 1
ca = 1
re = 1
def u():
    t.setheading(90)
    t.forward(3)
def d():
    t.setheading(-90)
    t.forward(3)
def r():
    t.setheading(0)
    t.forward(3)
def l():
    t.setheading(180)
    t.forward(3)
teleport.random_teleport(t2,1)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            tre = randint(0,3)
            if tre == 0:
                t2.forward(10)
            
            if tre == 1:
                t2.left(-90)
            
            if tre == 2:
                t2.left(90)
            
            if tre == 3:
                t2.forward(-10)
            
            ert = t2.distance(t)
            if ert <= 10:
                print('you lose')
                self.keeprunning = False
beep  = beeper()
beep.start()

def ata():
    t1 = t.clone()
    class beeper(threading.Thread):
        def run(self):
            global c,ch
            ch2 = ch
            self.keeprunning = True
            while self.keeprunning:
                t1.forward(3)

                x,y = t1.pos()
                if x >=500 or x <=-500 or y>=500 or y<=-500:
                    t1.ht()
                    #break
                    self.keeprunning = False
                tre = t1.distance(t2)
                if tre <= 10:
                    t1.ht()
                    ch = ch - 1
                    if ch <= 0:
                        ch = ch2
                        ch = ch +c
                        
                        teleport.random_teleport(t2,1)
                        c = c+1
                        print(c,ch,ch2)
                        self.keeprunning = False
                    self.keeprunning = False
                    

                
    beep  = beeper()
    beep.start()


listen()
q.onkey(u,'Up')
q.onkey(ata,'w')
q.onkey(d,'Down')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkeypress(u,'Up')
q.onkeypress(d,'Down')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')
mainloop()