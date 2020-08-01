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
sco1 = 0
sco2 = 0
while True:
    tre = randint(0,2)

    if tre == 0:
        ert = randint(0,10)
        tr = randint(0,10)
        print('1p')
        ytr = ert,'+',tr
        yt = int(input(ytr))
        an = tr+ert
        if an == yt:
            print('right')
            sco1 = sco1 + 1
        if an != yt:
            print('bad')
            print(sco1)
            break
    if tre == 1:
        ert = randint(0,10)
        tr = randint(0,10)
        print('1p')
        ytr = tr,'*',ert
        yt = int(input(ytr))
        an = tr*ert
        if an == yt:
            print('right')
            sco1 = sco1 + 1
        if an != yt:
            print('bad')
            print(sco1)
            break
    if tre == 2:
        ert = randint(0,10)
        tr = randint(0,10)
        print('1p')
        ytr = tr,'-',ert
        yt = int(input(ytr))
        an = tr-ert
        if an == yt:
            print('right')
            sco1 = sco1 + 1
        if an != yt:
            print('bad')
            print(sco1)
            break
while True:
    tre = randint(0,2)

    if tre == 0:
        ert = randint(0,10)
        tr = randint(0,10)
        print('2p')
        ytr = ert,'+',tr
        yt = int(input(ytr))
        an = tr+ert
        if an == yt:
            print('right')
            sco2 = sco2 + 1
        if an != yt:
            print('bad')
            print(sco2)
            break
    if tre == 1:
        ert = randint(0,10)
        tr = randint(0,10)
        print('2p')
        ytr = tr,'*',ert
        yt = int(input(ytr))
        an = tr*ert
        if an == yt:
            print('right')
            sco2 = sco2 + 1
        if an != yt:
            print('bad')
            print(sco2)
            break
    if tre == 2:
        ert = randint(0,10)
        tr = randint(0,10)
        print('2p')
        ytr = tr,'-',ert
        yt = int(input(ytr))
        an = tr-ert
        if an == yt:
            print('right')
            sco2 = sco2 + 1
        if an != yt:
            print('bad')
            print(sco2)
            break
if sco2 == sco1:
    print('draw')
if sco2 < sco1:
    print('1p.win')
if sco2 > sco1:
    print('2p.win')