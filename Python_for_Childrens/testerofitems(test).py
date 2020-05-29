
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
from random import *
import sys
import time
c = int(input("choose wearpon: 1)sniper 2)laser 3)bombs 4) arrow 5)remote patrons control 6)another remote patrons control 7) mega patrons 8)3 bullets 9) another 3 bullets 10) boomerang 11) dash 12) circle 13) ninga attack 14) bullets 15)following missiles 16) exo humat 17) magnet 18)???????? 19)cain 20)stupid bullets 21) secret bullets:"))
screen = Screen()
if c == 1:
    
    t = Turtle()
    t.pu()
    t.shape("circle")
    screen.onscreenclick(t.goto)
if c == 15:
    
    t = Turtle()
    t.pu()
    screen.onscreenclick(t.goto)
    def ata():
        x = randint(-300,300)
        y = randint(-300,300)
        t1 = t.clone()
        t1.goto(x,y)
    screen.onkey(ata,'w')

#    evil = Turtle()
#    evil.pu()



#    evil.goto(-300,-300)
#    evil.shape("circl
    def r():
    #    global sco
        x,y = t.pos()
        t.goto(x+1,y)
    def l():
        x,y = t.pos()
        t.goto(x-1,y)
    screen.onkey(l,"Left")
    screen.onkey(r,"Right")
    listen()
if c == 2:
    
    t = Turtle()
    t.pu()
    def ata():
        t1 = t.clone()
        t2 = t.clone()
        t3 = t.clone()
        t4 = t.clone()
        t5 = t.clone()
        t6 = t.clone()
        t7 = t.clone()
        t8 = t.clone()
        t9 = t.clone()
        t10 = t.clone()
        for x in range(500):
            t1.speed(1)
            t2.speed(2)
            t4.speed(4)
            t3.speed(3)
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
            t4.forward(10)
            t5.speed(5)
            t6.speed(6)
            t7.speed(7)
            t8.speed(8)
            t9.forward(10)
            t10.forward(10)
            t9.forward(10)
            t10.forward(10)
    listen()
    screen.onkey(ata,'w')            
if c == 3:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
    listen()
    screen.onkey(ata,'w')
if c == 4:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.pd()
        t2 = t.clone()
        t2.pd()
        t2.hideturtle()
        t2.color("white")
        for x in range(500):
            t1.forward(30)
            t2.forward(25)
if c == 5:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        def f():
            t1.forward(10)
        def b():
            t1.forward(-10)
        def l():
            t1.left(10)
        def r():
            t1.right(10)
        listen()
        screen.onkey(f,"Right")
        screen.onkey(b,"Left")
        screen.onkey(l,"Up")
        screen.onkey(r,"Down") 
    listen()
    screen.onkey(ata,'w')
if c == 6:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        def l():
            t1.left(90)
        def r():
            t1.right(90)
        
        listen()
        screen.onkey(l,"Up")
        screen.onkey(r,"Down")
        for x in range(500):
            t1.forward(10) 
    listen()
    screen.onkey(ata,'w')
if c == 7:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        for x in range(500):
            t1.forward(3)
        t2 = t.clone()
        t2.shapesize(20)
        t2.speed(1)
        for x in range(500):
            t2.forward(3) 
    listen()
    screen.onkey(ata,'w')
if c == 8:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        t2 = t.clone()
        t2.speed(1)
        t2.right(10)
        t3 = t.clone()

        t3.right(-10)
        t3.speed(1)
        for x in range(500):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
            
if c == 8:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        t2 = t.clone()
        t2.speed(1)
        t2.right(10)
        t3 = t.clone()

        t3.right(-10)
        t3.speed(1)
        for x in range(500):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
        
    listen()
    screen.onkey(ata,'w')
if c == 9:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        x,y = t1.pos()
        t1.goto(x,y+10)
        t2 = t.clone()
        t2.speed(1)
#        t2.right(10)
        t3 = t.clone()

#        t3.right(-10)
        t3.speed(1)
        x,y = t3.pos()
        t3.goto(x,y-10)
        for x in range(500):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
        
    def ata():
        t1 = t.clone()
        t1.speed(1)
        x,y = t1.pos()
        t1.goto(x,y+10)
        t2 = t.clone()
        t2.speed(1)
#        t2.right(10)
        t3 = t.clone()

#        t3.right(-10)
        t3.speed(1)
        x,y = t3.pos()
        t3.goto(x,y-10)
        for x in range(500):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
        
    listen()
    screen.onkey(ata,'w')
if c == 10:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        for x in range(30):
            t1.forward(10)
        for x in range(30):
            t1.forward(-10)
        t1.hideturtle()

    listen()
    screen.onkey(ata,'w')
if c == 11:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        x,y = t.pos()
        t.goto(x+50,y)

    listen()
    screen.onkey(ata,'w')
if c == 12:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        x,y = t.pos()
        t.goto(x+100,y)

    listen()
    screen.onkey(ata,'w')
if c == 12:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
#        t1.forward(10)
        for x in range(100):
            t1.right(-10)
            t1.forward(-10)

        t1.hideturtle()
    listen()
    screen.onkey(ata,'w')
if c == 13:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t.hideturtle()
    def ata2():
        t.showturtle()
    listen()
    screen.onkey(ata,'w')
    screen.onkey(ata2,'q')
if c == 14:
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        t1 = t.clone()
        t1.speed(1)
        t1.forward(700)
    listen()
    screen.onkey(ata,'w')
if c == 16:
    rtr = []
    ererrere = 10
    t = Turtle()
    
    screen.onscreenclick(t.goto)

    t.pu()
    def ata():
        global ererrere
        t1 = t.clone()
        t1.speed(1)
        rtr.append('t1')
        t2 = t.clone()
        t2.speed(1)
        rtr.append('t2')
        t2.right(10)
        t3 = t.clone()
        rtr.append('t3')
        t3.right(-10)
        t3.speed(1)
        for x in range(65):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
        
        
        t1 = t.clone()
        t1.speed(1)
        x,y = t1.pos()
        t1.goto(x,y+10)
        t2 = t.clone()
        t2.speed(1)
    #        t2.right(10)
        t3 = t.clone()

    #        t3.right(-10)
        t3.speed(1)
        x,y = t3.pos()
        t3.goto(x,y-10)
        for x in range(65):
            t1.forward(10)
            t2.forward(10)
            t3.forward(10)
        x = randint(-300,300)
        y = randint(-300,300)
        t1 = t.clone()
        t1.goto(x,y)
        t1 = t.clone()
        t1 = t.clone()
        t1.speed(1)
        for x in range(30):
            t1.forward(10)
        for x in range(30):
            t1.forward(-10)
        t1.hideturtle()
        t2 = t.clone()
        t2.shapesize(20)
        t2.speed(1)
        for x in range(500):

            t2.forward(3)
        
        rtr.append('t5')
        rtr.append('t6')

        rtr.append('t7')
        rtr.append('t8')
        rtr.append('t9')
        rtr.append('t10')
        rtr.append('t11')
        rtr.append('t12')
        rtr.append('t13')
        rtr.append('t14')
        rtr.append('t15')
        rtr.append('t16')
        rtr.append('t17')
        rtr.append('t18')
        rtr.append('t19')
        rtr.append('t20')
        rtr.append('t21')
        rtr.append('t22')
        rtr.append('t23')
        rtr.append('t24')
        rtr.append('t25')
        rtr.append('t26')
        rtr.append('t27')
        rtr.append('t28')

        rtr.append('t29')
        rtr.append('t30')
        rtr.append('t31')
        rtr.append('t32')
        rtr.append('t33')
        rtr.append('t34')
        rtr.append('t35')
        rtr.append('t36')
        for yty in rtr:
            yty = Turtle()
            yty.pu()
            yty.right(ererrere)
            ererrere = ererrere + 10
            yty.forward(100)
            time.sleep(0.1)
            yty.hideturtle()
        
        rtr.clear()
        ererrere = 10
        
    
    t.pu()
    def ata2():
        x,y = t.pos()
        t.goto(x+50,y)
    def ata3():
        Screen().bgcolor("black")
        time.sleep(1)
        sys.exit()
    def ata4():
        t.hideturtle()
    def ata5():
        t.showturtle()
    def ata6():
        xf = int(input("where do you want to teleport x: "))
        yf = int(input("where do you want to teleport y: "))
        t.setpos(xf,yf)
    def ata7():
        x = randint(-300,300)
        y = randint(-300,300)
        t.setpos(x,y)
    listen()
    screen.onkey(ata,"w")
    screen.onkey(ata6,"1")
    screen.onkey(ata7," ")
    screen.onkey(ata2,"l")
    screen.onkey(ata3,"q")

    screen.onkey(ata4,"n")
    screen.onkey(ata5,"m")
if c == 17:
    t = Turtle()
    
    screen.onscreenclick(t.goto)
    t.pu()
    t1 = t.clone()
    t1.shape("circle")
    t1.goto(100,100)
    t2 = t.clone()
    t2.goto(500,-500)
    t2.shape("triangle")
    t3 = t.clone()
    t3.goto(-500,500)
    t3.shape("square")
    def ata():

        class beeper(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                    x,y = t.pos()
                    t1.goto(x,y)
        beep  = beeper()
        beep.start()
        class beeper2(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                    x,y = t.pos()
                    t2.goto(x,y)
        beep2  = beeper2()
        beep2.start()
        class beeper3(threading.Thread):
            def run(self):
                self.keeprunning = True
                while self.keeprunning:
                    x,y = t.pos()
                    t3.goto(x,y)
        beep3  = beeper3()
        beep3.start()
    listen()
    screen.onkey(ata,'w')
if c == 18:
    t = Turtle()
    
    screen.onscreenclick(t.goto)
    t.pu()
#    print("o")
    def ata():
        t1 = t.clone()
        t1.forward(10)
        t1.speed(1)
        t1.shape("square")
        def u():
            x,y = t1.pos()
            t1.goto(x,y+10)
        def d():
            x,y = t1.pos()
            t1.goto(x,y-10)
        def l():
            x,y = t1.pos()
            t1.goto(x-10,y)
        def r():
            x,y = t1.pos()
            t1.goto(x+10,y)
        def do():
            x,y = t1.pos()
            t1.hideturtle()
            t2 = t.clone()
            t2.speed(1)
            t2.shape("square")
            t2.goto(x,y)
        listen()
        screen.onkey(u,"Up")
        screen.onkey(d,"Down")
        screen.onkey(l,"Left")
        screen.onkey(r,"Right")
        screen.onkey(do,"r")
    listen()
    screen.onkey(ata,"w")
if c == 19:
    t = Turtle()
    t.shapesize(10)
#    t.pencolor("white")
    t.speed(1)
    
    screen.onscreenclick(t.goto)
    t.pu()
    def ata():
        t1 = t.clone()
        t1.color("black")
#        t1.pd()
        t1.speed(1)
        t1.forward(500)
        t.forward(500)
        t1.hideturtle()
    listen()
    screen.onkey(ata,"w")    
if c == 20:
    t = Turtle()
#    t.shapesize(10)
#    t.pencolor("white")
    t.speed(1)
    
    screen.onscreenclick(t.goto)
    t.pu()
    def ata():
        t1 = t.clone()
        t1.color("black")
        for x in range(50):    
            t1.forward(10)
            t1.circle(10)
    listen()
    screen.onkey(ata,"w")
if c == 21:
    t = Turtle()
#    t.shapesize(10)
#    t.pencolor("white")
    t.speed(1)
    
    screen.onscreenclick(t.goto)
    t.pu()
    def l():
        t.left(10)
    def r():    
        t.right(10)
    def ata():
        t1 = t.clone()
        t1.color("black")
        for x in range(70):    
            t1.forward(10)
    listen()
    screen.onkey(ata,"w")
    screen.onkey(l,"Left")
    screen.onkey(r,"Right")

# if c == 22:
#     t = Turtle()
# #    t.shapesize(10)
# #    t.pencolor("white")
#     t.speed(1)
#     
#     screen.onscreenclick(t.goto)
#     t.pu()






        
# #    t.right(-10)
#     def ata():
#         t1 = t.clone()
#         t1.shape("circle")
        

#     listen()
#     screen.onkey(ata,"w")

mainloop()