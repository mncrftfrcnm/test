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
t.speed(1)
t.left(90)
t2 = Turtle()
yuy = True
sco = 0
t2.speed(0)
#t2.left(90)
t.pu()
t2.pu()
t2.goto(500,0)
t2.speed(0)
def f():
    t.forward(10)
def b():
    t.forward(-10)
def l():
    t.left(10)

def r():
    t.left(-10)
def ata():
    global sco
    re = t.distance(t2)
    if re <= 90:

        t1 = t.clone()
        x,y = t2.pos()
        t1.goto(x,y)
        x,y = t2.pos()
        x2,y2 = t1.pos()
        if x == x2 and y == y2:
            sco = sco +1
            t1.hideturtle()
            t2.hideturtle()
            t2.hideturtle()
            d = randint(-450,450)
            t2.goto(500, d)
            t2.showturtle()
            
            t1 = t2.clone()
        t1.hideturtle()
        
        
listen()
q.onkey(ata,'w')
q.onkey(r,'Right')
q.onkey(l,'Left')
q.onkey(f,'Up')
q.onkey(b,'Down')
while True:
    while True:
        if yuy == True:
            t2.forward(-1)
            re = t2.distance(t)
            if re <= 10:
                t.speed(0)
                t.home()
                t.speed(1)

            x,y = t2.pos()
            if x < 100:
                print('you lose, your score is',sco)
                

                yuy = False
                break
                break
            time.sleep(0.001)
mainloop()