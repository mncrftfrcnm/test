
from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from turtle import *
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
WinWidth=750
screen = Screen()
t = Pen()
screen.onscreenclick(t.goto)
WinTk = Tk()
Canv = Canvas(WinTk, width=WinWidth, height=500, bg="white")
Canv.pack()
Tr = Canv.create_polygon(50,90,100,20,140,90,fill="blue")
yt = Canv.create_polygon(100,90,100,20,140,90,fill="yellow")
def tre(event):
    t.pu()
def te(event):
    t.pd()
def on_key_release(event):
#    global leftPressed,rightPressed
    if event.keysym == "Left":
        t.right(-10)
#        leftPressed = 0
    if event.keysym == "Right":
        t.right(10)
    if event.keysym == "Up":
        t.forward(10)
#        leftPressed = 0
    if event.keysym == "Down":
        t.forward(-10)
#        rightPressed = 0
Canv.tag_bind(Tr, "<Button-1>",tre)
Canv.tag_bind(yt, "<Button-1>",te)
WinTk.bind("<KeyPress>",on_key_release)
WinTk.bind("<KeyRelease>",on_key_release)
WinTk.mainloop()
