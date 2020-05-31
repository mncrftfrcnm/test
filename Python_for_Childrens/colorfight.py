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
t  = Turtle()
t2 = Turtle()
t2.pu()
t2.goto(100,0)
ch = 0
ph = 0
#t.color("#00550")
#t.color("#999999")
#t.color("#05F4A0")
print("the color must be > #05F4A0")
for x in range(5):
    clr = input("please color: ")
    t.color(clr)
#    ph = ph+1
    
    if clr >= "#05F4A0":
        ph = ph + 4
    
print(ph)
for x in range(5):
    clr = input("please color: ")
    t2.color(clr) 
#    ph = ph+1
    if clr >= "#05F4A0":
        ch = ch + 4
print(ch)
if ch == ph:
    print("draw")
if ch < ph:
    print("1p.win")
if ch > ph:
    print("2p.win")
#jjjk = input("3:")