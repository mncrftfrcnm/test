from turtle import *
from random import *
f = True
while f == True:
    color("blue")
    shape("arrow")
    speed(randint(0,10))
    ret = randint(1,4)
    if ret == 1:
        forward(randint(50,100))
    if ret == 2:
        left(randint(50,100))
    if ret == 3:
        right(randint(50,100))
    if ret == 4:
        forward(randint(-100,-50))
    
