from turtle import *
from random import *
screen = Screen()
t=Pen()

t.speed(1)
t.shape("square")
t.pu()
t.goto(-400,0)
from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from turtle import *
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
def ats():
    t1 = t.clone()
    t1.speed(3)
    t2 = t.clone()
    t2.speed(3)
    t3 =  t.clone()
    t3.speed(3)
    x,y = t.pos()
    t1.goto(x,y+100)
    t2.goto(x+100,y+100)
    t3.goto(x-100,y+100)
    x = randint(-450,450)
    y = randint(-450,450)

    class beeper(threading.Thread):
        def run(self):
            x2 = randint(-450,450)
            y2 = randint(-450,450)
            self.keeprunning = True
            
            t1.goto(x2,y2)
            x,y = t.pos()
            t1.goto(x,y)
            t1.hideturtle()
                              
    beep  = beeper()
    beep.start()
    class beeper2(threading.Thread):
        def run(self):

            
            self.keeprunning = True
            
            while self.keeprunning:
                x,y = t1.pos()
                t2.goto(x,y)
                
                #print(x,y)               
    beep2  = beeper2()
    beep2.start()
    class beeper3(threading.Thread):
        def run(self):
            
            self.keeprunning = True
            while self.keeprunning:
                x,y = t1.pos()
                t3.goto(x,y)
            #    print(x,y)                
    beep3  = beeper3()
    beep3.start()
    
listen()
screen.onkey(ats,'w')
mainloop()