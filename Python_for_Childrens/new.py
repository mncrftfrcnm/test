from turtle import *
from random import *
hideturtle()
while True:
    trr = int(input("what do you want to do?(1)dot, 2)triagle, 3)another items)"))
    if trr == 1:
        dot()
    if trr == 2:
        goto(120,100)
        goto(240,-40)
        goto(0,0)
    hgh = randint(1,3)
    if trr == 3:
        g = randint(1,100)
        f = randint(1,100)
        if hgh == 1:
            goto(g,f)
                    
            g = randint(1,100)
            f = randint(1,100)
            goto(g,f)
            
            g = randint(1,100)
            f = randint(1,100)
            goto(g,f)
        
            g = randint(1,100)
            f = randint(1,100)
            goto(g,f)
        if hgh ==  2:
            color("blue")
            shape("arrow")
            speed(3)
            forward(50)
            right(90)
            forward(50)
            right(90)

            forward(50)
            right(90)
            forward(50)
            right(90)
            color("white")
            forward(-50)
            left(90)
            forward(50)
            right(90)
            forward(-50)
            left(90)
            forward(-50)
            left(90)
            forward(-50)
            left(90)
            forward(-50)
        if hgh == 3: 
            forward(50)
            goto(-100,100)
            forward(50)
            goto(0,0)


            
        





