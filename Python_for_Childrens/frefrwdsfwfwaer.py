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

screen = turtle.Screen()
#screen.setup(1000,1000)
screen.bgpic('BG.gif')

q.addshape("catBG.gif") 
t101 = Turtle()
t101.pu()
t100 = Turtle()
t100.pu()
t101.goto(450,-450)
t101.shapesize(3)
t100.goto(470,-450)
t100.shapesize(3)
t100.shape('square')
t = Turtle()
#t.shape("catBG.gif")
t.speed(0)
#t.pu()
t3 = Turtle()
t3.pu()
t3.speed(0)
t3.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t3.goto(c,v)
t3.color("red")
t3.shape("circle")
t3.st()
t4 = Turtle()
t4.pu()
t4.speed(0)
t4.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t4.goto(c,v)
t4.color("red")
t4.shape("circle")
t4.st()
t4 = Turtle()
t4.pu()
t4.speed(0)
t4.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t4.goto(c,v)
t4.color("red")
t4.shape("circle")
t4.st()
t5 = Turtle()
t5.pu()
t5.speed(0)
t5.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t5.goto(c,v)
t5.color("red")
t5.shape("circle")
t5.st()
t6 = Turtle()
t6.pu()
t6.speed(0)
t6.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t6.goto(c,v)
t6.color("red")
t6.shape("circle")
t6.st()

#t.goto(100,100)
#t.color("white")
t2 = Turtle()
t2.pu()
t2.speed(0)
t2.hideturtle()
c = randint(-450,450)
v = randint(-450,450)
t2.goto(c,v)
t2.shape("circle")
t2.st()
t.pu()
#Screen().bgcolor('black')
yty = 0
def u8():
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    qew = randint(0,5)
    t.color(clrname.upper())
    t.pensize(qew)
def u9(x,y):
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())
q.onkey(u8,'q')
def h():
    global yty
    if yty >= 1:
        t.home()
        yty = yty - 1
        clear()
        write(yty,font=("Calibri", 20, "bold"))
screen.onkey(h,'t')
def ata():
    global yty
    if yty >= 1:
        t.speed(0)
        t.forward(100)
        yty = yty - 1
        clear()
        write(yty,font=("Calibri", 20, "bold"))
#    f.right(90)
q.onkey(ata,'w')
def r():
#    f.right(90)
    t.right(90)
def ata2(x,y):
    global yty
    if yty >= 1:
        t.speed(0)
        t.forward(100)
        yty = yty - 1
        clear()
        write(yty,font=("Calibri", 20, "bold"))
#    f.right(90)
q.onkey(ata,'w')
def r2(x,y):
#    f.right(90)
    t.right(90)
t101.onclick(r2)
t100.onclick(ata2)

def cd():
    t3.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t3.goto(c,v)
    t3.st()
    t4.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t4.goto(c,v)
    t4.st()
    t4.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t4.goto(c,v)
    t4.st()
    t5.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t5.goto(c,v)
    t5.st()
    t6.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t6.goto(c,v)
    t6.st()
def ui():
    global yty
    yty = yty+1
    t2.hideturtle()
    c = randint(-450,450)
    v = randint(-450,450)
    t2.goto(c,v)
    t2.st()
    pu()
    clear()
    ht()
    write(yty,font=("Calibri", 10, "bold"))
listen()
q.onkey(r,'Right')
iooi = 0
while True:
    
    x,y = t2.pos()
#    t2.color('black')
#    t3.right(90)

    
    x2,y2 = t.pos()
    if x2 >= 450:
        t.goto(-x2,y2)
    if x2 <= -450:
        t.goto(-x2,y2)
    if y2 >= 450:
        t.goto(x2,-y2)
    if y2 <= -450:
        t.goto(x2,-y2)
    tr = t.distance(t2)
    if tr <= 10:
        ui()
        cd()
#    f.forward(1)
    t.forward(1)
    tr = t.distance(t2)
    if tr <= 10:
        ui()
        cd()
    tr = t.distance(t3)
    if tr <= 10:
        ht()
        pu()
        clear()
        write('your score is:')
        x,y = pos()
        goto(x,y-10)
        write(yty)
        break
    tr = t.distance(t4)
    if tr <= 10:
        ht()
        pu()
        clear()
        write('your score is:')
        x,y = pos()
        goto(x,y-10)
        write(yty)
        break
    tr = t.distance(t5)
    if tr <= 10:
        ht()
        pu()
        clear()
        write('your score is:')
        x,y = pos()
        goto(x,y-10)
        write(yty)
        break
    tr = t.distance(t6)
    if tr <= 10:
        ht()
        pu()
        clear()
        write('your score is:')
        x,y = pos()
        goto(x,y-10)
        write(yty)
        break

mainloop()