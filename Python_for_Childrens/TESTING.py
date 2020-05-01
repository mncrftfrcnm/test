from random import *

clr = randint(0x0,0xFFFFFF)
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')

while len(clrname) != 7:
    clrname = clrname.replace('#','#0')

print(clrname.upper())
