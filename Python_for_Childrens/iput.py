from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading

while True:
    f = int(input("1)your enter 2)computer music:"))
    if f == 1:
        
        t = int(input("choose number from 37 to 32000:"))
        rt = int(input("choose number from 0 to 1000:"))
        Beep(t,rt)
    else:
        x = randint(10,100)
        for g in range(x): 
            t = randint(37,32000)
            rt = randint(0,1000)
            Beep(t,rt)
            print(t,rt)