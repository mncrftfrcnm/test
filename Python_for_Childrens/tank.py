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
t.speed(1)
t3 = Turtle()
t3.pu()
t3.shape('circle')
t3.ondrag(t3.goto,btn=2)

def movenow(x,y):

            #self.keeprunning = True
#ert = 0
    t.goto(x,y)


                
q.onscreenclick(movenow)
    

tanker = 0
atack = 1
def ata(x,y):
    global tanker,atack
    if atack > 0:
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                first = randint(37,32000)
                second = randint(100,1000)
               # PlaySound("C:\windows\media\Ring02.wav",False)
                t1 = t.clone()
                if tanker == 0:
                    x,y = t3.pos()
                    t1.goto(x,y)
                
        beep  = beeper()
        beep.start()


t3.onrelease(ata,btn = 2)
mainloop()
