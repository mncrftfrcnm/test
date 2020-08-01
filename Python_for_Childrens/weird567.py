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
s = 1
ch = 1
th = 2
sco = 0
def g():
    global s,ch,th,sco
    ch = ch + th
    s = 1
    th = th + 1
    tre = sco + 1
    print(tre)
    sco = sco + 1
    teleport.random_teleport(t2,0)
def ata(x,y):
    global ch
    ch = ch - 1
    if ch <= 0:
        g()

class beeper(threading.Thread):
    def run(self):
        global s,th,sco
        self.keeprunning = True
        while self.keeprunning:
            t2.shapesize(s)
            s  = s + 1
            if s >=8:
                print('you lose',sco)
            time.sleep(1)
            
    
            
beep  = beeper()
beep.start()

t2.onclick(ata)
mainloop()