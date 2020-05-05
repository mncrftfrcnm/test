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
head = turtle.Turtle()
head.color("white")
head.goto(0,-300)
head.color("black")
ert = ["circle", "turtle", "classic"]
Screen = turtle.Screen()
head.shape("circle")
head.direction = "w"
head.pu()
def f():
    x,y = head.pos()
    head.goto(x+20,y)
def b():
    x,y = head.pos()
    head.goto(x-20,y)
def u():
    x,y = head.pos()
    head.goto(x+10,y+10)
    x,y = head.pos()
    head.goto(x+10,y-10)
    
listen()
Screen.onkey(f, "Right")
Screen.onkey(b, "Left")
Screen.onkey(u, "Up")
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            head.left(10)

beep2  = beeper2()
beep2.start()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            head2 = turtle.Turtle()
            head2.pu()
            head2.color("white")
            head2.shape(choice(ert))
            jhk = randint(1,10)
            head2.shapesize(jhk)
            head2.right(180) 
            der = randint(0,200)
            red = randint(0,200)
            head2.setpos(der,red)
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            head2.color(clrname.upper())
            head2.forward(700)
            ui = randint(0,2)
            time.sleep(ui)

beep  = beeper()
beep.start()
mainloop()









