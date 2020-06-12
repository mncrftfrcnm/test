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
q = Screen()
t = Turtle()
t.speed(1)
t.pu()
tre = input("what shape do you wanna")
t.shape(tre)
s = 1
y = 1
w = 1
def s1():
    global s,y,w
    s = s+0.5
    y = y+1
    w = w+0
    t.shapesize(s,y,w)
def s2():
    global s,y,w
    if s > 0.5  and y > 2:
        s = s-0.5
        y = y-1
        w = w-0
        t.shapesize(s,y,w)
def l():
    t.left(1)
def r():
    t.left(-1)
listen()
#q.onkeypress(ata1,'.')

q.onkey(l,'Left')
q.onkey(r,'Right')
    
q.onkey(s1,'w')
q.onkey(s2,'q')
mainloop()
