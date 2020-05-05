
import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("Black")  
def square():
       for x in range(4):
             t.forward(20)
             t.right(90)           

def Tetris_Piece_1():
  for x in range(4):
      t.begin_fill()
      square()
      t.color("Blue")
      t.end_fill()
      t.color("Black")
      t.forward(20)
import turtle
wn=turtle.Screen()
wn.bgcolor("Black")
t=turtle.Turtle()
t.speed(0)
t.pensize(4)
def square():
  for x in range(4):
    t.forward(20)
    t.right(90)
kd = input("L")






