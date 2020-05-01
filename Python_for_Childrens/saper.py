from tkinter import *
from random import *
score = 0
gameOver = False
squaresToClear = 0
def play_bombdodger():
    create_bombfield(bombfield)
    window = Tk()
    layout_window(window)
    window.mainloop()
bombfield = []
def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0,10):
        rowlist = []
        for colown in range(0,10):
            if randint(1,100) < 20:
                rowlist.append(1)
            else:
                rowlist.append(0)
                squaresToClear = squaresToClear + 1
        bombfield.append(rowlist)
    printfield(bombfield)
def printfield(bombfield):
    for rowlist in bombfield:
        print(rowlist)
#play_bombdodger()
def layout_window(window):
    for rownumber, rowlist in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowlist):
            if randint(1,100) < 25:
                square = Label(window, text="    ", bg="darkgreen") 
            elif randint(1,100) > 75:
                square = Label(window, text="    ", bg="seagreen")
            else:
                square = Label(window, text="    ", bg="green")
            square.grid(row=rownumber,column=columnNumber)
            square.bind("<Button-1>", on_click)
#play_bombdodger()
def on_click(event):
    global score
    global gameOver
    global squaresToClear
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currenttext = square.cget("text")
    if gameOver == False:
        if bombfield[row][column] == 1:
            gameOver == True
            square.config(bg="red")
            print("game over!")
            print("your score is ",score)
        elif currenttext =="    ":
            square.config(bg="brown")
            totalbombs = 0
            if row < 9:
                if bombfield[row+1][column] == 1:
                    totalbombs = totalbombs + 1
            if row > 0:

                if bombfield[row-1][column] == 1:
                    totalbombs = totalbombs + 1
            if column > 0:

                if bombfield[row][column-1] == 1:
                    totalbombs = totalbombs + 1
            if column < 9:

                if bombfield[row][column-1] == 1:
                    totalbombs = totalbombs + 1
            if row > 0 and column > 0:

                if bombfield[row-1][column-1] == 1:
                    totalbombs = totalbombs + 1
            if row < 9 and column > 0:

                if bombfield[row+1][column-1] == 1:
                    totalbombs = totalbombs + 1        
            if row > 0 and column < 9:

                if bombfield[row-1][column+1] == 1:
                    totalbombs = totalbombs + 1
            if row < 9 and column < 9:

                if bombfield[row+1][column+1] == 1:
                    totalbombs = totalbombs + 1
            
            square.config(text=" "+ str(totalbombs) +" ")
            squaresToClear = squaresToClear-1
            score = score+1
            if squaresToClear == 0:
                gameOver = True
                print("you win")
                print("your score is",score)
play_bombdodger()










#hhh = input("h")


















































































































































































































































































































































































































































































































































































































































































































































































































