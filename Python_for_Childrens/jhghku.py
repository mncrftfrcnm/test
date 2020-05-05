from turtle import *
import time
t = Pen()
t.shape("circle")
t.width(800)
#t.right(90)
t.speed(1)
t.color("green")

for x in range(50):
    t.color("green")
    t.forward(10)
for x in range(46):
    t.color("white")
    t.forward(-10)
mainloop()


