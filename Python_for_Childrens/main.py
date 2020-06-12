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
from PIL import Image
q = Screen()
t = Turtle()
t.pu()
def ata():
    t1 = t.clone()
    t2 = t.clone()
    t2.forward(500)
def l():
    t.forward(10)
listen()
q.onkey(ata,'w')
q.onkey(l,'Left')
mainloop()