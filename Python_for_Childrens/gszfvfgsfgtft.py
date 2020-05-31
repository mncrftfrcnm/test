from tkinter import*
from random import *
import turtle
from turtle import *
t = Turtle()
w = Tk()
rightPressed = 0
tytu = 0
leftPressed = 0
fj = randint(0,1)
rt = []
sco = 0
screen = Screen()
t = Turtle()
fj = randint(0,28)

if fj == 0:
    rt.append("Left")

elif fj == 1:
    rt.append("Right") 
elif fj == 2:
    rt.append("Up")
elif fj == 3:
    rt.append("Down")



elif fj == 4:
    rt.append("Q")
elif fj == 5:
    rt.append("W")
elif fj == 6:
    rt.append("E")
elif fj == 7:
    rt.append("R")
elif fj == 8:
    rt.append("T")
elif fj == 9:
    rt.append("Y")
elif fj == 10:
    rt.append("U")
elif fj == 11:
    rt.append("I")
elif fj == 12:
    rt.append("O")
elif fj == 13:
    rt.append("P")
elif fj == 14:
    rt.append("A")
elif fj == 15:
    rt.append("S")
elif fj == 16:
    rt.append("F")
elif fj == 17:
    rt.append("G")
elif fj == 18:
    rt.append("H")
elif fj == 19:
    rt.append("J")
elif fj == 20:
    rt.append("K")
elif fj == 21:
    rt.append("L")
elif fj == 22:
    rt.append("Z")
elif fj == 23:
    rt.append("X")
elif fj == 24:
    rt.append("C")
elif fj == 25:
    rt.append("V")
elif fj == 26:
    rt.append("B")
elif fj == 27:
    rt.append("N")
elif fj == 28:
    rt.append("M")
#print(rt)
print(rt[tytu])
def op(event):
    global leftPressed,rightPressed,tytu,sco

    fj = randint(0,28)
    if fj == 0:
        rt.append("Left")

    elif fj == 1:
        rt.append("Right") 
    elif fj == 2:
        rt.append("Up")
    elif fj == 3:
        rt.append("Down")



    elif fj == 4:
        rt.append("Q")
    elif fj == 5:
        rt.append("W")
    elif fj == 6:
        rt.append("E")
    elif fj == 7:
        rt.append("R")
    elif fj == 8:
        rt.append("T")
    elif fj == 9:
        rt.append("Y")
    elif fj == 10:
        rt.append("U")
    elif fj == 11:
        rt.append("I")
    elif fj == 12:
        rt.append("O")
    elif fj == 13:
        rt.append("P")
    elif fj == 14:
        rt.append("A")
    elif fj == 15:
        rt.append("S")
    elif fj == 16:
        rt.append("F")
    elif fj == 17:
        rt.append("G")
    elif fj == 18:
        rt.append("H")
    elif fj == 19:
        rt.append("J")
    elif fj == 20:
        rt.append("K")
    elif fj == 21:
        rt.append("L")
    elif fj == 22:
        rt.append("Z")
    elif fj == 23:
        rt.append("X")
    elif fj == 24:
        rt.append("C")
    elif fj == 25:
        rt.append("V")
    elif fj == 26:
        rt.append("B")
    elif fj == 27:
        rt.append("N")
    elif fj == 28:
        rt.append("M")


    if event.keysym == "Left" and rt[tytu] == "Left": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])
    elif event.keysym == "Right" and rt[tytu] == "Right":
        t.forward(10)
        sco = sco + 1
        rightPressed = 0
        print("cool")
        tytu = tytu + 1 
        print(rt[tytu])
    
#        print(rt[tytu])


    elif event.keysym == "Up" and rt[tytu] == "Up": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "Down" and rt[tytu] == "Down":
        t.forward(10)

        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
        sco = sco + 1
        print(rt[tytu])
    elif event.keysym == "Q" and rt[tytu] == "Q": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "W" and rt[tytu] == "W": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "E" and rt[tytu] == "E": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "R" and rt[tytu] == "R": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "T" and rt[tytu] == "T": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "Y" and rt[tytu] == "Y": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "U" and rt[tytu] == "U": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "I" and rt[tytu] == "I": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])











    elif event.keysym == "O" and rt[tytu] == "O": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "P" and rt[tytu] == "P": 

        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "A" and rt[tytu] == "A": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "S" and rt[tytu] == "S": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "D" and rt[tytu] == "D": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "F" and rt[tytu] == "F": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "G" and rt[tytu] == "G": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "H" and rt[tytu] == "H": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "J" and rt[tytu] == "J": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])








    elif event.keysym == "K" and rt[tytu] == "K": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])

    elif event.keysym == "L" and rt[tytu] == "L": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "Z" and rt[tytu] == "Z": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "X" and rt[tytu] == "X": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])










    elif event.keysym == "C" and rt[tytu] == "C": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "V" and rt[tytu] == "V": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "B" and rt[tytu] == "B": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])


    elif event.keysym == "N" and rt[tytu] == "N": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])



    elif event.keysym == "M" and rt[tytu] == "M": 
        t.forward(10)
        leftPressed = 0
        print("cool")
        

        tytu = tytu + 1
 
        sco = sco + 1    
        print(rt[tytu])






    else:
        t.forward(-10)
#        print("you lose")
#        print("your score is ",sco)        
#        w.destroy()
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
