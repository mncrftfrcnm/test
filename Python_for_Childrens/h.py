import turtle
import random

# function to draw circle
def draw_circle(turtle, color, size, x, y):
  turtle.penup()
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(size)
  turtle.end_fill()
  
  
# function to write message
def write_message(turtle, message, color, x, y, font):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.pensize(8)
  turtle.color(color)
  turtle.write(message, None, None, font)
  
# snowflake colors
snow_colors = ["white", "#80bfff", "#e6f2ff" ]

# set the background color for the page
bg = turtle.Screen()
bg.bgcolor("light blue")

turtle.speed(500)

# head
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.circle(40)
turtle.penup()
turtle.end_fill()

# body
turtle.penup()
turtle.goto(0,-105)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.circle(60)
turtle.penup()
turtle.end_fill()

# left eye
turtle.penup()
turtle.goto(-15,30)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(5)
turtle.penup()
turtle.end_fill()

# right eye
turtle.penup()
turtle.goto(15,30)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(5)
turtle.penup()
turtle.end_fill()

# nose
turtle.penup()
turtle.goto(0,25)
turtle.pendown()
turtle.begin_fill()
turtle.color("pink")
turtle.circle(3)
turtle.penup()
turtle.end_fill()

# left whisker 1
turtle.penup()
turtle.goto(-45,26,)
turtle.color("black")
turtle.pensize(1)
turtle.pendown()
turtle.goto(-21,24)

# left whisker 2
turtle.penup()
turtle.goto(-45,15,)
turtle.color("black")
turtle.pensize(1)
turtle.pendown()
turtle.goto(-20,20)

# right whisker 1
turtle.penup()
turtle.goto(45,26,)
turtle.color("black")
turtle.pensize(1)
turtle.pendown()
turtle.goto(21,24)

# right whisker 2
turtle.penup()
turtle.goto(45,15,)
turtle.color("black")
turtle.pensize(1)
turtle.pendown()
turtle.goto(20,20)

# mouth
turtle.penup()
turtle.goto(0,24)
turtle.color("black")
turtle.pensize(1)
turtle.pendown()
turtle.goto(0,18)
turtle.penup()

# left ear
turtle.goto(-20,69)
turtle.fillcolor("white")
turtle.color("white")
turtle.pensize(2)
turtle.pendown()
turtle.begin_fill()
turtle.goto(-35,61)
turtle.left(90)
turtle.forward(20)
turtle.right(124)
turtle.forward(20)
turtle.end_fill()
turtle.penup()

# hat bottom
turtle.goto(5, 86)
turtle.color("black")
turtle.pensize(8)
turtle.pendown()
turtle.goto(45,60)

# hat top
turtle.goto(8,84.488)
turtle.fillcolor("black")
turtle.color("black")
turtle.pensize(4)
turtle.begin_fill()
turtle.goto(42,63)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(20)
turtle.end_fill()
turtle.penup()

# write a message
'''write_message(turtle, "M", "green", -160, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "e", "red", -127, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "o", "white", -107, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "w", "green", -86, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "y", "red", -54, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "C", "white", -20, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "h", "green", 5, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "r", "red", 29, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "i", "white", 48, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "s", "green", 61, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "t", "red", 79, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "m", "white", 95, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "a", "green", 129, 140, font=('Georgia', 25, 'bold'))
write_message(turtle, "s", "red", 149.5, 140, font=('Georgia', 25, 'bold'))'''

# make it snow 
for i in range(30):
  turtle.penup()
  x = random.randint(-205, 205)
  y = random.randint(-205, 205)
  size = random.randint(1, 5)
  colors = (random.choice(snow_colors))
  turtle.goto(x, y)
  turtle.pendown()
  draw_circle(turtle, colors, size, x, y)
  turtle.penup()

# send turtle to the corner 
turtle.penup()
turtle.goto(250,250)
rrerr = input("L")