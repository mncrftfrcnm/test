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
wait_seconds = 1
WinWidth=750
screen = Screen()
t = Turtle()
t.pu()
sco = 0
def u():
    x,y = t.pos()
    t.goto(x,y+1)
def d():
    x,y = t.pos()
    t.goto(x,y-1)
listen()
screen.onkey(u,"Up")
screen.onkey(d,"Down")
screen.onkeypress(u,"Up")
screen.onkeypress(d,"Down")
def r():
    global sco
    x,y = t.pos()
    t.goto(x+1,y)
    x,y = t.pos()
    if x >300:
        print("you win, your score is",sco)
def l():
    x,y = t.pos()
    t.goto(x-1,y)
screen.onkey(l,"Left")
screen.onkey(r,"Right")
screen.onkeypress(l,"Left")
screen.onkeypress(r,"Right")

class beeper(threading.Thread):
    def run(self):
        global sco
        self.keeprunning = True
        while self.keeprunning:
            tr = Turtle()
            tr.color("white")
            tr.pu()
            tr.speed(1)
            tr.goto(700,0)
            y6= random.randint(-300,300)
            tr.right(90)
            tr.forward(y6)
            tr.left(90)
            tr.color("black")
#            tr.right(180)
            tr.speed(1)
            for x in range(1000):
                x2,y2 = tr.pos()
                x,y = t.pos()
                if y == y2:
                    tr.color("white")
                    sco = sco + 1
                    tr.forward(10)
                    break
                tr.forward(-1)
                x2,y2 = tr.pos()
                if x2 < 0:
                    print("you lose, your score is ",sco)
                    break
beep  = beeper()
beep.start()
mainloop()