import tkinter
from random import *
import tkinter.messagebox
import time
import random
import threading
from threading import Timer,Thread
from time import sleep
from tkinter import *
y = -90
w = tkinter.Tk()
c = tkinter.Canvas(w,width=400,height=500, bg="white")
c.pack()
tre = c.create_text(100,100,text="ooooooogrtg",angle=-90)
def r():
    global y
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    y = y - 1
    c.itemconfig(tre,angle=y)
    c.itemconfig(tre,fill=clrname)
        
#    tre.tag_configure(clrname,foreground=clrname)
#    c.itemconfig(tre,background=clrname)
def jgue(event):
    if event.keysym == "Left":
        r()
w.bind("<KeyPress>",jgue)

#r()

mainloop()