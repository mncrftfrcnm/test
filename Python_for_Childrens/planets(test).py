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

wait_seconds = 1
WinWidth=750
screen = Screen()
t = Turtle()
t.shape("circle")
t.pu()
t.left(90)
t.forward(50)
t2 = Turtle()
t2.shape("circle")
def treg():
    x,y =t.pos()
    x2, y2 = t2.pos()
    if x == x2:
        print("you win")
    else:
        print("you lose")
listen()
screen.onkey(treg,"w")
#t2.hideturtle()
#t2.pu()
t2.speed(0)
t2.forward(-5)
while True:
    for x in range(35):
        t2.left(10)
        t2.forward(10)
        x,y =t.pos()
        x2, y2 = t2.pos()
        if x2 == x and y2 == y:
            print("you lose")
    # t2.forward(-10)