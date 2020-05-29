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
from PIL import Image 
t = Turtle()
tr = 10
gh = 100
t.pu()
# s1  = Turtle()
# s1.shape("circle")
# s2  = Turtle()
# s2.shape("circle")
t.speed(1)
e = Turtle()
e.speed(1)
e.pu()
e.forward(300)
screen = Screen()
class beeper(threading.Thread):
    def run(self):
        global gh
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            e.goto(x,y)
            x2,y2 = e.pos()
            x,y = t.pos()
            
            if x == x2 and y == y2:
                gh = gh - 1
                if gh <= 0:
                    print("you lose")
beep  = beeper()
beep.start()

def ata():
    global tr
    
    t1 = t.clone()
    cv = randint(0,2)
    if cv == 0 or cv == 1:
        t.forward(-10)
        t.forward(10)
        for x in range(50):
            t1.forward(1)
            x,y = t1.pos()
            x2,y2 = e.pos()
            if x == x2 and y == y2:
                tr = tr - 1
                print(tr)
        t1.hideturtle()
    
    if cv == 2:
        
        t1.hideturtle()
        ert = randint(0,300)


        x,y = t1.pos()
        x2,y2 = e.pos()
        t1.goto(x2,300)
        t1.showturtle()
        t1.right(90)

        
        for x in range(500):
            t1.forward(1)
            x,y = t1.pos()
            x2,y2 = e.pos()
            if x == x2 and y == y2:
                tr = tr - 1
                print(tr)
                if tr <= 0:
                    print("you win")
        t1.hideturtle()
def r():
    t.forward(10)
def l():
    t.forward(-10)
def u():
    x,y = t.pos()
    t.goto(x,y+30)
    x,y = t.pos()
    t.goto(x,y-30)
    

    
#        print("L")
listen()
screen.onkey(ata,"w")
screen.onkey(l,"Left")
screen.onkey(r,"Right")
screen.onkey(u,"Up")
mainloop()