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
q = Screen()
t = Turtle()
listen()
t2 = Turtle()
t.pu()
t2.pu()
t.speed(0)
t.goto(0,90)
t2.speed(0)
t2.goto(90,0)
t2.shapesize(10)
t3 = Turtle()
t3.pu()
i = []
il = 0
for h in range(7):
    yy = randint(0,2)
    i.append(yy)
for tu in i:
    if tu == 0:
        t.color('yellow')
        time.sleep(0.9)
        t.color('black')
    if tu == 1:
        t2.color('yellow')
        time.sleep(0.9)
        t2.color('black')
    if tu == 2:
        t3.color('yellow')
        time.sleep(0.9)
        t3.color('black')
def tt(x,y):
    global il
    if il <8:
        tyty = 0
    #    print(i[tyty])
        if tyty == i[il]:
           # tyty = tyty + 1
            
            il = il+1
            print(il)
            if il == 7:
                print("WIN")


            print('normal')
        else:
            print("bad")
            il = 0
def tt2(x,y):
    global il
    if il <8:
        tyty = 1
    #    print(i[tyty])
        if tyty == i[il]:
            #tyty = tyty + 1
            
            il = il+1
            print(il)
            if il == 7:
                print("WIN")


            print('normal')
        else:
            print("bad")
            il = 0
t.onclick(tt)
t2.onclick(tt2)
def tt3(x,y):
    global il
    if il <8:
        tyty = 2
            
        if tyty == i[il]:
            #tyty = tyty + 1
            
            il = il+1
            print(il)
            #print(il)
            if il == 7:
                print("WIN")

            print('normal')
        else:
            print("bad")
            il = 0
t3.onclick(tt3)
mainloop()