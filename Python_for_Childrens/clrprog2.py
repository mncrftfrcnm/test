from random import *
from turtle import *
t = Pen()
t.hideturtle()
t.speed(0)
clr = 0
x = 5
while True:
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
        t.forward(x)
        t.left(59)
        t.pencolor(clrname)
        x = x+0.1
        




































































