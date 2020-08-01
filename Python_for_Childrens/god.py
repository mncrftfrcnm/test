import time
import sys
#from pygame.sprite import Sprite
#from pygame.sprite import Group
from random import *
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
from telnetlib import *
from teleport import *
q = Screen()
q.addshape('fire.gif')
t = Turtle()
t.pu()
t.ht()
t.speed(0)
t2 = Turtle()
t2.pu()
t4 = Turtle()
t4.pu()
t4.ht()
t4.speed(0)
t4.goto(-500,500)
t4.shape('circle')
random_teleport(t2,0)
def storm_attack(x,y):
    t1 = t.clone()
    
    t1.goto(x,y)
    tre = t1.distance(t2)
    if tre <= 10:
        random_teleport(t2,0)
    t3 = t1.clone()
    t3.pd()
    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            x,y = t3.pos()
            t3.goto(x+5,y+45)
            time.sleep(0.1)
            
            t3.clear()
            t3.color('white')
            t3.goto(x,y)
            
            
            
            
            
    beep  = beeper()
    beep.start()
def winter_attack(x,y):
    for tyu in range(40):
        t2.forward(3)
            
            
            
            
def sun_attack(x,y):
    t4.st()
    t2.shape('fire.gif')
    time.sleep(1)
    t2.shape('classic')
    t4.ht()
    random_teleport(t2,0)
            

            
            

q.onscreenclick(storm_attack)
q.onscreenclick(sun_attack,btn = 3)
q.onscreenclick(winter_attack,btn = 2)
mainloop()