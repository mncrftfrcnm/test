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
from move_turtle import * 
from printnow import *
import teleport
screen = Screen()
t = Turtle()
t.left(-90)
t.pu()
t.speed(0)
e = Turtle()
e.pu()
e.speed(0)
uy = 0
sco = 0
e.hideturtle()
e.right(90)
#e.right(90)
#teleport.random_teleport(t,2)
#p("vova")
def tu():
    u(t)
def tr():
    r(t)
def tl():
    l(t)
def ata():
    global sco
    if sco > 10:
        print("you win")
listen()
screen.onkey(tu,"Up")
screen.onkey(tr,"Right")
screen.onkey(ata,"w")
screen.onkey(tl,"Left")
screen.onkeypress(tu,"Up")
screen.onkeypress(tr,"Right")
screen.onkeypress(tl,"Left")
while True:
    e.hideturtle()
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    e.goto(x,600)
    e.showturtle()
    for yy in range(600):
        uy = 0
        e.forward(1)
        x,y = t.pos()
        e.speed(1)
        x2,y2 = e.pos()
        if x2 == x and y == y2:
            print("good")
            sco = sco + 1
            uy = 1
            break
        if x2 == x+1 and y == y2:
            print("good")
            uy = 1
            sco = sco + 1
            break
        if x2 == x-1 and y == y2:
            print("good")
            sco = sco + 1
            uy = 1
            break
        if x2 == x+2 and y == y2:
            print("good")
            sco = sco + 1
            uy = 1
            break
        if x2 == x-2 and y == y2:
            print("good")
            sco = sco + 1
            uy = 1
            break
    if uy == 0:
        print("you lose, your score is               ", sco)
        break
mainloop()