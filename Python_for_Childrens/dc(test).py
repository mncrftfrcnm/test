import turtle
from turtle import *
import move_turtle
screen = Screen()
t = Turtle()
t.speed(1)
t.pu()
def re():
    move_turtle.r(t)
def le():
    move_turtle.l(t)
def ata():
    t1 = t.clone()
    for x in range(40):
        
        t1.forward(20)
        x,y = t1.pos()
        t1.goto(x,y-10)
    t1.hideturtle()

listen()
screen.onkey(ata,'w')
screen.onkey(le,'Left')
screen.onkeypress(le,'Left')
screen.onkey(re,'Right')
screen.onkeypress(re,'Right')
mainloop()