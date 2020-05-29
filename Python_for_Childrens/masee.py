from turtle import *
from random import *
t = Turtle()
y = 30
t.pu()
screen = Screen()
errt = [0,1,0,2,1,1,1,2,1,1,1,2,0,1,0,1,2,1,0]
for x in errt:
    if x == 1:
       t1 = t.clone()
       t.forward(10)
    elif x == 0:
#         t1 = t.clone()
         t.forward(20)
    if x == 2:
        t1 = t.clone()
        t.setpos(0,0)
        t.right(90)
        t.forward(y)

        t.left(90)
        y = y + 30
    
tre = input("YH")    