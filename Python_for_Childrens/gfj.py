from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer
while True:
    t = randint(37,32000)
    rt = randint(100,1000)
    Beep(t,rt)
    print(t,rt)





