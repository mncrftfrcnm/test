
from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
wait_seconds = 1
WinWidth=750

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            PlaySound("C:\windows\media\Ring02.wav",False)
            
beep  = beeper()
beep.start()

wo = True
ballsizecheck = True
WinTk = Tk()
Canv = Canvas(WinTk, width=WinWidth, height=500, bg="white")
Canv.pack()
Tr = Canv.create_polygon(50,90,100,20,140,90,fill="blue")
yt = Canv.create_polygon(100,90,100,20,140,90,fill="yellow")
iung = Canv.create_polygon(200,90,100,20,140,90,fill="green")
ng = Canv.create_polygon(300,180,290,20,140,90,fill="brown")
gn = Canv.create_polygon(300,180,290,30,190,90,fill="orange")
bombfield = []
squaresToClear=0
gameOver = False
score = 0

def gh(event):
    global bombfield
    score = 0
    gameOver = False
    squaresToClear = 0
    def play_bombdodger():
        global bombfield, squaresToClear
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





def pp(event):
    import igkjgjgfhfvj
def yyyy(event):
    import trtjg

def yyn(event):
    import forcalculator
def yhy(event):
    import mama
rbf = input("if you want to play music print y")
if rbf == "y":
    import music
import test
Canv.tag_bind(iung, "<Button-1>",yyyy)

Canv.tag_bind(ng, "<Button-1>",yyn)

Canv.tag_bind(gn, "<Button-1>",yhy)


Canv.tag_bind(Tr, "<Button-1>",gh)
Canv.tag_bind(yt, "<Button-1>",pp)
WinTk.mainloop()












































