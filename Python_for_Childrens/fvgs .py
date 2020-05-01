from turtle import *
from random import *
while True:
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    color(clrname)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    Screen().bgcolor(clrname)
    ert = randint(-900,900)
    tre = randint(-900,900)
    penup()
    setpos(ert,tre)
    pendown
    write(ert)
    right(90)
    forward(20)
    write(tre)
    left(90)








