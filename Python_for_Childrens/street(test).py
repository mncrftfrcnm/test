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
from se import *
q = Screen()
t = Turtle()
listen()
t2 = Turtle()
t.pu()
t2.pu()
t.speed(0)
t.goto(0,90)
t2.speed(0)
t2.goto(90,0)
t2.shapesize(10)
t3 = Turtle()
t4 = Turtle()
t3.pu()

t4.pu()
t3.speed(0)
t3.goto(-123,43)
t4.speed(0)
t3.goto(-90,0)
t4.shapesize(10)
def fight(cha):
    
    if cha == 't':
        global far
        e = Turtle()
        e.pu()
        e.forward(-30)
        l = 10
        far = 100
        def j():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x,y+100)
            t.goto(x,y)
            t.speed(0)
            iu = t.distance(e)
            if iu <= 10:
                far = far - 1
                print(far)
        def f():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x+1,y)
            iu = t.distance(e)
            if iu <= 10:
                far = far - 1
                print(far)
        def b():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x-1,y)
            iu = t.distance(e)
            if iu <= 10:
                far = far - 1
                print(far)
        q.onkey(j,'Up')
        q.onkeypress(f,'Left')
        q.onkeypress(b,'Right')
    if cha == 't2':
  #      global far
        e = Turtle()
        e.pu()
        e.forward(-30)
        l = 10
        far = 100
        def j():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x,y+100)
            t.goto(x,y)
            t.speed(0)
        def f():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x+1,y)

        def b():
            global far
            x,y = t.pos()
            t.speed(1)
            t.goto(x-1,y)
        def ata():
            global far
            t1 = t.clone()
            for m in range(100):
                t1.forward(1)
                iu = t1.distance(e)
                if iu <= 10:
                    far = far - 1
                    print(far)
            t1.ht()
        q.onkey(j,'Up')
        q.onkeypress(f,'Left')
        q.onkeypress(b,'Right')
        q.onkey(ata,'w')

def cd():
    Screen().bgcolor("black")
    t2.goto(700,700)
    t3.goto(700,700)
    t4.goto(700,700)
    #t2.goto(700,700)
    
    Screen().bgcolor("white")
def fort(x,y):


    cd()
    t.goto(0,0)

    fight('t')
t.onclick(fort)
def fort2(x,y):


    cd()
    t.goto(0,0)

    fight('t2')
t2.onclick(fort2)    
mainloop()