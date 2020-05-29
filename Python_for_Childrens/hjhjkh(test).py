from turtle import *

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

t = Pen()
t.hideturtle()
clr = randint(0x0,0xFFFFFF)
        
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
                
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

t.color(clrname.upper())

                        

t.circle(100)
t.pu()
t.left(90)
t.forward(200)
t.right(90)
t.pd()
clr = randint(0x0,0xFFFFFF)
        
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
                
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

t.color(clrname.upper())

t.circle(50)
t.pu()
t.left(90)
t.forward(100)
t.right(90)
t.pd()
clr = randint(0x0,0xFFFFFF)
        
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
                
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

t.color(clrname.upper())

t.circle(10)
t.pu()
t.left(90)
t.forward(50)
t.right(90)
t.pd()
t.pu()
t.write("STOP CORONAVIRUS!")

mainloop()