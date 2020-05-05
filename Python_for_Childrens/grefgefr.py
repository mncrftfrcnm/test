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
mn = 3

def do3():
    global mn
    if mn > 0:
        head2.color("white")
        head2.pu()
        head2.goto(1000,1000)
        mn = mn - 1
    else:
        pass
def do2():
    
    x,y = head2.pos()
    x3,y3 = head3.pos()
    if x == x3+2 or y == y3+2 or x == x3+1 or y == y3+1 or x == x3 or y == y3 or x == x3+3 or y == y3+3:
        head2.color("white")
        head2.pu()
        head2.goto(1000,1000)
        head2.pu()
def do():
    
    x,y = head2.pos()
    x2,y2 = head.pos()
    if x == x2+2 or y == y2+2 or x == x2+1 or y == y2+1 or x == x2 or y == y2 or x == x2+3 or y == y2+3 or x == x2+4 or y == y2+4 or x == x2+5 or y == y2+5 or x == x2 or y == y2 or x == x2+6 or y == y2+6:
        head2.color("white")
        head2.pu()
        head2.goto(1000,1000)
        head2.pu() 
def do4():
    
    x,y = head2.pos()
    x2,y2 = head.pos()
    head = turtle.Turtle()
    if x == x2+2 or y == y2+2 or x == x2+1 or y == y2+1 or x == x2 or y == y2 or x == x2+3 or y == y2+3 or x == x2+4 or y == y2+4 or x == x2+5 or y == y2+5 or x == x2 or y == y2 or x == x2+6 or y == y2+6:
        head2.color("white")
        head2.pu()
        head2.goto(1000,1000)
        head2.pu() 
ter = int(input("how many monsters do you wanna:")) 
head = turtle.Turtle()
Screen = turtle.Screen()
head.shape("circle")
head.direction = "w"
head.pu()
head.color("blue")
head.left(90)
head3 = turtle.Turtle()
head3.shape("circle")
Screen.onclick(head3.goto)
head3.pu()
head3.color("red")
def u():
    x,y = head.pos()
    head.forward(10)
def d():
    x,y = head.pos()
    head.forward(-10)
def r():
    x,y = head.pos()
    head.right(90)
    head.forward(10)
    head.left(90)
def l():
    x,y = head.pos()
    head.left(90)
    head.forward(10)
    head.right(90)
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
    Screen.onkey(do,"2")
    Screen.onkey(u,"Up")
    Screen.onkey(d,"Down")
    Screen.onkey(l,"Left")
    Screen.onkey(r,"Right")
    Screen.onkey(wsd,"d")
    Screen.onkey(do2,"1") 
    Screen.onkey(do3,"v")
#    mainloop()
    #ytu = input("is it ok")
mainloop()
#ty = input("oooo")








