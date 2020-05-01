from tkinter import*
from random import *
from turtle import *
w = Tk()
rightPressed = 1
tytu = 1
leftPressed = 1
fj = randint(0,1)
rt = []
for x in range(0,5):
    fj = randint(0,3)
    if fj == 0:
        rt.append("Left")

    elif fj == 1:
        rt.append("Right") 

    elif fj == 2:
        rt.append("Up")
    elif fj == 3:
        rt.append("Down")
#print(rt)
print(rt[tytu])
def op(event):
    global leftPressed,rightPressed,tytu
    if tytu >= 5:
        print("you win")
        w.destroy()

    if event.keysym == "Left" and rt[tytu] == "Left":
        if tytu >= 5:
            print("you win")
            w.destroy()

        leftPressed = 1
        print("cool")
        if tytu > 5:
            print("you win")
            w.destroy()

        tytu = tytu + 1

        if tytu >= 5:
            print("you win")
            w.destroy()
        else:
            print(rt[tytu])
    elif event.keysym == "Right" and rt[tytu] == "Right":
        if tytu > 5:
            print("you win")
            w.destroy()
        else:
            print(rt[tytu])
    
        rightPressed = 1
        print("cool")
        tytu = tytu + 1
        if tytu >= 5:
            print("you win")
            w.destroy()
        else:
            print(rt[tytu])
    
#        print(rt[tytu])


    elif event.keysym == "Up" and rt[tytu] == "Up":
        if tytu >= 5:
            print("you win")
            w.destroy()

        leftPressed = 1
        print("cool")
        if tytu > 5:
            print("you win")
            w.destroy()

        tytu = tytu + 1

        if tytu >= 5:
            print("you win")
            w.destroy()
        else:
            print(rt[tytu])

    elif event.keysym == "Down" and rt[tytu] == "Down":
        if tytu >= 5:
            print("you win")
            w.destroy()

        leftPressed = 1
        print("cool")
        if tytu > 5:
            print("you win")
            w.destroy()

        tytu = tytu + 1

        if tytu >= 5:
            print("you win")
            w.destroy()
        else:
            print(rt[tytu])
    else:
        print("you lose")
        w.destroy()
# def on_key_release(event):
#     global leftPressed,rightPressed,tytu
#     if event.keysym == "Left" and rt[tytu] == "Left":
#         leftPressed = 0
#         print("cool")
#         tytu = tytu + 1
#         if tytu > 5:
#             print("you win")
#             w.destroy()
#         print(rt[fj])
#     elif event.keysym == "Right" and rt[tytu] == "Right":
#         rightPressed = 0
#         print("cool")
#         tytu = tytu + 1
#         if tytu > 5:
#             print("you win")
#             w.destroy()
#         print(rt[fj])
#     else:
#         print("you lose")
#         w.destroy()
#w.bind("<KeyRelease>",on_key_release)
w.bind("<KeyPress>",op)
w.mainloop()











