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
import teleport
import all_my_commands
tre = randint(1,3)
ter = int(input('1) paper, 2) knife, 3) stone: '))
print(tre)
if tre == ter:
    print('draw')
if tre == 2 and ter == 1:
    print('you lose')
if tre == 3 and ter == 1:
    print('you win')
if tre == 1 and ter == 2:
    print('you win')
if tre == 3 and ter == 2:
    print('you lose')
if tre == 1 and ter == 3:
    print('you lose')
if tre == 2 and ter == 3:
    print('you win')
