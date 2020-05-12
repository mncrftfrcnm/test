from turtle import *
import time
color("orange")
dot(10)
center = pos()
color("blue")
shape("turtle")
speed(0)
pu()
goto(200,0)
pd()
g = 800
v = Vec2D(0, 1)
t = 0
dt = 1
while t < 1100:
    goto(pos() + v* dt)
    setheading(towards(center))
    r = distance(center)
    acc = (-g / r ** 3) * pos()
    v += acc * dt
    t += dt
mainloop()


