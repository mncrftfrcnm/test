def r(t):
    x,y = t.pos()
    t.goto(x+1,y)
def l(t):
    x,y = t.pos()
    t.goto(x-1,y)
def u(t):
    x,y = t.pos()
    t.goto(x,y+30)
    x,y = t.pos()
    t.goto(x,y-30)
def d(t):
    x,y = t.pos()
    t.goto(x,y-30)