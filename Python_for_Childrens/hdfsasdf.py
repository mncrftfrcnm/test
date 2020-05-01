from turtle import *
from random import *
shape("turtle")
speed(0)
pencolor("white")
pensize(6)
hideturtle()
from random import *
gh = False
while gh == False:
    h = int(input("choose 1)goodbye 2)hello: "))
    Screen().bgcolor("turquoise")
    if h == 1:
        we = randint(0,2)
        if we == 0:
            write("have a good day!")
            gh = True
            break
        elif we == 1:
            write("bye")
            gh = True
            break
        elif we == 2:
            write("goodbye")
            gh = True
            break
    elif h == 2:
        we = randint(0,1)
        if we == 1:
            write("hi")
        elif we == 0:
            write("hello")
rty = input("udfg")