import words
from turtle import *
from random import *
q = Screen()
t = Turtle()
t.pu()
t.forward(70)
t2 = Pen()
t2.pu()
t2.forward(-40)
r = 0
o = 0         

def cd():
    clear()
    ht()
    write(choice(words.mass))
def ri(x,y):
    global r
    r = r+1
    cd()
def ru(x,y):
    global o
    o = o+1
    cd()
def en():
    global o,r
    print('right',r,', bad',o)
t.onclick(ri)
listen()
t2.onclick(ru)
q.onkey(en,'w')
cd()
mainloop()