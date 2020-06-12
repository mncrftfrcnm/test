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
t.shape('circle')
t.pu()
t.hideturtle()
t2 = Turtle()
t2.pu()
t2.pu()
t2.forward(10)
t2.shape('circle')
t2.hideturtle()
t3 = Turtle()
t3.pu()
t3.forward(20)
t3.shape('circle')
t3.pu()
t3.hideturtle()
t4 = Turtle()
t4.shape('circle')
t4.pu()
t4.hideturtle()
t4.goto(0,-100)
t4.pensize(10)
t3.clear()
t4.pd()
for x in range(10):
#    print("P")
    t.st()
    
    time.sleep(1)
    t2.st()
    #t2.ht()
    time.sleep(1)
    t3.st()
    #t3.ht()
    time.sleep(1)
    t.ht()
    t2.ht()
    t3.ht()
for x in range(20):
    t4.forward(10)
    time.sleep(0.1)
t5 = Turtle()
t5.pu()
t5.goto(0,-200)
for x in range(30):
    t5.circle(10)
    time.sleep(0.1)
t5.hideturtle()
t4.clear()
write('the loading not end becose it is have errors!:)')
mainloop()