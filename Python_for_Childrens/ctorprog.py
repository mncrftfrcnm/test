from turtle import *
from random import *
t=Pen()
t.speed(0)
#t.hideturtle()
for x in range(400):
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

    t.circle(x)
    t.left(45)
e = input("ys")