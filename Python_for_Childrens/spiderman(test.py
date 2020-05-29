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
e = 0
x = 0
y = 1
screen = Screen()
t = Pen()
t.hideturtle()
t.speed(0)
#t.pu()
while True:
#321
    
    for x  in range(10):
            
        t.circle(y)
        y = y + 10
        t.right(10)
    t.right(90)
#    t.forward(5)
        
    # y = 0
    # t.right(90)
    #print(y)
#    t.forward(20)
    