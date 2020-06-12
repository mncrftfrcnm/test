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
t = Turtle()
t.speed(1)
t.pu()
def ata():
    i = 0
    t1 = t.clone()
    t1.pd()
    for x in range(15):
        t1.forward(30)
        i = i+5
        t1.pensize(i)
    t1.hideturtle()
    t1.clear()
    t.clear()
listen()
q.onkey(ata,'w')
#q.onkeypress(ata,'w')
mainloop()