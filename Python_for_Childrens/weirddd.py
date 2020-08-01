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
t3 = Turtle()
t3.pu()
t2 = Turtle()
t3.speed(0)
t3.shape('circle')
t2.pu()
t2.forward(100)
q.onscreenclick(t3.goto)
def tel():
    tre = randint(0,3)
    if tre == 0:
        x = -300
        y = randint(-500,500)
    
    if tre == 1:
        x = 300
        y = randint(-500,500)
    if tre == 2:
        y = -300
        x = randint(-500,500)
    if tre == 3:
        y = 300
        x = randint(-500,500)
    teleport.teleport(t2,1,x,y)
tel()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            #t2.goto(x/2,y-2)
            
            x,y = t.pos()
            t2.goto(x,y)
            
            tre = t.distance(t2)
            if tre <= 10:
                print('you lose')
                







beep  = beeper()
beep.start()
def ata():
    tre = t3.distance(t2)
    if tre <= 15:
        tel()
listen()
q.onkey(ata,'w')
mainloop()