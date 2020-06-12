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
t = Turtle()
t.left(90)
t.pu()
while True:
    c = randint(-450,450)
    v = randint(-450,450)
    t.goto(c,v)
    etr = randint(1,20)
    for x in range(etr):
        t1 = t.clone()
        t1.shape('square')
        t.forward(10)
    t.forward(5)
    t1 = t.clone()
    t1.shapesize(1)
    t1.shape('triangle')