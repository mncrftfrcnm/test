from turtle import *
from random import *
f = True

while f == True:
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    color(clrname.upper())
    rew = randint(1,5)
    if rew == 1:
        shape("arrow")
    if rew == 2:
        shape("turtle")
    if rew == 3:
        shape("circle")

    if rew == 4:
        shape("square")

    if rew == 5:
        shape("triangle")
    gfgf = randint(0,5)
    if gfgf == 0:
        pensize(1)
    if gfgf == 1:
        pensize(2)
    if gfgf == 2:
        pensize(3)
    if gfgf == 3:
        pensize(4)
    if gfgf == 4:
        pensize(5)
    if gfgf == 5:
        pensize(6)
    speed(randint(0,10))
    eerer = randint(1,4)
    ret = randint(1,350)
    ter = randint(1,350)
    if eerer == 1:
        goto(ter,ret)
        dot()
    if eerer == 2:
        goto(-ter,-ret)
        dot()
    if eerer == 3:
        goto(-ter,ret)
        dot()    
    if eerer == 4:
        goto(ter, -ret)
        dot()
    






