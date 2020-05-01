from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import sys
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
import sys

o = 0
wert = int(input("print number from 0 to intenger:"))
trew = int(input("print number from 0 to intenger:"))
hg = int(input("print how many math operations do you wanna (1+,2+-,3+-*,4+-*/ 5)+-*/**):"))

TimeWait=5
isOver=False

class beeper(threading.Thread):
    def run(self):
        global TimeWait, isOver
        self.keeprunning = True
        while self.keeprunning:
            if TimeWait == 0:
                print("\nTime is over!")
                isOver=True
                exit()
            TimeWait = TimeWait-1  
            time.sleep(1)
            #print(TimeWait)

            
beepProg  = beeper()
beepProg.start()

while True:
    ret = randint(1,hg)
    ter = randint(wert,trew)
    er = randint(wert,trew)
    if ret == 1:
        lk = ter + er
        print(ter)
        print("+")
        print(er)
        uo = input("=")
        if lk == int(uo):
            print("right!")
            o = o + 1
            print("your score is ",o)
        else:
            print("your score is ",o)
            break
    if ret == 2:
        lk = ter - er
        print(ter)
        print("-")
        print(er)
        uo = input("=")        
        if lk == int(uo):
            print("right!")
            o = o + 1
            print("your score is ",o)
        else:
            print("your score is ",o)
            break
    if ret == 3:
        lk = ter * er
        print(ter)
        print("*")
        
        print(er)
        uo = input("=")        
        
        if lk == int(uo):
            print("right!")
            o = o + 1
            print("your score is ",o)
        else:
            print("your score is ",o)
            break
    if ret == 4:
        lk = ter / er
        if isinstance(lk, int):
            print(ter)
            print("/")
            print(er)
            uo = input("=")
            if lk == int(uo):
                print("right!")
                o = o + 1
                print("your score is ",o)
            else:
                print("bad")
                print("your score is ",o)
                break
    if hg == 5:

        lk = ter - er
        print(ter)
        print("-")
        print(er)
        uo = input("=")        
        if lk == int(uo):
            print("right!")
            o = o + 1
            print("your score is ",o)
        else:
            print("your score is ",o)
            break
    if ret == 3:
        lk = ter ** er
        print(ter)
        print("**")
        
        print(er)
        uo = input("=")        
        
        if lk == int(uo):
            print("right!")
            o = o + 1
            print("your score is ",o)
        else:
            print("your score is ",o)
            break
        






















































































