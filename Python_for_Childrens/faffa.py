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

wait_seconds = 1
WinWidth=750
screen = Screen()
t = Turtle()
t.pu()
t.speed(0)
'''c = int(input("choose wearpon: 1)sniper 2)laser"))
if c == 1:
    t.shape("circle")
    screen.onscreenclick(t.goto)
    evil = Turtle()
    evil.pu()
#    evil.goto(-300,-300)
    evil.shape("circle")
    def u():
        x,y = t.pos()
        t.goto(x,y+1)
    def d():
        x,y = t.pos()
        t.goto(x,y-1)
    listen()
    screen.onkey(u,"Up")
    screen.onkey(d,"Down")
    screen.onkeypress(u,"Up")
    screen.onkeypress(d,"Down")
    def r():
    #    global sco
        x,y = t.pos()
        t.goto(x+1,y)
    def l():
        x,y = t.pos()
        t.goto(x-1,y)
    screen.onkey(l,"Left")
    screen.onkey(r,"Right")

    def ata():
        x,y = t.pos()
        x2,y2 = t.pos()
        if x == x or y == y:
            print("you win")
        listen()
        screen.onkey(ata,"w")
        screen.onkeypress(ata,"w")
        
mainloop()'''
tr = 0
sco = 1
ret = 1
t2 = t.clone()
def do():
    global tr,sco,ret
    t1 = t.clone()
    t1.shapesize(ret)
    t3 = t2.clone()
    t3.shapesize(ret)
    if sco == 0:
        clr = randint(0x0,0xFFFFFF)
    
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t1.color(clrname.upper())
        t3.color(clrname.upper())
#        sco = 1
    
    # if tr == 0:
    #     t1.shape("square")
    # if tr == 1:
    #     t1.shape(tre)
    def fl():
        t1.left(1)
        t3.left(-1)
    def fr():
        t1.left(-1)
        t3.left(1)
    listen()
    screen.onkey(fl,"d")
    screen.onkey(fr,"a")

    
tryo = 20
def u():
    global tryo
    x,y = t.pos()
    t.seth(90)
    t.forward(10)
    t2.seth(90)
    t2.forward(10)
def d():
    global tryo
    t.seth(-90)
    t.forward(10)
    t2.seth(-90)
    t2.forward(10)
listen()
screen.onkey(u,"Up")
screen.onkey(d,"Down")

def r():
#    global sco
    global tryo
    t.seth(0)
    t.forward(10)
    t2.seth(180)
    t2.forward(10)
    
def l():
    global tryo
    t.seth(-180)
    t.forward(10)
    t2.seth(0)
    t2.forward(10)
def c():
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="duck.ps")
screen.onkey(l,"Left")
screen.onkey(r,"Right")
screen.onkey(do,"=")
screen.onkey(c,"s")

while True:
    ert = input("1)color 2) shape 3)shapesize 4)write 5)image 6)bgcolor 7)unicode: ")
    if ert == "2":
        tre = input("what shape do you wanna: ")
        if tre:
        
            tr = 1
        t.shape(tre)
    if ert == "1":
        tre = input("what color do you wanna. If you want random color, print r: ")
        if tre != "r":
            t.color(tre)
            t2.color(tre)

            sco = 1
        if tre == "r":
            sco = 0
    if ert == "3":
        tre2 = int(input("what shapesize do you wanna: "))
        ret = tre2

    if ert == '4':
        hgf = input('write: ')
        t.write(hgf)
        t2.write(hgf)
    if ert == '5':
        ima = input('image: ')
        screen.addshape(ima)
        t.shape(ima)
        t2.shape(ima)
    if ert == '6':
        ima = input('color: ')
        screen.bgcolor(ima)
    if ert == '7':
        code = input('unicode: ')
        code = code
        t.write(code)

    
#        tryo = 20 + tre2 ** 3
mainloop() 