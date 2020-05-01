from turtle import *
from random import *
from math import *

clr = randint(0xAAAAAA,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')
cf = [clrname.upper()]

for x in range(1,1000):
        
    clr = randint(0x555555,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    cf.append(clrname.upper())

    
t = Pen()
t.hideturtle()
t.speed(0)
bgcolor("black")
for y in range (1,30):
    for x in range(1,20):
        t.pencolor(cf[x%999])
        varx=2*sin(y/pi)*pow(x,1/x)
        t.forward(40*sin(varx/pi)*sin(varx/pi))
        t.left(40*cos(varx/pi)*cos(varx/pi))
        t.forward(40*cos(varx/pi))
        t.right(-40*sin(varx/pi))
rrrr = input("t")

