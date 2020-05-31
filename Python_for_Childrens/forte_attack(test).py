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
e = 0
x = 0
screen = Screen()
t = Pen()
t.pu()
def ata():
    class beeper2(threading.Thread):
        def run(self):
            self.keeprunning = True
            while self.keeprunning:
                t1 = t.clone()

listen()
screen.onkey(ata,'q')
#
mainloop()