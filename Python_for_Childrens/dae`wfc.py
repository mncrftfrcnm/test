import turtle
from turtle import *
import time
ty = 1
screen = Screen()
t = turtle.Turtle()
t.shape("turtle")
screen.onscreenclick(t.goto)
while True:

    
    time.sleep(1)
    x,y = t.pos()
    t.write(x,y)
    t.pensize(ty)
    t.shapesize(ty)
    ty = ty + 1
