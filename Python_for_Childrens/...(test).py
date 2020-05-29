import tkinter
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC
import threading
from threading import Timer
from random import *
import random
canvasWidth = 750
canvasHeight = 500
w = tkinter.Tk()
c = tkinter.Canvas(w,width=canvasWidth,height=canvasHeight, bg="dodgerblue4")
c.pack()
bat = c.create_rectangle(100,canvasHeight-300,1100,canvasHeight-400,fill="pink")
ret = 0
def ata(event):
    global ret
    if ret == 0:
        c.itemconfig(bat,fill='green')
        c.config(background='black')
        ret2 = 1
    if ret == 1:
        c.itemconfig(bat,fill='pink')
        c.config(background='dodgerblue4')
        ret2 = 0
    ret = ret2
c.tag_bind(bat, "<Button-1>", ata)
w.mainloop()