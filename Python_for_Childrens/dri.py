<<<<<<< HEAD

from turtle import *
import turtle
from random import *

from tkinter import *
=======
from turtle import *
import turtle
import threading
from threading import *
import tkinter
>>>>>>> faaeda10621a017a9006732e0e35b05f454e5895
from random import *
import tkinter.messagebox
import time
import random
<<<<<<< HEAD
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
wait_seconds = 1
WinWidth=750
screen = Screen()
head = turtle.Turtle()
head.speed(1)
tr = 0
head.pu()
#s = ["turtle","circle","arrow","square","triangle"]
head.color("white")
head.setpos(0,-300)
head.color("black")
t = Turtle()
c = 0
#Screen = turtle.Screen()

def up():
    global c
    if c == 0:
        x,y = head.pos()
        head.goto(x,y+30)
        x,y = head.pos()
        head.goto(x,y-30)
listen()
screen.onkey(up,"Up")
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            
            t.pu()
            t.goto(400,-300)

            t.goto(-500,-300)
            x,y = head.pos()
            x2,y2 = t.pos()
            t.goto(0,0)            
beep  = beeper()
beep.start()
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = head.pos()
            x2,y2 = t.pos()
            if x == x2 and y == y2:
                print("game over")
            x,y = head.pos()
            x2,y2 = t.pos()
            if x2 == x and y2 == y :
                print("game over")
                        
beep2  = beeper2()
beep2.start()

mainloop()
#class beeper3(threading.Thread):
#    def run(self):
=======
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









>>>>>>> faaeda10621a017a9006732e0e35b05f454e5895
