from turtle import *
import turtle
from random import *
ret = randint(0,1000)
screen = Screen()

turtle = Turtle()
turtle.shape("turtle")
turtle.pu() 
turtle.speed(1)
turtle.write(ret)
screen.onscreenclick(turtle.goto)
screen.mainloop




