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
screen = Screen()
t = Pen()
t.speed(0)
listen()
t.pu()
def HJ():
    for x in range(5):
        t1 = t.clone()
        
        
        t.forward(10)
        time.sleep(0.1)
        t1.hideturtle()
screen.onkey(HJ,'o')
mainloop()
   
  
