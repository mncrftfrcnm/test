from turtle import *
from random import *
t=Pen()
t.speed(0)
t.hideturtle()
while True:
    for x in range(2):
        for y in range(35):
            for x in range(4):
                t.forward(30)
                t.left(90)
                clr = randint(0x0,0xFFFFFF)
                    
                clrtxt = str(hex(clr))
                clrname = clrtxt.replace('0x','#')
                        
                while len(clrname) != 7:
                    clrname = clrname.replace('#','#0')

                t.color(clrname.upper(),clrname.upper())
            t.left(10)
        t.pu()
        t.left(140)
        t.forward(30)
        t.pd()
    t.forward(10)
    t.left(90)
 #   t.write(t)
    
    t.left(100)

#140