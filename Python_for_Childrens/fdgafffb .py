from random import *
gh = False
while gh == False:
    h = int(input("choose 1)goodbye 2)hello: "))
    if h == 1:
        we = randint(0,2)
        if we == 0:
            print("have a good day!")
            gh = True
            break
        elif we == 1:
            print("bye")
            gh = True
            break
        elif we == 2:
            print("goodbye")
            gh = True
            break
    elif h == 2:
        we = randint(0,1)
        if we == 1:
            print("hi")
        elif we == 0:
            print("hello")        




































































































