import tkinter
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC
import threading
from threading import Timer
from move_item import *
from random import *
import random
canvasWidth = 750
canvasHeight = 500
w = tkinter.Tk()
c = tkinter.Canvas(w,width=canvasWidth,height=canvasHeight, bg="dodgerblue4")
c.pack()
bat = c.create_rectangle(100,canvasHeight-300,1100,canvasHeight-400,fill="pink")
ballsize=-20
ball = c.create_oval(0,canvasHeight-30,ballsize,canvasHeight-40,fill="yellow",width=3,outline="white")
wo = True
score = 0
bounceCount = 0
ballsizecheck=False
wait_seconds=1
ballMoveX = 0
ballMoveY = 0
ischanged=False
batSpeed = 6
def main_loop():
    global ballMoveX, ballMoveY, ballsize, ischanged
    global ballMoveX,ballMoveY, score, bounceCount,batSpeed,ballsize,ballsizecheck
#    ballsize = 1000
#    TimerToChange()
#    ballMoveX = ballMoveX - 500
#    ballsize = ballsize + 435
    while wo == True:
        move_bat(batSpeed, rightPressed, leftPressed, c, bat, canvasWidth)
        if ischanged == False:
            (ballLeft, ballTop, ballRight, ballBottom) = c.coords(ball)
            c.coords(ball, ballLeft+ballMoveX, ballTop+ballMoveY, ballRight+ballMoveX+ballsize, ballBottom+ballMoveY+ballsize)
            ischanged = True
            ranfill=lambda: random.randint(50,255)
            ballfill='#%02X%02X%02X' % (ranfill(),ranfill(),ranfill())
            c.itemconfig(ball,fill=ballfill)

#        move_ball()
        w.update()
        time.sleep(0.02)

        if wo == True:
            check_game_over()
leftPressed = 0
rightPressed = 0

def TimerToChange():
    global wait_seconds, wo
    OurTask=Timer(wait_seconds,TimerToChange)
    OurTask.start()
    ChangeBallSize()
    if wo == False:
        OurTask.cancel()

def ChangeBallSize():
    global ballsize, ballsizecheck, ischanged
    yuih = random.randint(100,200)
    if ballsizecheck==False:
        print(ballsize)
        ballsizecheck=True
        ballsize=ballsize+10
        ischanged=False
    else:
        print(ballsize)
        ballsizecheck=False
        ballsize=ballsize+10
        ischanged=False

def op(event):
    global leftPressed,rightPressed,score,batSpeed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
    elif event.keysym == "v":
        tre = int(input("you can upgrate your speed from 1: "))
        if tre <= score:
            batSpeed = batSpeed + tre
            score = score - tre
        else:
            print("you cant do it")
def on_key_release(event):
    global leftPressed,rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    if event.keysym == "Right":
        rightPressed = 0

w.bind("<KeyPress>",op)
main_loop()