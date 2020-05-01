from turtle import *
from random import *
t = Pen()
t.shape("turtle")
t.speed(0)
t.pencolor("white")
t.pensize(6)
Screen().bgcolor("turquoise")

def vf(size):
    t.right(25)
    t.forward(size)
    t.backward(size)
    t.left(50)
    t.forward(size)
    t.backward(size)
    t.right(25)
def fdfd(size):
    for x in range(0,4):
        t.forward(size)
        vf(size)
    t.backward(size*4)
def uy(size):
    for x in range(0,6):
        fdfd(size)
        t.right(60)     
def ytyt(size,x,y):
    for c in range(0,4):
        uy(size)   
        t.right(20)
        t.penup()
        t.goto(x,y)    
        t.pendown() 
while True:
    size = randint(5,40)
    x = randint(-500,500)
    y = randint(-500,500)
    t.penup()
#    goto(x,y)
    t.pendown()

    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())
    ytyt(size,x,y)
#    right(36)
hh = input("dd")