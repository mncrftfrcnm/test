from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import turtle
from turtle import *
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
f = 'forolya2prog.txt'
while True:    
    with open(f,'r+') as d:
        tre = input("what do you wanna to wtrite: ")
        d.write(tre)
