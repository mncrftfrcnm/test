import turtle
from turtle import *
y = 1
screen = Screen()
t= turtle.Turtle()
def at():
    global y
    y= y+ 1
    t.shapesize(y)
def a():
    global y
    if y > 1:
        y= y- 1
        t.shapesize(y)
listen()
screen.onkey(a,'Right')
screen.onkey(at,'Left')
mainloop()