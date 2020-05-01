from random import *
from turtle import *
from threading import*
from time import *
t = Pen()
t.hideturtle()
clr = 0
uol = 3
t.speed(0)
clr = 0
uuu = 0
t.penup()
t.goto(-300,200)
ugvyu4e = int(input("how many dots do you wanna:"))
e = input("what symbol do you wanna:")
strwid=len(e)
for x in range(ugvyu4e):
    t.penup()
    for g in range(x+1):
        if clr>=16777215:
            clr = 0
        elif clr<16777215:
            clr=clr+1000000+g*500000
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#') 
        while len(clrname) < 7:
            clrname = clrname.replace('#','#0')
        if clr<=16777215:
            t.pencolor(clrname)
        t.write(e,font=("webdings",35))
        t.forward(45*strwid)
        g = g+1
#    t.right(90)
    t.forward(-g*45*strwid)
    t.right(90)
    t.forward(45)
    t.left(90)
 
yyy = input("o")
