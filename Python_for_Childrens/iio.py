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
from PIL import Image
q = Screen()
q.addshape('grass.gif')
q.addshape('fire.gif')
q.addshape('mangal.gif')

q.addshape('potato.gif')
q.addshape('grasspotato.gif')
e = Turtle()
e.pencolor('white')
e.speed(0)
m = Turtle()
m.pencolor('white')
m.shape('mangal.gif')
m.speed(0)
e.goto(-670,0)
ter = 'grass.gif'
t2 = Turtle()
t2.pu()
t2.goto(400,400)
t2.shape('potato.gif')
ytu = 0
def tel(x,y):
    e.goto(-670,0)
e.onclick(tel,btn = 3)
def cd2(x,y):
    global ter,ytu
    ter = 'potato.gif'
    ytu = 1
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            ef = randint(-10000,10000)
            if ef == 10:
                t1 = e.clone()
                t1.color('white')
                e.forward(3)
                x,u = e.pos()
                if x > 500:
                    tel()
           #     if 
            
beep  = beeper()
beep.start()

t2.onclick(cd2)
t3 = Turtle()
t3.pu()
t3.goto(400,350)
t3.shape('grass.gif')
def cd3(x,y):
    global ter,ytu 
    ter = 'grass.gif'
    ytu = 0

t3.onclick(cd3)
def j(x,y):
    global ter,ytu
    t = Turtle()
    t.pu()
    t.shape(ter)
    t.speed(0)
    t.speed(0)
    t.goto(x,y)
    x2,y2 = t.pos()
    class beeper(threading.Thread):
        def run(self):
            global ytu
            self.keeprunning = True
            while self.keeprunning:
                
                u,i = t.pos()
                t.goto(u,i -1)
                tre = t.distance(m)
                if tre <= 30:
                    t.shape('fire.gif')
                    time.sleep(1)
                    t.ht()
                    break

                if i <=0:
                    tre = randint(2,3)
                    if tre == 3 and ytu == 1:
                        t.shape('grasspotato.gif')

                    if tre ==3:
                        yt = randint(2,6)
                        for h in range(yt):
                            time.sleep(1)
                            t1 = t.clone()
                            u,i = t1.pos()
                            t1.goto(u,h*10)
                    self.keeprunning = False

    beep = beeper()
    beep.start()
q.onscreenclick(j)
mainloop()