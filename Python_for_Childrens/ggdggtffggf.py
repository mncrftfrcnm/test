from turtle import *


while True:
    nb = input("what shape do you wanna?(1)turtle 2)arrow)?")
    hg = input("were do you want to go?(1)left, 2)right, 3)forward)?")
    gh = int(input("how many do you wanna to go?"))
    color("blue")
    fb = str(nb)
    hb = str(hg)
    fg = str(gh)
    if fb == 1:
        shape("turtle")

    if fb == 2:
        shape("arrow")
        pass
    speed(4)
    if hb == 1:
        shape(fb)
        left(fg)
    elif hb == 2:
        shape(fb)
        right(fg)
    elif hb == 3:
        shape(fb)
        forward(fg)
    rt = input("jjjd")
rt = input("jjjd")


    




