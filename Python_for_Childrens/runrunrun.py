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
q = Screen()
t = Turtle()
t.pu()
t.speed(0)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x = randint(-400,400)
            y = randint(-400,400)
            t.goto(x,y)
            t1 = t.clone()
            
                    

            class beeper(threading.Thread):
                def run(self):
                    self.keeprunning = True
                    while self.keeprunning:
                        t1.forward(10)
                            
            beep  = beeper()
            beep.start()
beep  = beeper()
beep.start()

mainloop()
    