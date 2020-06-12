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
q = Screen() 
t = Turtle()
t.speed(1)
t.pu()
#t.goto(100,100)
t.color("white")
t2 = Turtle()
t2.pu()
t2.speed(0)
t2.hideturtle()
u = 0
class beeper2(threading.Thread):
    def run(self):
        global u
        self.keeprunning = True
        while self.keeprunning:
            if u == 0:
          #      t2.hideturtle()
                print("O")
                c = randint(-450,450)
                v = randint(-450,450)
                t.goto(c,v)
                t2.showturtle()
                u = 1
            x,y = t.pos()
            x2,y2 = t2.pos()
            t.goto(x2,y2)
           # print(x,y)
            if x == x2 and y == y2:
                u = 0
            

            
beep2 = beeper2()
beep2.start()
class beeper3(threading.Thread):
    def run(self):
        global u
        self.keeprunning = True
        while self.keeprunning:
            t.forward(1)
            

            
beep3 = beeper3()
beep3.start()

def r():
    print("O")
    t.left(90)
    
listen()
q.onkey(r,'w')
mainloop()