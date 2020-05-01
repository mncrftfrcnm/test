from turtle import *
t = Pen()
t.shape("circle")
y = 0
t.speed(1)
t.width(100)
t.color("green")
t.left(90)
while True:
    t.color("green")
    t.forward(y)
    t.color("white")
    t.forward(-y)
    y = y + 10







