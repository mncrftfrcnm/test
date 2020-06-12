from turtle import *
from random import *
t=Pen()
t.shape("square")
t.pu()

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
wait_seconds = 1
WinWidth=750

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:

            x,y = t.pos()
            x,y4 = t.pos()
            while y > 0:
                x,y = t.pos()
                t.forward(-1)

beep  = beeper()
beep.start()
t.left(90)
t.ondrag(t.goto)

mainloop()