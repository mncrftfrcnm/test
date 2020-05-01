from random import *
from turtle import *
from threading import*
from time import *
t = Pen()
#t.hideturtle()
clr = 0
uol = 3
t.speed(0)
g = 10
clr = 0
uuu = 0
ugvyu4e = int(input("how many dots do you wanna:"))
ug = input("what symbol do you wanna:")
oe = int(input("how many lines do you wanna:"))

strWidth=len(ug)

def uu():
    global uuu
    t.forward(10)
    
def u():
    global clr
    t.penup()
    t.goto(-300,200)
    for ioarfut in range(oe):
        for x in range(ugvyu4e):
            
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
            t.write(ug,font=('Webdings',35,"normal"))  
            t.forward(45*strWidth)
        t.forward(-ugvyu4e*45*strWidth)
        t.right(90)
        t.forward(40)
        t.left(90)

        
u() 
y = input("Input any key")
    