from turtle import *
import turtle
from random import *
screen = Screen()

turtle = Turtle()
turtle.pu() 
turtle.speed(1)
screen.onscreenclick(turtle.goto) 

turtle2 = Turtle() 
turtle2.speed(1)
turtle2.pu()
def move_second(): 

    tryio = randint(-500,500)
    ty = randint(-500,500)
    turtle2.goto(ty,tryio)
    x,y = turtle.pos()
    x2,y2 = turtle2.pos()
    if x == x2 or y == y2:
        print("game over")                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    screen.ontimer(move_second)

screen.ontimer(move_second) 

screen.mainloop()






