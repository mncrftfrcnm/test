from turtle import *
from random import *
t = Pen()
#t.hideturtle()
while True:
    xcoord=randint(-250,200)
    ycoord=randint(-200,50)
    xwindow=randint(-50,0)
    ywindow=randint(-10,20)
    height = randint(100,300)
    bgb = randint(100,300)
    yty = bgb/2
    yt = height/2
    ii = randint(0,10)
    m = randint(-700,700)
    n = randint(-700,700)
    t.pensize(ii)
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.penup()
    t.goto(0+xcoord,height+ycoord)
    t.pendown()
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.goto(bgb+xcoord,height+ycoord)
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
            
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    t.pensize(ii)
    t.color(clrname.upper())
    t.pensize(ii)
    t.goto(bgb+xcoord,0+ycoord)

    clr = randint(0x0,0xFFFFFF)
        
    t.pensize(ii)
    t.goto(0+xcoord,0+ycoord)
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.goto(0+xcoord,height+ycoord)
    clr = randint(0x0,0xFFFFFF)
        
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
            
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    t.color(clrname.upper())
    t.pensize(ii)
    t.goto(bgb/2+xcoord,height+40+ycoord)
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.goto(bgb+xcoord,height+ycoord)
    t.penup()
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.goto(yty+xcoord+xwindow,yt+ycoord+ywindow)
    t.pendown()
    t.goto(yty+xcoord+xwindow,yt+yt/2+ycoord+ywindow)
    clr = randint(0x0,0xFFFFFF)
        
 
    t.pensize(ii)
    t.goto(yty+yty/2+20+xcoord+xwindow,yt+yt/2+ycoord+ywindow)
    clr = randint(0x0,0xFFFFFF)
        
 

    t.goto(yty+yty/2+20+xcoord+xwindow,yt+ycoord+ywindow)
    clr = randint(0x0,0xFFFFFF)
        
 

    t.goto(yty+xcoord+xwindow,yt+ycoord+ywindow)
    t.goto(yty+xcoord+yty/2+xwindow,yt+ycoord+ywindow)
    t.goto(yty+xcoord+yty/2+xwindow,yt+ycoord+yt/2+ywindow)
    t.goto(yty+xcoord+yty/2+xwindow,yt+ycoord+yt/4+ywindow)
    t.goto(yty+xcoord+xwindow,yt+ycoord+yt/4+ywindow)
    
    #t.forward(20)
    #t.left(90)
    #t.forward(yt)
 #   t.penup()
 #   t.goto(m+xcoord,n+ycoord)
 #   t.pendown()

    #goto(bgb,height)
#    uji = input("uj:")




