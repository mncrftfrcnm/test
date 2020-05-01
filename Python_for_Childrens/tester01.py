from turtle import *
import tkinter
from random import *
from tkinter import*
w = tkinter.Tk()
Canv = Canvas(w, width=300, height=500, bg="white")                     
Canv.pack()
clr = randint(0x0,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
        
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

















