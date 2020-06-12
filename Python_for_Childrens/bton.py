from turtle import *
t9 = Turtle()
t9.color("black")
yt9 = 1
def aa(x,y):
    global yt9
    if yt9 == 0:
        Screen().bgcolor("black")
        t9.color('white')
        t9y = 1
    if yt9 == 1:
        Screen().bgcolor("white")
        t9.color("black")
        t9y = 0
    yt9 = t9y
t9.onclick(aa,btn=1)
mainloop()