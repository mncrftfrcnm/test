import random
def random_teleport(t,peed):
    t.speed(0)
    x = random.randint(-400,400)
    t.speed(0)
    y = random.randint(-400,400)
    t.goto(x,y)
    t.speed(peed)
def teleport(t,peed,x,y):
    t.speed(0)
    t.goto(x,y)
    t.speed(peed)