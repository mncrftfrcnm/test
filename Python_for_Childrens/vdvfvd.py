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
sco = 0
t  = Turtle()
while True:
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
#clrtxt.replace('0x','#')
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper()) 
    tre = input("please enter a code of color: ")
    if tre == clrname:
        sco = sco + 1  
    else:
        print("your score is ",sco)
        break
    
