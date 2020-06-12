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
from PIL import Image
q = Screen()
t = Turtle()
t2 = Turtle()
t.pu()
t2.pu()
t.speed(0)
t2.speed(0)
s = Turtle()
s.pu()
s.speed(0)
s.goto(450,-450)
s.ht()
t.goto(-450,-450)
t2.hideturtle()
t2.goto(500,0)

t2.showturtle()
t2.speed(1)
yuy = True
gt = 0
def cd(o,p):
    global yuy,gt
    t1 = t.clone()
    def re(x,y):
        global yuy,gt
        t1.goto(x,y)
        tr = t1.distance(t2)
        if tr <= 50:
        #    print('you win')
            gt = gt+1
            if gt >= 10:
                s.st()
            t1.hideturtle()

            t2.hideturtle()
            t2.hideturtle()
            d = randint(-450,450)
            t2.goto(500, d)
            t2.showturtle()
            

    q.onscreenclick(re)
def msf(o,p):
    global yuy,gt

#    def re(x,y):
    global yuy
    #t1.goto(x,y)
    tr = 45
    if gt >= 10:
        #    print('you win')
        
            
        t2.hideturtle()
        t2.hideturtle()
        d = randint(-450,450)
        t2.goto(500, d)
        t2.showturtle()
        s.ht()
            

#    q.onscreenclick(re)
t.onclick(cd)
s.onclick(msf)
while True:
    while True:
        if yuy == True:
            t2.forward(-1)
            x,y = t2.pos()
            if x < 100:
                print('you lose')
                

                yuy = True
                break
            time.sleep(0.001)
        #else:
        #    break
mainloop()