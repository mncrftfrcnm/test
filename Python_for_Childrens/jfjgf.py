from turtle import *
from random import *
t = Turtle()
screen = Screen()

pu()
while True:
    t = Turtle()
    t.pu()
    screen.onclick(t.goto)
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
            
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0') 
    t = Turtle()

    t.color(clrname.upper())    



