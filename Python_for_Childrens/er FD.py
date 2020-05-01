from turtle import *

s = 360

setpos(-s/2, -s/2)

def drawLine(a, b):
    ax = a.getX()
    ay = a.getY()
    ah = a.heading()
    a.moveTo(b.getX(), b.getY())
    a.setpos=pos(ax, ay)
    a.heading(ah)
    
# generate Turtle clone
t1 = clone() 
t1.speed(-1)
forward(s)
right(90)
t2 = clone()
t2.speed(-1)
forward(s)
right(90)
t3 = clone()
t3.speed(-1)
forward(s)
right(90)
t4 = clone()
t4.speed(-1)
forward(s)
right(90)
#hideTurtle()

while True:
    t1.setHeading(t1.towards(t2))
    t2.setHeading(t2.towards(t3))
    t3.setHeading(t3.towards(t4))
    t4.setHeading(t4.towards(t1))
   
    drawLine(t1, t2)
    drawLine(t2, t3)
    drawLine(t3, t4)
    drawLine(t4, t1)

    t1.forward(5)
    t2.forward(5)
    t3.forward(5)