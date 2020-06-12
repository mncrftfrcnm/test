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
t.shapesize(123)
rrt = 123

for x in range(122):
    
    t.forward(1)
    rrt = rrt-1
    t.shapesize(rrt)

mainloop()