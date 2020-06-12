from turtle import *
from random import *
screen = Screen()
t=Pen()
t.ondrag(t.goto)
t.begin_fill()
def ef():
    t.end_fill()
    t.begin_fill()
listen()
screen.onkey(ef,'w')
while True:
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
            
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper(),clrname.upper())

#    t.color("green",'yellow')

mainloop()