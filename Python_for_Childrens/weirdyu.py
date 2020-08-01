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
import teleport
import all_my_commands
q = Screen()
t = Turtle()
t.speed(0)
t.pu()
t2 = Turtle()
t2.speed(0)
t2.shape("triangle")
t2.pu()
t3 = Turtle()
t3.speed(0)
t3.shape('square')
t3.pu()
t4 = Turtle()
t4.shape('circle')
t4.pu()
t4.speed(0)
t.goto(500,500)
t3.goto(450,500)
t4.goto(400,500)
t2.goto(350,500)
def ft(x,y):
    t1 = t.clone()
    t1.ondrag(t1.goto)
    def r(x,y):
        t1.right(10)
    def d(x,y):
        t1.ht()
    t1.onclick(r)
    t1.onclick(d,btn = 2,add = True)
def ft2(x,y):
    t1 = t2.clone()
    t1.ondrag(t1.goto)
    def r(x,y):
        t1.right(10)
    def d(x,y):
        t1.ht()
    t1.onclick(r)
    t1.onclick(d,btn = 2,add = True)
t2.onclick(ft2)
t.onclick(ft)
def ft3(x,y):
    t1 = t3.clone()
    t1.ondrag(t1.goto)
    def r(x,y):
        t1.right(10)
    def d(x,y):
        t1.ht()
    t1.onclick(r)
    t1.onclick(d,btn = 2,add = True)
def ft4(x,y):
    t1 = t4.clone()
    t1.ondrag(t1.goto)
    def d(x,y):
        t1.ht()

    def r(x,y):
        t1.right(10)
    t1.onclick(r)
    t1.onclick(d,btn = 2,add = True)
t4.onclick(ft4)
t3.onclick(ft3)
mainloop()