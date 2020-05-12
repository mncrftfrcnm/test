from tkinter import*
from random import *
import turtle

from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
from turtle import *
screen = turtle.Screen()
t = Turtle()
t.pu()
screen.onscreenclick(t.goto)
def E1():
    t.write("1")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E2():
    t.write("2")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E3():
    t.write("3")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E4():
    t.write("4")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E5():
    t.write("5")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E6():
    t.write("6")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E7():
    t.write("7")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E8():
    t.write("8")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E9():
    t.write("9")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E0():
    t.write("0")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def Q():
    t.write("Q")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def W():
    t.write("W")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def E():
    t.write("E")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def R():
    t.write("R")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def T2():
    t.write("T")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def Y():
    t.write("Y")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def U():
    t.write("U")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def O():
    t.write("O")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def P():
    t.write("P")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def A():
    t.write("A")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def S():
    t.write("S")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def D():
    t.write("D")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def i():
    t.write("i")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def F():
    t.write("F")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def G():
    t.write("G")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def H():
    t.write("H")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def J():
    t.write("J")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def K():
    t.write("k")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def L():
    t.write("L")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def Z():
    t.write("Z")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def X():
    t.write("X")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def C():
    t.write("C")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def V():
    t.write("V")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def B():
    t.write("B")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def N():
    t.write("N")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def M():
    t.write("M")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def q():
    t.write("q")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def w():
    t.write("w")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def e():
    t.write("e")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def r():
    t.write("r")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def t2():
    t.write("t")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def y():
    t.write("y")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def u():
    t.write("u")
    t.forward(10)

    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def o():
    t.write("o")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def p():
    t.write("p")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def a():
    t.write("a")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def I():
    t.write("I")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def s():
    t.write("s")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def d():
    t.write("d")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def f():
    t.write("f")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def g():
    t.write("g")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def h():
    t.write("h")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def j():
    t.write("j")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def k():
    t.write("k")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def l():
    t.write("l")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def z():
    t.write("z")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def x():
    t.write("x")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def c():
    t.write("c")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def v():
    t.write("v")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def b():
    t.write("b")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def n():
    t.write("n")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

def m():
    t.write("m")
    t.forward(10)
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    t.color(clrname.upper())

listen()
screen.onkey(q,"q")
screen.onkey(w,"w")
screen.onkey(e,"e")
screen.onkey(r,"r")
screen.onkey(t2,"t")
screen.onkey(y,"y")
screen.onkey(u,"u")
screen.onkey(o,"o")
screen.onkey(p,"p")
screen.onkey(a,"a")
screen.onkey(s,"s")
screen.onkey(d,"d")
screen.onkey(f,"f")
screen.onkey(g,"g")
screen.onkey(h,"h")
screen.onkey(j,"j")
screen.onkey(i,"i")
screen.onkey(k,"k")
screen.onkey(l,"l")
screen.onkey(z,"z")
screen.onkey(x,"x")
screen.onkey(c,"c")
screen.onkey(v,"v")
screen.onkey(b,"b")
screen.onkey(n,"n")
screen.onkey(m,"m")
screen.onkey(Q,"Q")
screen.onkey(W,"W")
screen.onkey(E,"E")
screen.onkey(R,"R")
screen.onkey(T2,"T")
screen.onkey(Y,"Y")
screen.onkey(U,"U")
screen.onkey(O,"O")
screen.onkey(P,"P")
screen.onkey(A,"A")
screen.onkey(S,"S")
screen.onkey(D,"D")
screen.onkey(F,"F")
screen.onkey(I,"I")
screen.onkey(G,"G")
screen.onkey(H,"H")
screen.onkey(J,"J")
screen.onkey(K,"K")
screen.onkey(L,"L")
screen.onkey(Z,"Z")
screen.onkey(X,"X")
screen.onkey(C,"C")
screen.onkey(V,"V")
screen.onkey(B,"B")
screen.onkey(N,"N")
screen.onkey(M,"M")
screen.onkey(E1,"1")
screen.onkey(E2,"2")
screen.onkey(E3,"3")
screen.onkey(E4,"4")
screen.onkey(E5,"5")
screen.onkey(E6,"6")
screen.onkey(E7,"7")
screen.onkey(E8,"8")
screen.onkey(E9,"9")
screen.onkey(E0,"0")
mainloop()
