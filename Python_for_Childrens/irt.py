from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer
canvasWidth = 750
canvasHeight = 500

WinTk = Tk()
Canv = Canvas(WinTk, width=canvasWidth, height=canvasHeight, bg="white")
Canv.pack()
gn = Canv.create_polygon(300,180,290,30,190,90,fill="orange")
ng = Canv.create_polygon(150,230,340,80,190,90,fill="orange")
r = True
#while r == True:
def hh(event):
#    t = randint(50,5000)
    Beep(500,1000)
def h(event):
#    t = randint(50,5000)
    Beep(37,109)
yy = Canv.create_polygon(350,180,290,30,190,90,fill="orange")
y = Canv.create_polygon(590,270,340,80,190,90,fill="orange")
r = True
#while r == True:
def tt(event):
#    t = randint(50,5000)
    Beep(100,100)
def t(event):
#    t = randint(50,5000)
    Beep(1000,100)

Canv.tag_bind(yy, "<Button-1>",tt)
Canv.tag_bind(y, "<Button-1>",t)
Canv.tag_bind(gn, "<Button-1>",hh)

Canv.tag_bind(ng, "<Button-1>",h)
WinTk.mainloop()