from turtle import *
import turtle
from random import *
while True:
    screen = Screen()

    turtle = Turtle()
    turtle.shape("turtle")
    turtle.pu() 
    turtle.speed(1)
    screen.onscreenclick(turtle.goto) 

    turtle2 = Turtle() 
    turtle2.speed(1)
    turtle2.pu()
turtle2.setpos(500,500)
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
wait_seconds = 1
WinWidth=750
from turtle import *
import turtle
from random import *

screen = Screen()

turtle = Turtle()
turtle.shape("turtle")
turtle.pu() 
turtle.speed(1)            

x = 0
turtle2 = Turtle() 
turtle2.speed(1)
turtle2.pu()
turtle2.setpos(500,500)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
#            first = randint(37,32000)
#            second = randint(100,1000)
#            PlaySound("C:\windows\media\Ring02.wav",False)
                        
            x2,y2 = turtle2.pos()
            if x == x2 or y == y2:
                print("game over")      
            tryio = randint(-500,500)
            x,y = turtle.pos()
            x2,y2 = turtle2.pos()
            if x == x2 or y == y2:
                print("game over")      
            ty = randint(-500,500)
            x,y = turtle.pos()
            x2,y2 = turtle2.pos()
            if x == x2 or y == y2:
                print("game over")      
            turtle2.goto(tryio,ty)
            x,y = turtle.pos()
            x2,y2 = turtle2.pos()
            if x == x2 or y == y2:
                print("game over")  
            
beep  = beeper()
beep.start()
'''
def move_second(): 
    x,y = turtle.pos()
    x2,y2 = turtle2.pos()
    if x == x2 or y == y2:
        print("game over")      
    tryio = randint(-500,500)
    x,y = turtle.pos()
    x2,y2 = turtle2.pos()
    if x == x2 or y == y2:
        print("game over")      
    ty = randint(-500,500)
    x,y = turtle.pos()
    x2,y2 = turtle2.pos()
    if x == x2 or y == y2:
        print("game over")      
    turtle2.goto(tryio,ty)
    x,y = turtle.pos()
    x2,y2 = turtle2.pos()
    if x == x2 or y == y2:
        print("game over")                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    screen.ontimer(move_second)

screen.ontimer(move_second) 
'''                
for i in range(50):
   turtle.forward(50)           
   turtle.right(144)               
turtle.done()
screen.onscreenclick(turtle.goto) 
screen.mainloop()