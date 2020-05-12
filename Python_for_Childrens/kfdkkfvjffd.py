from tkinter import*
from random import *
import turtle

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
from turtle import *
screen = turtle.Screen()
t = Turtle()
ty = 2
t.speed(0)
t.pu()
t.goto(-500,500)
t.pd()
t.goto(-500,-500)
t.goto(500,-500)
t.goto(500,500)
t.goto(-500,500)
t.pu()
t.goto(0,0)
t.pd()
t.speed(1)
score = 0
'''
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            x,y = t.pos()
            if x >= 400:
                t.setpos(x-1,y)
            if x <= 400:
                t.setpos(x+1,y)
beep  = beeper()
beep.start()'''
def u():
    global ty  
    if ty == 2:
        ty = 1
def l():
    global ty
    if ty == 1:
        ty = 4
def d():
    global ty
    if ty == 4:
        ty = 3
def r():
    global ty
    if ty == 3:
        ty = 2
listen()
screen.onkey(u, "Up")
screen.onkey(l, "Left")
screen.onkey(d, "Down")
screen.onkey(r, "Right")

def colorpen():
    clr = randint(0x0,0xFFFFFF)
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    t.color(clrname.upper())
x,y = t.pos()

while (x <= 490) and (x >= -490) and (y <= 490) and ( y >= -540):
    colorpen()
    re = randint(1,8)
    t.pensize(re)
    #up
    if ty == 1:
        x,y = t.pos()
        t.goto(x,y+10)
    #left
    if ty == 4:
        x,y = t.pos()
        t.goto(x-10,y)
    #right
    if ty == 2:
        x,y = t.pos()
        t.goto(x+10,y)
    #down
    if ty == 3:
        x,y = t.pos()
        t.goto(x,y-10)
    score = score + 10
    if score > 100 and score <  1000:
        t.speed(5)
    if score > 1000:
        t.speed(10)
    
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-250,0)
t.pendown()
t.write("GAME OVER",font=('Arial', 60,'normal'))
t.penup()
t.goto(-250,-300)
t.pendown()
t.write("your score is "+str(score),font=('Arial', 60,'normal'))

GO= input("press any key to exit: ")








