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
from se import *
q = Screen()
t = Turtle()
t.pu()
t.speed(0)
t2 = Turtle()
t2.pu()
t2.speed(0)
t2.color('white')
f = 36
t2.forward(-f)
listen()
ty = 0
def u():
    global f,ty
    ty = 1
    t.setheading(90)
    tre = f/2
    for gftf in range(f):
        t2.forward(1)
        t1 = t2.clone()
    t2.setheading(90)
    t2.forward(-f)
    ty = 0
def d():
    global f,ty
    ty = 1
    t.setheading(-90)
    tre = f/2
    for gftf in range(f):
        t2.forward(1)
        t1 = t2.clone()
    t2.setheading(-90)
    t2.forward(-f)
    ty = 0
def l():
    global f,ty
    ty = 1
    t.setheading(180)
    tre = f/2
    for gftf in range(f):
        t2.forward(1)
        t1 = t2.clone()
    t2.setheading(180)
    t2.forward(-f)
    ty = 0
def r():
    global f
    t.setheading(0)
    ty = 1
    t.setheading(0)
    tre = f/2
    for gftf in range(f):
        t2.forward(1)
        t1 = t2.clone()
    t2.setheading(0)
    t2.forward(-f)
    ty = 0

q.onkey(u,'Up')
q.onkey(d,'Down')
q.onkey(l,'Left')
q.onkey(r,'Right')
while True:
    if ty == 0:
        t.forward(3)
        t1 = t.clone()
        t2.forward(3)
        t1 = t2.clone()