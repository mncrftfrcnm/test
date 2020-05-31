from turtle import *
from random import *
t = Turtle()
z = True
y = 0
scren = Screen()
t.forward(100)
t.left(90)
t2 = Turtle()
t2.left(90)
x = 0
s = 0
v = 0
def ata():
    global y,s,z
    print(y)
    s = y
    z = False
def ata2():
    global x,v,z
    print(x)
    v = x
    z = False
    
listen()
scren.onkey(ata,"l")
scren.onkey(ata2,"w")
while z ==  True:
    for b in range(20):
        t.forward(10)
        y = y + 1
    
    for b in range(20):
        t.forward(-10)
        y = y - 1
z = True
while z ==  True:
    for b in range(20):
        t2.forward(10)
        x = x + 1
    
    for b in range(20):
        t2.forward(-10)
        x = x - 1
if v == s:
    print("draw")

if v > s:
    print("2p win")

if s > v:
    print("1p win")