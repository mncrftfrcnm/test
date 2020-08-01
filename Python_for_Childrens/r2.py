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
import teleport
import all_my_commands
q = Screen()
t = Turtle()
t.pu()
t.speed(0)
f = 0
class beeper(threading.Thread):
    def run(self):
        global f
        self.keeprunning = True
        while self.keeprunning:
            t.forward(f)
            f = f + 1
            
            
beep  = beeper()
beep.start()
mainloop()