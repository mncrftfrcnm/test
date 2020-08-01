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
t.pu()
t2 = Turtle()
t2.speed(0)
t2.shape("triangle")
t2.pu()
t3 = Turtle()
t3.speed(0)
t3.shape('square')
t3.pu()
t4 = Turtle()
t4.shape('circle')
t4.pu()
t4.speed(0)
t.goto(500,500)
t3.goto(450,500)
t4.goto(400,500)
t2.goto(350,500)
print('t,t3,t4,t2')
mon = 15
ht()
write(mon)
bul = 0
spe = 0
fl = 0
mi = 0
def ft(x,y):
    global mon, bul
    if mon >= 10:
        mon = mon - 10
        bul = bul + 1
    clear()
    write(mon)
def ft2(x,y):
    global mon, spe
    if mon >= 5:
        mon = mon - 5
        spe = spe + 1
    clear()
    write(mon)
    
t.onclick(ft)
t2.onclick(ft2)
tre = input('1) test 2) fight 3) fight 1 vs 1: ')
if tre == '1':
    clear()
    print(tre)
    t6 = Turtle()
    t6.pu()
    t6.speed(0)
    def f():
        global spe
        #print(spe)

        t6.forward(spe)
    def ata():
        global bul
        if bul >= 1:
            t1 = t.clone()
            



    listen()
    q.onkey(f,'Up')
    tre = input('')
