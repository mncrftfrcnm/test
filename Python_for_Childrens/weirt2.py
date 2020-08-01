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
t.shapesize(2)
t.speed(0)
t.goto(500,500)
bul = 1
t2 = Turtle()
pat = 0
t2.pu()
t2.speed(0)
t2.goto(550,500)
t8 = Turtle()
t8.pu()
t3 = Turtle()
t3.pu()
t3.speed(0)
#t3.goto(600,900)
t3.goto(50,50)
def g(it):
    global bul
    bul = bul + 1
    tre = randint(0,1)
    d = randint(-400,400)
    if tre == 0:
        teleport.teleport(it,1,500,d)
    if tre == 1:
        teleport.teleport(it,1,-500,d)
g(t3)
def ft(x,y):
    global bul
    t1 =  t.clone()
    t1.ondrag(t1.goto)

    class beeper(threading.Thread):
        def run(self):
            global bul,pat
            self.keeprunning = True
            pat = pat +1
            while self.keeprunning:
                tre = t1.distance(t3)
                if tre <= 450:

                    class beeper2(threading.Thread):
                        
                        def run(self):
                            
                            self.keeprunning = True
                            t4 = t1.clone()
                            t4.speed(1)
                            x,y = t3.pos() 
                            t4.goto(x,y)
                            tre = t2.distance(t3)
                            if tre <= 10:
                                bul = bul - 1
                                if bul <= 0:
                                    g(t2)
                                

                                

                            
                                                            
                    beep2  = beeper2()
                    beep2.start()


                
    beep  = beeper()
    beep.start()

t.onclick(ft)


tre = input("all?: ")
t3.speed(1)
tre2 = Turtle()
tre2.pu()
tre2.shape('circle')
q.onscreenclick(tre2.goto)
class beeper(threading.Thread):
    def run(self):
        global bul,pat
        self.keeprunning = True
            
        x,y = t8.pos()
        t3.goto(x,y)
        tre = t3.distance(t8)
        if tre <= 10:
            print("you lose")
a = beeper()
a.start()

def ata():
    global bul,pat

    for sd in range(pat):
        t1 = t8.clone()
        class beeper(threading.Thread):
            def run(self):
                x,y = tre2.pos()
                t1.goto(x,y)
                ret = t1.distance(t3)
                if ret <= 10:
                    bul = bul - 1
                    if bul <=0:
                        g(t3)
        ao = beeper()
        ao.start()

listen()
q.onkey(ata,'w')
mainloop()