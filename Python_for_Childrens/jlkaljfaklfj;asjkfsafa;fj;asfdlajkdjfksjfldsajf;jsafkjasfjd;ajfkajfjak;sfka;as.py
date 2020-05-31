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
ert = "circle"
screen = Screen()
tre = 0
tr = 1
rt = 1
t4 = 1
t = Pen()
t.pu()
screen.onscreenclick(t.goto)

def ata2():
    t1 = t.clone()
    t1.shape("square")
    class beeper2(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                ert = randint(0,1)
                if ert == 0:
                    t2 = t1.clone()
                    t2.speed(1)
                    #t2.shape("circle")
                    x = randint(-300,300)
                    y = randint(-300,300)
                    t2.goto(x,y)
                    t2.hideturtle()

    beep2 = beeper2()
    beep2.start()
def ata():
    t1 = t.clone()
    t1.shape("square")
    class beeper2(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                ert = randint(0,10)
                if ert == 0:
                    t2 = t1.clone()
                    t2.speed(1)
                    t2.shape("circle")
                    x = randint(-300,300)
                    y = randint(-300,300)
                    t2.goto(x,y)
                    t2.hideturtle()
                
    beep2 = beeper2()
    beep2.start()
listen()
screen.onkey(ata,'u')
screen.onkey(ata2,'i')
mainloop()     