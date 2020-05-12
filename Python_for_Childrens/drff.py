from turtle import *
import turtle
import threading
from threading import *
import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
h = 100
head = turtle.Turtle()
Screen = turtle.Screen()
head.shape("circle")
head.direction = "w" 
head.pu()
#Screen.onscreenclick(head.goto)
head2 = turtle.Turtle()
#Screen = turtle.Screen()
head2.shape("circle")
head.direction = "w" 
head2.pu()
head2.goto(500,500)
head2.speed(1)
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = head.pos()
            x2,y2 = head2.pos()
            if h < 50:
                head2.speed(5)
            if x == x2 or y == y2:
                print("you lose") 
beeb2 = beeper2()
beeb2.start()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = head.pos()
            head2.goto(x,y)
beeb = beeper()
beeb.start()
def powd():
    global h
    h = h - 1
    if h < 50:
        head2.speed(10)
    if h <= 0:
        print("you win")
def u():
    x,y = head.pos()
    head.forward(10)
def d():
    x,y = head.pos()
    head.forward(-10)
def r():
    x,y = head.pos()
    head.right(10)
def l():
    x,y = head.pos()
    head.left(10)
Screen.listen()
Screen.onkey(u,"Up")
Screen.onkey(powd,"w")
Screen.onkey(d,"Down")
Screen.onkey(l,"Left")
Screen.onkey(r,"Right")

mainloop()