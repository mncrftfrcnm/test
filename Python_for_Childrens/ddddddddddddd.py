from turtle import *
import turtle
import threading
from threading import *
import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
import os
head = Turtle()
head.speed(0)
while True:
    head.left(10)
    uy = randint(0,2)
    if uy == 0:
        head.shape("turtle")
    if uy == 1:
        head.shape("classic")
    if uy == 2:
        head.shape("triangle")