from turtle import *
import turtle
shape("circle")
penup()

while True:
    x,y = pos()
    if x < 100 and y < 100:
        goto(x+100,y+100)
    elif x > -100 and y > -100:
        goto(x-100,y- 100)               
    








