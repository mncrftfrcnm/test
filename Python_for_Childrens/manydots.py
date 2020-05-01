from random import *
from turtle import *
from threading import*
from time import *
t = Pen()
#t.hideturtle()
t.speed(0)
g = 10
clr = 0

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
wait_seconds = 1
WinWidth=750

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            PlaySound("C:\windows\media\Ring02.wav",False)
            
beep  = beeper()
beep.start()
trt = int(input("how many dots do you want:"))


for x in range(trt):
    
    
    t.right(90)
    t.dot()
    t.forward(x+g)
    g = g+ 10
clr = randint(0x0,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
        
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

t.color(clrname.upper())

    
    
    



hh = input("yy")





