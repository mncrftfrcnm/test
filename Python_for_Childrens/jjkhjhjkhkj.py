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
# q = Screen() 
# t = Turtle()
# t.speed(1)
# t.pu()
t2 = Pen()
#t2.pu()
#t2.hideturtle()

t2.goto(450,450)
tr = 0
class beeper(threading.Thread):
    def run(self):
        global tr
        self.keeprunning = True
        while self.keeprunning:
            if tr == 0:
                t2.goto(0,0)
                if tr == 1:
                    print("I")
                else:
                    print("u")
            #ret = distance(t,t2)
                           
beep  = beeper()
beep.start()

def trrtr():
    t = Pen()
    class beeper(threading.Thread):
        
        t.pu()
        q.onscreenclick(t.goto)
        def run(self):
            global tr
            self.keeprunning = True
            while self.keeprunning:
                ret = distance(t,t2)
                
                if ret < 300:
                    t1 = t.clone()
            #        t1.hideturtle()
                    x,y = t2.pos()
                    t1.goto(x,y)
                    x,y = t1.pos()
                    x2,y2 = t2.pos()
                    if x == x2 and y == y2:
                        tr = 1            

    beep  = beeper()
    beep.start()




listen()
q.onkey(trrtr,'w')
# if ret > 12:
#     print("K")
#   TurtleGraphicsErrorTurtleGraphicsError print("P")
#t.onclick(t.shapesize)
#t.onclick(t.color)
mainloop()
