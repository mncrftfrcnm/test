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
t.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t.pu()

def ata(x,y):
    t1 = t.clone()
    t1.speed(0)
    t1.goto(x,y)
    t1.shape('triangle')
def g(x,y):
    
    t.setx(x)
#def ata2(x,y):
t2 = Turtle()
t2.speed(0)
shapes = ['triangle','turtle','square','circle','classic','arrow']
t2.pu()
q.onscreenclick(g)
q.onscreenclick(ata,btn = 3)
mainloop()