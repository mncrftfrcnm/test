from turtle import *
from random import *
    
clr = randint(0x0,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')
cf = [clrname.upper()]
for x in range(1,90):
        
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    cf.append(clrname.upper())

    
t = Pen()
t.speed(0)
bgcolor("black")
for x in range(60):
    t.pencolor(cf[x%89])
    t.width(x/100 +1)
    t.forward(x)
    t.left(59)
right(180)
for x in range(60):
    t.pencolor("black")
    t.forward(x)
    t.left(-59)
    
rrrr = input("t")

