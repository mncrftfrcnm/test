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
t.right(30)
while True:
    x,y = t.pos()
    if x>=500:
        tre = t.heading()
        t.left(tre)
    if y>=500:
        tre = t.heading()
        t.left(tre)
    

    if y<=-500:
        tre = t.heading()
        t.left(tre+2)
    
    if x<=-500:
        tre = t.heading()
        t.left(tre+2)
    

    t.forward(1)
    x,y = t.pos()
    if x>=500:
        tre = t.heading()
        t.left(tre)
    if y>=500:
        tre = t.heading()
        t.left(tre)
    

    if y<=-500:
        tre = t.heading()
        t.left(tre+2)
    
    if x<=-500:
        tre = t.heading()
        t.left(tre+2)
    
