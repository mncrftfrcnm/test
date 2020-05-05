from turtle import *
from random import *
import winsound
from winsound import Beep
yyy = 1
while True:
    t = Turtle()
    ty = randint(0,2)
    if ty == 0: 
        t.shape("turtle")
        winsound.Beep(100,10)
    if ty == 1:
        t.shape("classic")
        winsound.Beep(1000,100)

    if ty == 2:
        t.shape("circle")
        winsound.Beep(123,10)
    x = randint(-600,600)
    y = randint(-600,600)
    t.pu()
    t.goto(x,y)
    yy = randint(1,50)
    for x in range(yy):
        
        t.shapesize(yyy)
        yyy = yyy + 1 
    yyy = 1
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
            
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    t.color(clrname)