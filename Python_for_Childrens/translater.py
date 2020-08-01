import time
import sys
#from pygame.sprite import Sprite
#from pygame.sprite import Group
from random import *
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
import turtle
from turtle import *
import sys
from telnetlib import *
from teleport import *
ad = {}
while True:
    eg = input("word:")
    e = input("as:")
    ad[e] = eg
    eh = input('all: ')
    if eh == 'y':
        break

#267
while True:
    eg = input("what do you want to translate:")
    ew = eg.lower().split()
    aw = []
    for w in ew:
        if w in ad:
            aw.append(ad[w])
        else:
            print('we have no this word')
        print("".join(aw))

            