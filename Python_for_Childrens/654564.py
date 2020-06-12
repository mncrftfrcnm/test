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
t9 = Turtle()
t9.pu()
t9.goto(100,100)
t9.color("white")
yt9 = 1

ht()
x,y = pos()
goto(x,y+40)
write("you die today")
Screen().bgcolor('black')
t6 = Turtle()
t6.shape("square")
t6.speed(0)
t6.goto(-400,450)

t6.pu()
t6.color("green")
t7 = Turtle()
t7.speed(0)
t7.pu()
t7.shape("square")
t7.goto(-430,450)
t7.color("yellow")
t8 = Turtle()
t8.speed(0)
t8.pu()
t8.goto(-450,450)
t8.shape("square")
t8.color("red")

t4 = Turtle()
t4.shape("turtle")
t4.speed(1)
t4.pu()
t5 = Turtle()
t5.speed(1)
t5.pu()
t5.shape("turtle")
rt43 = 0

class beeper2(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            c = randint(-450,450)
            v = randint(-0,0)
            t4.goto(c,v)
            
beep2 = beeper2()
beep2.start()

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            c = randint(-0,0)
            v = randint(-450,450)
            t5.goto(c,v)
            
beep  = beeper()
beep.start()

t1 = Pen()

t1.color("green")
t1.shapesize(4)
#t1.oni("L")
t1.speed(1)
t1.pu()
t1.shape('circle')
t1.color('white')
t = Turtle()
#t.color('green')
t.speed(1)
t.pu()
t.forward(5)
listen()
# class beeper4(threading.Thread):
#     def run(self):
#         global rt43
#         self.keeprunning = True
#         while self.keeprunning:
#             time.sleep(0.01)
#             trtrtrt = randint(-23,23)

#             if trtrtrt == -23:
#                 Screen().bgcolor("white")
#                 time.sleep(0.1)
#                 Screen().bgcolor("black")

            
# beep4  = beeper4()
# beep4.start()

class beeper3(threading.Thread):
    def run(self):
        global rt43
        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            rt43 = rt43 + 1
            if rt43 == 10:
                t6.hideturtle()
            if rt43 == 20:
                t7.hideturtle()
            if rt43 == 30:
                t8.hideturtle()
                t1.hideturtle()
            
beep3  = beeper3()
beep3.start()

def ata():
    u = 1
    while True:
        t1.forward(1)
        x,y = t1.pos()
        if x >= 500:
   #         print('r')
            t1.hideturtle()
            break
q.onkey(ata,'~')
def fe():
    u = 1
    t2 = t1.clone()
    t1.hideturtle()
    def rt():
 #       print('t')
        x,y = t1.pos()
        x2,y2 = t.pos()
        gh = distance(t,t2)
        if gh <= 30:
            t2.hideturtle()
  #          print("Y")
            t1.showturtle()
    listen()
    q.onkey(rt,'=')
class beeper3(threading.Thread):
    def run(self):
        global rt43
        self.keeprunning = True
        while self.keeprunning:
            x,y = t1.pos()
            x2,y2 = t.pos()
            gh = distance(t,t9)
            if gh <= 5:
                t9.hideturtle()
                rt43 = 0
                t8.showturtle()
                t7.showturtle()
                t6.showturtle()
                

beep3  = beeper3()
beep3.start()


def f():
#
    
    t1.forward(1)
    t.forward(1)
def b2():
    if u == 0:
        t1.color("black")
u = 0
def w():
    global u
    #print("O")
    if u == 0:
        t1.color('white')
        t.color("black")

def b():
    
    t1.forward(-1)
    t.forward(-1)
def u():
    x,y = t1.pos()
    t1.goto(x,y+1)
    x,y = t.pos()
    t.goto(x,y+1)

def d():
    x,y = t1.pos()
    t1.goto(x,y-1)
    x,y = t.pos()
    t.goto(x,y-1)

q.onkey(f,'Right')
q.onkeypress(f,'Right')
q.onkey(b,'Left')
q.onkeypress(b,'Left')
q.onkey(u,'Up')
q.onkeypress(u,'Up')
q.onkey(d,'Down')
q.onkeypress(d,'Down')
q.onkey(b2,'-')
q.onkey(fe,'.')
q.onkey(w,'=')
mainloop()

  #         print("Y")

