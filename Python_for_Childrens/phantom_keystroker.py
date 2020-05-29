import turtle
import time
import random
from random import *
from turtle import *
t = Turtle()
t.hideturtle()
t.pu()
t.speed(0)
tre = 10
ret = [1,2,3,4,5,6,7,8,9,0,"!","@","$","%","q","w","e","t","r","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","z","x","c","v","b","n","m"]
while True:
    for y in range(30):
        rety = choice(ret)
        t.write(rety)
        t.forward(10)
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t.color(clrname.upper())
    t.home()
    t.right(90)
    t.forward(tre)
    t.left(90)
    tre = tre + 10