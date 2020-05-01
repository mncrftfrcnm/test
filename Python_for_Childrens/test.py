from turtle import *
name = input("print  1 or 3 or z:")
hideturtle()
window = Screen()
shape("arrow")
if name == "1":
    goto(35,45)
    goto(35,-100)
if name == "z":
    goto(35,0)
    goto(0,-35)
    goto(35,-35)
if name == "3":
    goto(35,0)
    goto(0,-35)
    goto(35,-50)
    goto(0,-50)
h = input("0")