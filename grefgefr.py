from turtle import *
import turtle
import threading
from threading import *
import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
def do():
    if head.direction == "w":
        x,y = head2.pos()
        x2,y2 = head.pos()
    if x == x2+2 or y == y2+2 or x == x2+1 or y == y2+1 or x == x2 or y == y2 or x == x2+3 or y == y2+3:
        head2.color("white")
        head2.pu()
        head2.goto(1000,1000)
        head2.pu()

ter = int(input("how many monsters do you wanna:")) 
head = turtle.Turtle()
Screen = turtle.Screen()
head.shape("circle")
Screen.onclick(head.goto)
head.direction = "w"
head.pu()
def u():
    x,y = head.pos()
    head.goto(x,y+10)
def d():
    x,y = head.pos()
    head.goto(x,y-10)
def r():
    x,y = head.pos()
    head.goto(x+10,y)
def l():
    x,y = head.pos()
    head.goto(x-10,y)
def wsd():
    head.right(10)

def sd():
    head.left(10)
    
for x in range(ter):
    rt = randint(-190,190)
    tr = randint(-190,190)
    head2 = turtle.Turtle()
    head2.color("white")
    head2.pu()
    head2.setpos(rt,tr)
    head2.color("black")
    head2.pu()    




    Screen.listen()
    Screen.onkey(do,"w")
    Screen.onkey(u,"Up")
    Screen.onkey(d,"Down")
    Screen.onkey(l,"Left")
    Screen.onkey(r,"Right")
    Screen.onkey(wsd,"d")
    Screen.onkey(sd,"a")
    ytu = input("is it ok")
mainloop()
#ty = input("oooo")








