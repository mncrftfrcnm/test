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
def ft(x,y):
    t.goto(x,y)
    t1 = t.clone()
    t1.shape(choice(shapes))
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                x,y = t1.pos()
                t1.goto(x,y-10)
                x,y = t1.pos()
                if y <= -500:
                    self.keeprunning = False
                
                
    beep  = beeper()
    beep.start()
t.ondrag(ft)
mainloop()