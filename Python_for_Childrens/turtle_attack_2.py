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
import turtle
from turtle import *
import teleport
import all_my_commands
screen = Screen()
t = Pen()
t.speed(1)
listen()
t.pu()
def ata53():
    t1 = t.clone()
    t1.left(90)
    x,y = t.pos()
    t1.goto(x,y+10)
    t2 = t.clone()
    x,y = t.pos()
    t2.goto(x,y-10)
    t2.left(-90)
    t3 = t.clone()
    x,y = t.pos()
    t3.goto(x+10,y)
    t4 = t.clone()
    x,y = t.pos()
    t4.left(180)
    t4.goto(x-10,y)
screen.onkey(ata53,'4')
def ata73():
    t1 = t.clone()
    x,y = t.pos()
    t1.goto(x,y+5)
    t2 = t.clone()
    x,y = t.pos()
    t2.goto(x,y-5)
    t3 = t.clone()
    x,y = t.pos()
    t3.goto(x+5,y)
    t4 = t.clone()
    x,y = t.pos()
    t4.goto(x-5,y)
    t1.speed(0)
    t2.speed(0)
    t3.speed(0)
    t4.speed(0)
    while True:
        
        x,y = t.pos()
        t1.goto(x,y+5)
        #t2 = t.clone()
        x,y = t.pos()
        t2.goto(x,y-5)
        #t3 = t.clone()
        x,y = t.pos()
        t3.goto(x+5,y)
        t4 = t.clone()
        x,y = t.pos()
        #t4.goto(x-5,y)
screen.onkey(ata73,'5')
def ata93():
    t1 = t.clone()
    x,y = t.pos()
    t1.goto(x,y+5)
    t2 = t.clone()
    x,y = t.pos()
    t2.goto(x,y-5)
    t3 = t.clone()
    x,y = t.pos()
    t3.goto(x+5,y)
    t4 = t.clone()
    x,y = t.pos()
    t4.goto(x-5,y)
    for x in range(200):
        t1.forward(1)
        t2.forward(1)
        t3.forward(1)
        t4.forward(1)
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
screen.onkey(ata93,'/')
def ata101():
    t1 = t.clone()
    t1.left(90)
    x,y = t.pos()
    t1.goto(x,y+10)
    t2 = t.clone()
    x,y = t.pos()
    t2.goto(x,y-10)
    t2.left(-90)
    t3 = t.clone()
    x,y = t.pos()
    t3.goto(x+10,y)
    t4 = t.clone()
    x,y = t.pos()
    t4.left(180)
    t4.goto(x-10,y)
    while True:

        x,y = t.pos()
        t1.goto(x,y+10)
        x,y = t.pos()
        t2.goto(x,y-10)
        x,y = t.pos()
        t3.goto(x+10,y)
#        t4 = t.clone()
        x,y = t.pos()
#        t4.left(180)
        t4.goto(x-10,y)
screen.onkey(ata101,'A')
# def ata53():
#     t1 = t.clone()
#     x,y = t.pos()
#     t1.goto(x,y+5)
#     t2 = t.clone()
#     x,y = t.pos()
#     t2.goto(x,y-5)
#     t3 = t.clone()
#     x,y = t.pos()
#     t3.goto(x+5,y)
#     t4 = t.clone()
#     x,y = t.pos()
#     t4.goto(x-5,y)
# screen.onkey(ata53,'4')

def ata43():
    t1 = t.clone()
    x,y = t1.pos()
    while x < 450:
        t1.forward(1)
        x,y = t1.pos()
    tre = randint(0,1)
    if tre == 0:
        t1.right(190)
    if tre == 1:
#        print("U")
        t1.left(190)
    for x in range(100):
        t1.forward(1)
    t1.hideturtle()

screen.onkey(ata43,',')

def ata53():
    t1 = t.clone()
    t1.speed(0)
    t1.hideturtle()
    t1.right(90)
    x = randint(-450,450)
    t1.goto(x,400)
    t1.showturtle()
    t1.speed(1)
    for d in range(420):
        t1.forward(1)
    t1.shape("square")



screen.onkey(ata53,'0')
def ata1000():
    t1 = t.clone()
    t1.shape("circle")
    t1.left(90)
    t1.forward(50)
    while True:
        x = randint(-300,300)
        y = randint(-300,300)
        t1.goto(x,y)
        x,y = t.pos()
        t1.goto(x,y+50)
    


screen.onkey(ata1000,'?')
def ata34():
    t1 = t.clone()
    # print("O")
    t1.forward(10)
    t1.hideturtle()
screen.onkey(ata34,'x')
def stoptime():
    time.sleep(3)
def a():
    z = Turtle()
    z.pu()
    z.hideturtle()
    x,y = t.pos()
    z.goto(x+20,300)
    x,y = t.pos()
    x2,y2 = z.pos()
    z.showturtle()
    while y != y2:
        z.goto(x2,y)
        x,y = t.pos()
        x2,y2 = z.pos()
    za = z.clone()
    for y in range(100):
    #    z.goto(x2,y)
        z.forward(1)
        x2,y2 = za.pos()
    #print("J")
    za.hideturtle()
    z.hideturtle()
    
screen.onkey(a,'1')        
def n():
    Screen().bgcolor("black")
    time.sleep(2)
    Screen().bgcolor("white")
screen.onkey(n,'2')
def search_snake():
    t54 = t.clone()
    for x in range(4):
        t54.forward(400)
        t54.left(90)
    t54.hideturtle()
screen.onkey(search_snake,'3')
def crash():
    t1 = t.clone()
    t1.shape("circle")
    x,y = t.pos()
    t1.goto(300,y)
    
    #time.sleep(2.05)
    #t1.shape("classic")
    t2 = t1.clone()
    t2.shape("classic")
    t2.left(90)
    t3 = t1.clone()
    t3.shape("classic")
    t3.left(180)
    t4 = t1.clone()
    t4.shape("classic")
    t4.left(270)
    t1.shape("classic")
    for x in range(10):
        t1.forward(10)
        clr = randint(0x0,0xFFFFFF)

        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')

        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t1.color(clrname.upper())

        t2.forward(10)
        clr = randint(0x0,0xFFFFFF)

        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
        

        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t2.color(clrname.upper())

        t3.forward(10) 
        clr = randint(0x0,0xFFFFFF)

        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')

        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t3.color(clrname.upper())


        t4.forward(10) 
        clr = randint(0x0,0xFFFFFF)

        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')

        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')

        t4.color(clrname.upper())   


    
screen.onkey(search_snake,' ')
screen.onkey(crash,'-')
def at():   
    print("U")
    t34 = t.clone()
    t34.hideturtle() 
    t34.speed(1)
    te = randint(0,2)
    if te == 0:
        x,y = t.pos()
        t34.goto(x,y)
    if te == 1:
        x,y = t.pos()
        t34.goto(x,y-10)
    if te == 2:
        x,y = t.pos()
        t34.goto(x,y+10)
    t34.showturtle()
    t34.forward(200)
    t34.hideturtle() 
screen.onkey(at,'o')        
screen.onkey(stoptime,'p')
def TimerToChange():
#    global wait_seconds, wo
    OurTask=Timer(2.05,TimerToChange)
    OurTask.start()
screen.onscreenclick(t.goto)
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            def ata():
                t1 = t.clone()
                t1.shape("circle")
                t1.pu()
                #                time.sleep(2.05)
#                t1.shape("classic")
                t2 = t1.clone()
                t2.shape("classic")
                t2.left(90)
                t3 = t1.clone()
                t3.shape("classic")
                t3.left(180)
                t4 = t1.clone()
                t4.shape("classic")
                t4.left(270)
                t1.shape("classic")
                for x in range(10):
                    t1.forward(10)
                    clr = randint(0x0,0xFFFFFF)
                    
                    clrtxt = str(hex(clr))
                    clrname = clrtxt.replace('0x','#')
                        
                    while len(clrname) != 7:
                        clrname = clrname.replace('#','#0')

                    t1.color(clrname.upper())

                    t2.forward(10)
                    clr = randint(0x0,0xFFFFFF)
                    
                    clrtxt = str(hex(clr))
                    clrname = clrtxt.replace('0x','#')
                         

                    while len(clrname) != 7:
                        clrname = clrname.replace('#','#0')

                    t2.color(clrname.upper())

                    t3.forward(10) 
                    clr = randint(0x0,0xFFFFFF)
                    
                    clrtxt = str(hex(clr))
                    clrname = clrtxt.replace('0x','#')
                        
                    while len(clrname) != 7:
                        clrname = clrname.replace('#','#0')

                    t3.color(clrname.upper())


                    t4.forward(10) 
                    clr = randint(0x0,0xFFFFFF)
                    
                    clrtxt = str(hex(clr))
                    clrname = clrtxt.replace('0x','#')
                        
                    while len(clrname) != 7:
                        clrname = clrname.replace('#','#0')

                    t4.color(clrname.upper())

                def ata2():

                    class beeper2(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()
                                t1.goto(x,y)
                    beep2  = beeper2()
                    beep2.start()
                    class beeper3(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()
                                t2.goto(x,y)
                    beep3  = beeper3()
                    beep3.start()
                    class beeper4(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning: 
                                x,y = t.pos()
                                t3.goto(x,y)
                    beep4  = beeper4()
                    beep4.start()
                    class beeper5(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()
                                t4.goto(x,y)
                    beep5  = beeper5()
                    beep5.start()
                listen()
                screen.onkeypress(ata2,'q')       
                def ata3():
                    class beeper6(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()
                                t1.goto(x+100,y)
                                t1.hideturtle()
                    beep6  = beeper6()
                    beep6.start()
                    class beeper7(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()       
                                t2.goto(x+100,y)
                                t2.hideturtle()
                    beep7  = beeper7()
                    beep7.start()
                    class beeper8(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning: 
                                x,y = t.pos()
                                t3.goto(x+100,y)
                                t3.hideturtle()
                    beep8  = beeper8()
                    beep8.start()
                    class beeper9(threading.Thread):
                        def run(self):
                            self.keeprunning = True
                            while self.keeprunning:
                                x,y = t.pos()
                                t4.goto(x+100,y)
                                                
                                t4.hideturtle()
                    beep9  = beeper9()
                    beep9.start()           

                    t2.hideturtle()
                    t3.hideturtle()
                    t4.hideturtle()                    
                screen.onkey(ata3,'e')         
                # t1.hideturtle()
                # t2.hideturtle()
                # t3.hideturtle()
                # t4.hideturtle()
            screen.onkey(ata,'w')
                

     
beep  = beeper()
beep.start()

mainloop()

