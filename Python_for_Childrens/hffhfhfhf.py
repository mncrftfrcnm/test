

from turtle import *
import random

title("Snake Game")     #title of the game

setup(555,555)  #sets the screensize into 555x555 px

bgcolor("orange")   #background color

#pressed key functions
def up():
    penup()
    pendown()
    head(90)


def right():
    penup()
    pendown()
    head(0)

def left():
    penup()
    pendown()
    head(180)

def down():
    penup()
    pendown()
    head(270)


#draw dot
def dotx():
    pen2.penup()
    pen2.goto(x1,y1)
    pen2.pendown()
    pen2.dot(20,"green")

#heading of the snake
def head(x):
    for i in range(9999999):
        for ii in range(20):
            seth(x)
            fd(2)
            if xcor()>=250.0 or ycor()>=250.0 or xcor()<=-250.0 or ycor()<=-250.0:
                clear()
                pen2.clear()
                pen4.write("GAME OVER")
                break
            elif (xcor() in x2) and (ycor() in y2):
                pen2.clear()
                pen4.write("EATEN",False,'center',font=('Arial',15,'normal'))
        if xcor()>=250.0 or ycor()>=250.0 or xcor()<=-250.0 or ycor()<=-250.0:
            clear()
            pen2.clear()
            pen4.write("GAME OVER")
            break
        clear()


color("white")
pensize(5)  #pensize

shape('turtle')

#hideturtle()


delay(2)    #delay of animation
speed(10)    #speed of animation

pen2=Pen()  #dots
pen2.hideturtle()

pen4=Pen()
pen4.hideturtle()
pen4.color("white")

#border
pen3=Pen()
pen3.color("white")
pen3.pensize(3)
pen3.hideturtle()
pen3.speed(10)
pen3.penup()
pen3.goto(-250,-250)
pen3.pendown()
for p3 in range(4):
    pen3.fd(500)
    pen3.left(90)


#dots coordinates

x1=random.randint(-225,225)
y1=random.randint(-225,225)
x2=list(range(x1-6,x1+6))
y2=list(range(y1-6,y1+6))


dotx()  #call dots


#controls 
listen()
onkey(up,"Up")
onkey(right,"Right")
onkey(left,"Left")
onkey(down,"Down")
dotx()
mainloop()

















