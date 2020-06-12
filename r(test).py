from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import turtle
from turtle import *
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep

q = Screen()
t = Pen()
t.speed(0)
#t.pu()
ti = 0
class beeper2(threading.Thread):
    def run(self):
        global ti
        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            ti= ti +1
                            
beep2  = beeper2()
beep2.start()


class beeper(threading.Thread):
    def run(self):
        global ti
        self.keeprunning = True
        while self.keeprunning:
            #print("O")
            t.forward(6)
            x,y = t.pos()
            if x >= 300 or y >= 300 or y <= -300 or x<= -300:
                print("your score is", ti)
                self.keeprunning = False                
beep  = beeper()
beep.start()


def l():
    t.left(10)
def r():
    t.left(-10)
listen()

q.onkey(l,'Left')
q.onkey(r,'Right')
#q.onkeypress(f1,'w')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')

mainloop()