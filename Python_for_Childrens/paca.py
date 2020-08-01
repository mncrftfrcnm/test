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
t.speed(0)
t.pu()
t.hideturtle()
f = 500
t.goto(-500,f)
t2 = Turtle()
t2.speed(0)
t2.pu()
t2.goto(900,900)
def show_position(x,y):
    print(x,y)


#q.onscreenclick(show_position)
for x in range(5):
    for u in range(5):
        t1 = t.clone()
        t1.st()
 #       t1.onclick(got)



        

            

        t.forward(200)
    f = f -200
    t.goto(-500,f)
t2.ht()
mainloop()