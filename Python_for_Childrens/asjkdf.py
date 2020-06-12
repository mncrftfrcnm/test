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
s = ['classic','triangle','circle','square']
while True:
    x = randrange(1,56)
    y = randrange(1,56)
    z = randrange(1,56)
 #   a = randint(0.01,56)
    t.shape(choice(s))
    t.shapesize(x,y,z)