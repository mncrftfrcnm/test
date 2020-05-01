from turtle import *
from random import *
t = Pen()

while True:
    t.pu()
    tyu = randint(-500,500)
    tre = randint(-500,500)
    t.goto(tre,tyu)
    hhj = randint(0,1)
    t.pd()
    if hhj == 0:
        for i in range(50):
    
            t.forward(i)
            t.left(91)
    if hhj == 1:    
        for i in range(5):
            t.forward(50)           
            t.right(144)
    t.pu()
    