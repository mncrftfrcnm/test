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
#t.color('green')
t.speed(1)
t.pu()
t.forward(2)
t.speed(1)
u = 0
def l():
    global u
    u = 0
def r():
    global u
    u = 1
    print(u)
def ata():
    global u
    print(u)
    if u == 1:
        t1 = t.clone()
        x,y = t.pos()
        t1.goto(x,y+7)
        time.sleep(0.1)

        x,y = t.pos()
        t1.goto(x+7,y)
        time.sleep(0.1)
        x,y = t.pos()
        t1.goto(x,y-7)
        time.sleep(0.1)
        t1.hideturtle()
    if u == 0:
        t1 = t.clone()
        t1.goto(500,0)
        t1.hideturtle()
            


listen()
q.onkey(l,'1')
q.onkey(r,'2')
q.onkey(ata,'w')
mainloop()