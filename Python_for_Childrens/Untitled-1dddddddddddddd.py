from tkinter import*
from random import *
import turtle

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
from turtle import *
screen = turtle.Screen()
t = Turtle()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            t.color(clrname.upper())
            tre = randint(1,20)
            t.pensize(tre)
            
beep  = beeper()
beep.start()
screen.onclick(t.goto)
mainloop()    







