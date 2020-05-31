import tkinter
from random import *
import tkinter.messagebox
import time
from turtle import *
import random
import threading
from threading import Timer,Thread
from time import sleep
from tkinter import *
y = 0
w = tkinter.Tk()
c = tkinter.Canvas(w,width=400,height=500, bg="white")
c.pack()
screen = Screen()
t = Turtle()
screen.onscreenclick(t.goto)
while True:
    x,y = t.pos()
    c.config(width=x)
    x,y = t.pos()
    c.config(height=y)
    tre = input("config?:")

#tre = c.create_text(100,100,text="wyeragjujs5yt5tgrtg",angle=0)