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

q = Screen()

t = Turtle()
t.forward(100)
t.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t.pu()
t2 = Turtle()
q.setup(1500,1500)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t2.pu()
def ata(x,y):
    t.goto(x,y)
    tre = t.distance(t2)
    if tre <= 10:
        print("P")
t.ondrag(ata)
mainloop()