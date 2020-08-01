
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
t = Turtle()
t.pu()
t.speed(0)
t2 = Turtle()
t2.pu()
random_teleport(t2,1)
ch = 1
ta = 10
pu()
ht()
goto(0,500)
write(ta)
def u():
    t.seth(90)
    t.forward(3)
def d():
    t.seth(-90)
    t.forward(3)
def l():
    t.seth(180)
    t.forward(3)
def r():
    t.seth(0)
    t.forward(3)
def trible_attack():
    global ta,ch
    if ta >0:
        ta = ta - 1
        clear()
        write(ta)
        t3 = t.clone()
        t1 = t.clone()
        t2 = t.clone()
        t1.right(0)
        t2.right(45)
        t3.left(45)
        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                
                t1.forward(10)
                time.sleep(0.1)
                t1.ht()
                    
        beep  = beeper()
        beep.start()
        
        class beeper2(threading.Thread):
            def run(self):
                self.keeprunning = True
                t2.right(10)
                t2.forward(10)
                time.sleep(0.1)
                t2.ht()
                
                    
        beep2  = beeper2()
        beep2.start()
        
        class beeper3(threading.Thread):
            def run(self):
                self.keeprunning = True
                t3.right(-10)
                t3.forward(10)
                time.sleep(0.1)
                t3.ht()
                    
        beep3  = beeper3()
        beep3.start()
    #t1 = t.clone()
#    t2 = t.clone(
def ata():
    global ch
    t1 = t.clone()
    t1.right(0)

    class beeper(threading.Thread):
        def run(self):
            self.keeprunning = True
            
            t1.forward(10)
            time.sleep(0.1)
            t1.ht()
                
    beep  = beeper()
    beep.start()
listen()
q.onkey(trible_attack,'w')
q.onkey(ata,'q')
q.onkey(u,'Up')
q.onkey(d,'Down')
q.onkey(l,'Left')
q.onkey(r,'Right')
q.onkeypress(u,'Up')
q.onkeypress(d,'Down')
q.onkeypress(l,'Left')
q.onkeypress(r,'Right')
q.onkey(l,'Left')
q.onkey(r,'Right')
mainloop()