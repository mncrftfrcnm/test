from random import *
from turtle import *
from threading import*
t = Pen()
t.right(90)
#t.left(-90)
#t.forward(10)
iiiu8iiuhjhy = input("8usd2wse")
if clr>=16777215:
    clr = 0
elif clr<16777215:
    clr=clr+1700000
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#') 
while len(clrname) < 7:
    clrname = clrname.replace('#','#0')
if clr<=16777215:
    t.pencolor(clrname)
       