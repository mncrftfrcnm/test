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


y = 100
t = Pen()
t.hideturtle()
t.pu()
t.speed(0)
trre = input('what math question do you want to know: ')
t.write(trre)
t.right(90)
t.forward(10)
t.write("=")
#t.right(90)
t.forward(10)
t.write(str(trre))
mainloop()