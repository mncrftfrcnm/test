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
t.speed(0)
t.pu()
t2 = Turtle()
t2.speed(0)
t2.shape("triangle")
t2.pu()
t.right(-90)
t2.right(90)
t2.speed(0)
t2.forward(-400)
t2.speed(0)


class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            t2.goto(x,y+400)  
            #time.sleep(0.1)          
beep  = beeper()
beep.start()

#q.onscreenclick(g)
def r(x,y):
    x,y = t.pos()

    t.goto(x+10,y)
ri = Turtle()
ri.pu()
ri.speed(0)
ri.goto(510,-400)
ri.shapesize(3)
ri.onclick(r)
def l(x,y):
    x,y = t.pos()
    t.goto(x-10,y)
le = Turtle()
le.pu()
le.speed(0)
le.goto(390,-400)
le.right(180)
le.shapesize(3)
le.onclick(l)
bul = 1
ch = 10
def ata(x,y):
    global bul
    if bul == 1:
        bul = bul - 1
        t1 = t.clone()
        class beeper3(threading.Thread):
            def run(self):
                global bul,ch
                self.keeprunning = True
            
                x,y = t1.pos()
                t1.goto(x,y+400)
                tre = t1.distance(t2)
                if tre <= 10:
                    ch = ch - 1
                    if ch <= 0:
                        print("P")
                #time.sleep(0.1)
                    clr = randint(0x0,0xFFFFFF)
                
                    clrtxt = str(hex(clr))
                    clrname = clrtxt.replace('0x','#')
                    
                    while len(clrname) != 7:
                        clrname = clrname.replace('#','#0')
                    Screen().bgcolor(clrname)
                t1.ht()   
                bul = bul + 1       
        beep3  = beeper3()
        beep3.start()


at = Turtle()
at.shape('square')
at.pu()
at.speed(0)
at.goto(450,-400)
at.right(180)
at.shapesize(3)
at.onclick(ata)
class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            print("O")
                      
            t1 = t2.clone()
            t1.speed(1)
            x,y = t1.pos()
            x2,y2 = t2.pos()
            t1.goto(x,0)
            tre = t1.distance(t)
            t1.ht()
            if tre <= 10:
                beep.keeprunning = False
                self.keeprunning = False
                ht()
                pu()
                x,y = pos()
                goto(x,y+200)
                pensize(450)
                write("you lose")
                time.sleep(1)
                Screen().bgcolor('black')

beep2  = beeper2()
beep2.start()

mainloop()