import tkinter
import tkinter.messagebox
import time
import random
import winsound
from tkinter import *
from winsound import PlaySound,SND_ASYNC
import threading
from threading import Timer
from random import *
import random
y = 5
l = 1
massive = []
while True:
    for element in range(1,y):
        window = "w" + str(element)
        massive.append(window)

    print(massive)

    for element in massive:
        element = tkinter.Tk()
    y = y+3
    mainloop()
    print("level ",l, "complited")
    l = l + 1