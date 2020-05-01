from random import *
from turtle import *

t = Pen()
t.hideturtle()
t.speed(0)
t.penup()
g = 10
clr = 0
trt = int(input("what step do you want:"))
for x in range(1000):
    t.right(90)
    t.forward(10)
    t.write("+")
    t.right(90)
    t.forward(10)
    t.write("+")
    g = g+trt
#    trt = trt + 10
    
    if clr>=16777215:
        clr = 0
    elif clr<16777215:
        clr=clr+10000
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#') 
#    print (clrname)
    while len(clrname) < 7:
        clrname = clrname.replace('#','#0')
    if clr<=16777215:
        t.pencolor(clrname)
yy = input("u")