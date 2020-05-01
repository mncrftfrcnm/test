
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
WinTk = Tk()

Canv = Canvas(WinTk, width=500, height=500, bg="white")
Canv.pack()
Tr = Canv.create_polygon(50,90,100,20,140,90,fill="blue")
def uut(event):
    f = open('recepies.txt', 'r')
    for line in f:
        print(line)
#    uuu  = input("90")
Canv.tag_bind(Tr, "<Button-1>",uut)
WinTk.mainloop()










