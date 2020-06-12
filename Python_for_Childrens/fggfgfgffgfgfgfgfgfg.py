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
u = 0
def ata():
    global u
    if u == 0:
        t.left(90)
        t.forward(400)
        t.right(90)
        x = 1
    if u == 1:
        t.right(90)
        t.forward(400)
        t.left(90)
        x = 0
    u = x
listen()
q.onkey(ata,'w')
mainloop()

