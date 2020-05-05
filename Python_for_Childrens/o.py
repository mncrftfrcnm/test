import turtle
from random import *
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")

tess.penup()                
size = 20
for i in range(30):
    tre = randint(0,2)
    if tre == 0:
       tess.shape("turtle") 
    if tre == 1:
       tess.shape("classic")
    if tre == 2:
       tess.shape("arrow")
    tess.stamp()
    size = size + 3
    tess.forward(size)
    tess.right(24)

wn.mainloop()