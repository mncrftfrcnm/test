from turtle import *
screen = Screen()
t = Pen()
t.pu()
screen.onscreenclick(t.goto)          
t.speed(1)
#ondrag(t.goto)
listen()
def j():
    t1 = t.clone()
    #print("L")
    def jk():
        x,y = t1.pos()
        x2,y2 = t.pos()
        if x == x2 and y == y2:
            t1.forward(100)
            t1.hideturtle()
    screen.onkey(jk,'W')
screen.onkey(j,'w')
mainloop()