from turtle import *
from random import *
t=Pen()
t.speed(0)
#t.hideturtle()
while True:
    tre = randint(-350,350)
    tr = randint(-350,350)
    t.goto(tre,tr)
    ty = randint(0,3)
    if ty == 0:
        t.begin_fill()
        for x in range(40):
            t.left(10)
            t.forward(10)
        t.end_fill()
    if ty == 1:
        for x in range(40):
            t.left(10)
            for gf in range(10):
                t.forward(5)
                t.write("1")
    if ty == 2:
        def vf(size):
            t.right(25)
            t.forward(size)
            t.backward(size)
            t.left(50)
            t.forward(size)
            t.backward(size)
            t.right(25)
        def fdfd(size):
            for x in range(0,4):
                t.forward(size)
                vf(size)
            t.backward(size*4)
        def uy(size):
            for x in range(0,6):
                fdfd(size)
                t.right(60)

        size = randint(5,40)
        uy(size)
    if ty == 3:
        for x in range(40):
            
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')

            t.color(clrname.upper())

            t.circle(x)
            t.left(45)

#shape("turtle")
#speed(0)
#pencolor("white")
#pensize(6)
#Screen().bgcolor("turquoise")

