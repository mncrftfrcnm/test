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
import sys
from PIL import Image
q = Screen()


def ata(x,y):
    t = Turtle()
    t.pu()
    t.speed(0)
    t.speed(0)

    t.goto(x,y)
    class beeper(threading.Thread):

        def run(self):
            self.keeprunning = True
            while self.keeprunning:

                x2,y2 = t.pos()
                while True:
                    x,y = t.pos()
                    t.goto(x,y-1)
                    x,y = t.pos()
                    if y <=0:
                        break

                t.speed(1)
                y2 = y2 -5
                for x in range(3):
                    y2 = y2 / 2
                    t.goto(x2,y2)
                    t.goto(x2,0)
                    t.goto(x2,y2)
                    t.goto(x2,0)
                t1 = t.clone()
                t1.speed(0)
                t1.right(180)
                t.speed(0)
                t.left(0)
                #t1.speed(1)
                for oi in range(23):
                    for uy in range(10):
                        x,y = t1.pos()

                        t1.goto(x+1,y+1)
                        x,y = t.pos()
                        t.goto(x-1,y+1)

                        t2 = t.clone()
                        t2.speed(0)
                        t2.forward(50)
                        t2 = t1.clone()
                        t2.speed(0)
                        t2.forward(50)
                        
                    for uy in range(10):
                        x,y = t1.pos()
                        t1.goto(x+1,y-1)
                        x,y = t.pos()
                        t.goto(x-1,y-1)

                        t2 = t.clone()
                        t2.speed(0)
                        t2.forward(50)
                        t2 = t1.clone()
                        t2.speed(0)
                        t2.forward(50)
                

    beep  = beeper()
    beep.start()

q.onscreenclick(ata)
mainloop()