from turtle import *
shape("turtle")

from random import *
speed(10)
pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")
hideturtle()
def vf():
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    color(clrname.upper())
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def fdfd():
        
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    color(clrname.upper())
    for x in range(0,4):
        forward(30)
        vf()
    backward(120)
def uy():
    for x in range(0,10):
        fdfd()
for x in range(10):
    uy()
    right(36)

hh = input("dd")
    







