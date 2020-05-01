from turtle import Turtle, Screen

screen = Screen()

DIAMETER = 200
STAMP_SIZE = 20
BACKGROUND = screen.bgcolor()

yertle = Turtle('circle', visible=False)
yertle.penup()

yertle.shapesize(DIAMETER / STAMP_SIZE)
yertle.color('black', BACKGROUND)  # drop second argument for a filled semicircle
yertle.stamp()

yertle.shape('square')
yertle.shapesize(stretch_len=(DIAMETER / 2) / STAMP_SIZE)
yertle.color(BACKGROUND)
yertle.forward(DIAMETER / 4)
yertle.stamp()
ijm = input("jdxbfuxgugdfydegfufhdfshgsjfhjhjdfhgzsdgf irye gl oers lgre uf uire brikrfhguglotehfdhjgifdjhggikfsdjjgkl.fsdhggrldfkhgligwr")