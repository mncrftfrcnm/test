import turtle
from turtle import *
screen = Screen()
linkTurtle = Turtle()
# this assures that the size of the screen will always be 400x400 ...
screen.setup(1000, 1000)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("cat3.gif")

# Or, set the shape of a turtle
im="cat3.gif"
screen.addshape(im)
im2="cat4.gif"
screen.addshape(im2)

def r():
    linkTurtle.shape(im2)
listen()
screen.onkey(r,"Right")
screen.onkeypress(r,"Right")
while True:
    linkTurtle.shape(im)
screen.onscreenclick(linkTurtle.goto)
mainloop()