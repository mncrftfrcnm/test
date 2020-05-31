from turtle import *
from random import*
t = Turtle()
t.hideturtle()
t2 = Turtle()
t2.shapesize(5)
t2.pu()
t2.shape("circle")   
y = 1
t.right(90)
t4 = Turtle()
t4.penup()
t4.right(90)
t4.forward(200)
t4.color("yellow")
t4.speed(1)
while True:
    for y in range(40):
        t.pensize(y)
        t.forward(5)
        y = y + 1
    t.color("white")
#    t.forward(100)
    t4.forward(-190)
    t4.hideturtle()
    t.color("black")
    y = 0
    break
    
mainloop()