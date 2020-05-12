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
import os









Screen = Screen()
head = turtle.Turtle()
head.shape("circle")
Screen.onclick(head.goto)
head.pu()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = head.pos()
            if x > 100 and x < 200:
                head.shape("turtle")
            elif x > 200:
                head.shape("classic")
            elif x < 100 and x > 50:
                head.shape("circle")
            else:
                head.shape("triangle")
beep  = beeper()
beep.start()
mainloop()