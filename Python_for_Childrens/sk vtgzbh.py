from turtle import *
import turtle
from random import *

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

screen.mainloop()
