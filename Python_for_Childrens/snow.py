from turtle import *
from random import *
shape("turtle")
speed(0)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")

def vf(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def fdfd(size):
    for x in range(0,4):
        forward(size)
        vf(size)
    backward(size*4)
def uy(size):
    for x in range(0,6):
        fdfd(size)
        right(60)
while True:
    size = randint(5,40)
    x = randint(-500,500)
    y = randint(-500,500)
    penup()
    goto(x,y)
    pendown()
    uy(size)
#    right(36)
hh = input("dd")
        









