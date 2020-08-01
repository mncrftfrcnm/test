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
from se import *
q = Screen()
t = Turtle()
t.pu()
t.speed(0)
t2 = Turtle()
t2.pu()
t2.speed(0)
t.forward(20)
def sn():
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                tre = t.distance(t2)
                if tre <= 90:
                    t1 = t.clone()
                    t1.speed(1)
                    x,y = t2.pos()
                    t1.goto(x,y)
                    tre = t1.distance(t2)
                    if tre <= 10:
                        pass
                    

                
    beep  = beeper()
    beep.start()
sn()
mainloop()