from turtle import *

screen = Screen() # create the screen

turtle = Turtle() # create the first turtle
screen.onscreenclick(turtle.goto) # set up the callback for moving the first turtle

turtle2 = Turtle() # create the second turtle

def move_second(): 
    turtle2.back(100)
    turtle2.forward(200)
    turtle2.back(100)
    screen.ontimer(move_second)

screen.ontimer(move_second) 

screen.mainloop()