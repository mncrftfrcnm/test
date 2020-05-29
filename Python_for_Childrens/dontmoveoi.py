from turtle import *
screen = Screen()
t = Pen()
t.pu()

def forw():
    t.forward(100)
    x,y = t.pos()
    if x > 450 or y > 450 or x < -450 or y < -450:
        print("game over")
        screen.setup(0,0)
screen.onkey(forw,"w")
listen()
while True:
    t.right(360) 