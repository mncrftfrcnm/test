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
ytu = 0
def r(t):
    global ytu
    ytu = 1
    rtty = t.heading()
    if rtty ==180:
        t.right(180)
    x,y = t.pos()
    t.goto(x+1,y)
    ytu = 0
def l(t):
    global ytu
    rtty = t.heading()
    ytu = 1
    if rtty ==0:
        t.right(180)
    x,y = t.pos()
    t.goto(x-1,y)

def u(t):
    global ytu
    ytu = 2
    x,y = t.pos()
    t.goto(x,y+30)
    x,y = t.pos()
    t.goto(x,y-30)
    ytu = 0
def ata(t,t2,fun):
    global ytu
    if ytu == 0:
        t1 = t.clone()
        t1.forward(5)
        tre = t1.distance(t2)
        if tre <=10:
            fun()
    
    if ytu == 1:
        t1 = t.clone()
        for c in range(100):

            tre = t1.distance(t2)
            t1.forward(1)
            if tre <=10:
                fun()
    
    if ytu == 2:
        x,y = t.pos()
        t.goto(x,y+30)
        x,y = t.pos()
        t.goto(x,y-30)
