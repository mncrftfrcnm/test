
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
u = []
k = 0
def uut():
    global k
    f = input("what word do you wanna:") 
    hg = len(f)
    gh = str(f)
    for x in range(hg):
        u.append(gh[x])
        if gh[x] == "a" or gh[x] == "а":
            k = k + 1 
#        print(u)
    print(k)
        
uut()