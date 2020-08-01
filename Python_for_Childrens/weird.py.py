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
from PIL import Image
q = Screen()
w1 = Turtle()
w1.pu()
w1.forward(-500)
w2 = Turtle()
w2.pu()
w2.forward(500)
t3 = Turtle()
t3.pu()
t3.speed(0)
ti = 60
mon = 10
powe = 0
mon2 = 10
powe2 = 0
listen()
def rewrite():
    global mon,powe
    w1.clear()

    w1.write(powe)
def rewrite2():
    global mon2,powe2
    w2.clear()

    w2.write(powe2)

def m():
    global mon
    if mon >= 10:
        class beeper(threading.Thread):
            def run(self):
                global mon
                self.keeprunning = True
                while self.keeprunning:
                    mon = mon + 1
                    time.sleep(0.05)
                    
                    
        beep  = beeper()
        beep.start()
def p():
    global mon,powe
    if mon >= 20:
        w1.clear()
        class beeper(threading.Thread):
            def run(self):
                global mon,powe
                self.keeprunning = True
                while self.keeprunning:
                    w1.clear()
                    powe = powe + 1
                    w1.clear()
                    
        beep  = beeper()
        beep.start()
q.onkey(m,',')
q.onkey(p,'.')
def m2():
    global mon2
    if mon2 >= 10:
        class beeper(threading.Thread):
            def run(self):
                global mon2
                self.keeprunning = True
                while self.keeprunning:
                    mon2 = mon2 + 1
                    time.sleep(0.05)
                    
                    
        beep  = beeper()
        beep.start()
def p2():
    global mon2,powe2
    if mon2 >= 20:
        w1.clear()
        class beeper(threading.Thread):
            def run(self):
                global mon2,powe2
                self.keeprunning = True
                while self.keeprunning:
                    w1.clear()
                    powe2 = powe2 + 1
                    w1.clear()
                    
        beep  = beeper()
        beep.start()
def sh2():
    global mon2,powe2
    print(mon2,powe2)
class beeper(threading.Thread):
    def run(self):
        global ti,powe,powe2
        self.keeprunning = True
        while self.keeprunning:
            ti = ti - 1
            print(ti)
            if ti <=0:
                print('time is over')
                print(powe,powe2)
                if powe == powe2:
                    print('draw')
                if powe < powe2:
                    print('2p win')
                if powe > powe2:
                    print('1p win')
                
                self.keepruning = False
            time.sleep(1)
            
                    
beep  = beeper()
beep.start()
def sh():
    global mon,powe
    print(mon,powe)
q.onkey(m2,'w')
q.onkey(p2,'q')
q.onkey(sh2,'e')
q.onkey(sh,'m')
mainloop()