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
# t = Turtle()
# t.pu()
# t.speed(0)
print("the coordinates what we print for you is -2,+1,-3: ")
k = 10
while True:

    for f in range(10):
        tx = randint(-50,50)
        print(tx-2+1-3)
        ty = randint(-50,50)
        print(ty-2+1-3)
        x = int(input("please coordinate x (from -50 to 50): "))
        y = int(input("please coordinate y(from -50 to 50): "))
        if x == tx and y == ty:
            print("good")
            k = k - 1
    if k == 0:
        print("you win")
        break
    if k != 0:
        print("you lose")
        break

    
