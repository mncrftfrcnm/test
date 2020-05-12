import turtle
import math
import random
import time
from animations import setup, congratulate
shoot = turtle.Turtle()
shoot.shape("turtle")
shoot.color("blue")
shoot.penup()
enemy = turtle.Turtle()
enemy.hideturtle()
enemy.shape("circle")
enemy.color("red")
enemy.penup()
enemy.speed(2)
random.seed()
myscreen = turtle.Screen()
setup(myscreen)
