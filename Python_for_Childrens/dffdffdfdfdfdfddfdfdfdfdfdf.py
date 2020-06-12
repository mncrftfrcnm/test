from turtle import *
from random import *
s = Screen()
t=Pen()
t.pu()
t.speed(1)
y2 = 0
def ata():
    global y2
    if y2 == 1:
        t.shape("circle")

    if y2 == 0:
        t1 = t.clone()
        t1.forward(100)
        t1.hideturtle()
def j():
    global y2
    y2 = 1
    x,y = t.pos()
    t.goto(x,y+100)

    x,y = t.pos()
    t.goto(x,y-100)
    t.shape("classic")
    y2 = 0
listen()
s.onkey(ata,'w')
s.onkey(j,'Up')
mainloop()