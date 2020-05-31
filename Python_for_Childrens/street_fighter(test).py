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
screen = Screen()
tre = 0
tr = 1
rt = 1
t4 = 1
t = Pen()
t.pu()
t.speed(1)
screen.onscreenclick(t.goto)
def ata():
    global tre,tr

    t1 = t.clone()
    t1.forward(90)
    t1.hideturtle()
    if tr == 1:

        

        tre = tre + 1
        tr = tr - 1
    def ata2():
        global tre, rt
        #print("P")
        t1 = t.clone()
        if rt == 1:
            tre = tre + 1
            rt = 0
        def ata3():
            global tre, t4
            time.sleep(2)
            # print("L")
            if t4 == 1:
                tre = tre + 1
                t4 = 0
            
            if tre == 3:
                print("you win")            
        screen.onkey(ata3,'o')
    screen.onkey(ata2,'i')
listen()
#screen.onkey(ata2,'i')
screen.onkey(ata,'p')

mainloop()