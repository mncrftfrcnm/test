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
import se
q = Screen()
t = Turtle()
t.speed(1)
listen()
t.pu()
def j():
    t1 = t.clone()
    t1.forward(10)
    def a():
        x,y = t1.pos()
        t.goto(x,y)
        x2 = y/2
        t.goto(x2,0)
        x,y = t.pos()
        print(x)
        tyyk = t.clone()
        t.home()
    q.onkey(a,'w')
    while True:
        x,y = t1.pos()
        t1.goto(x,y+400)
        x,y = t1.pos()
        t1.goto(x,y-400)
    
q.onkey(j,'Up')
mainloop()