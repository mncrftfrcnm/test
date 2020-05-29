import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
from tkinter import *
y = 90
w = tkinter.Tk()
c = tkinter.Canvas(w,width=400,height=500, bg="white")
c.pack()
tre = c.create_text(100,100,text="ooooooogrtg",angle=-90)

def clocktic():
    global y
    for x in range(60):
        clr = randint(0x0,0xFFFFFF)    
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        c.itemconfig(tre,angle=-y)
        c.itemconfig(tre,fill=clrname)
        w.update()
        time.sleep(1)
        y=y+6

def jgue(event):
    if event.keysym == "Right":
        clocktic()

w.bind("<KeyPress>",jgue)
w.mainloop()
