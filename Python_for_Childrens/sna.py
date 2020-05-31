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
t2 = Turtle()
t2.hideturtle()
t2.color("white")
t2.forward(-10)
t2.pensize(10)
def r():
    t.right(10)
    t2.forward(10)
    t2.right(90)
listen()
screen.onkey(r,"Right")

#screen.onkeypress(r,"Right")
while True:
    t.forward(10)
    t2.forward(10)
#    t2.forward(-10)










