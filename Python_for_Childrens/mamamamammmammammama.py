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
from sqrt import find_middle
tre = int(input('number:'))
a = 0
b = tre
middle = find_middle(a,b)
while True:
    
    find = middle**2
    if find > tre:
        b = middle
    if find < tre:
        a = middle
    if find == tre:
        print(middle)
        break
    if tre < middle*middle and middle*middle < tre+0.00001:
        print(middle)
        break
    middle = find_middle(a,b)
        
