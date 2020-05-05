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
Screen = turtle.Screen()
head.shape("circle")
head.direction = "w"
head.color("blue")
head.pu()
Screen.onclick(head.goto)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t = Pen()
            t.color("white")
            t.pu()
            t.right(180)
            t.forward(500)
            tt = randint(-500,500)
            ttt = randint(-500,500)
            t.setpos(tt,ttt)
            t.color("black") 
            x,y = t.pos()
            x2,y2 = head.pos()
            if x == x2 or y == y2:
                print("you lose")
beep  = beeper()
beep.start()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t = Pen()
            t.pu()
            t.right(180)
            t.forward(500)
            tt = randint(-500,500)
            ttt = randint(-500,500)
            t.setpos(tt,ttt) 
            x,y = t.pos()
            x2,y2 = head.pos()
            if x == x2 or y == y2:
                print("you lose")
beep  = beeper()
beep.start()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            t = Pen()
            t.pu()

            tt = randint(200,500)
            ttt = randint(-500,500)
            t.setpos(tt,ttt) 
            x,y = t.pos()
            x2,y2 = head.pos()
            t.right(180)
            t.forward(500)
            if x == x2 or y == y2:
                print("you lose")
beep  = beeper()
beep.start()
'''class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            x2,y2 = head.pos()
            if x == x2 or y == y2:
                print("you lose")
beep  = beeper()
beep.start()'''
mainloop()
































































































































