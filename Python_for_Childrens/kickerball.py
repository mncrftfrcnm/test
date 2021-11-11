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
t = Turtle()
t.speed(0)
Screen().setup(1500,1500)
t.shape('circle')
t.shapesize(3)
fx = 4
fy = 4
t.pu()
t.goto(600,600)
t.pd()
for x in range(4):
    t.right(90)
    t.forward(1200)
t.pu()
t.goto(0,0)


while True:
    x,y = t.pos()
    t.goto(x+0.5*fx,y+fy)  
    x,y = t.pos()
    if x>= 560:
        fx *= -1

    if y>=560:
        fy *= -1

    if x<= -560:
        fx *= -1
    if y<= -560:
        fy *= -1
  #  break

###################################
while True:
    t.forward(1)
    if x>= 500:
        r = randint(0,1)
        if r == 0:
            pass


    if y>= 500:
        fy *= -1

    if x<= -500:
        fx *= -1
    if y<= -500:
        fy *= -1    
