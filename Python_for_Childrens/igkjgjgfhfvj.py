import tkinter
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC
import threading
from threading import Timer
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
        move_bat()
        if ischanged == False:
            (ballLeft, ballTop, ballRight, ballBottom) = c.coords(ball)
            c.coords(ball, ballLeft+ballMoveX, ballTop+ballMoveY, ballRight+ballMoveX+ballsize, ballBottom+ballMoveY+ballsize)
            ischanged = True
            ranfill=lambda: random.randint(50,255)
            ballfill='#%02X%02X%02X' % (ranfill(),ranfill(),ranfill())
            c.itemconfig(ball,fill=ballfill)

        move_ball()
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


def move_bat():
    batMove = batSpeed*rightPressed - batSpeed*leftPressed
    (batLeft,batTop,batRight,batBottom) = c.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        c.move(bat,batMove,0)
ballMoveX = 4                     
ballMoveY = -4
setBatTop = canvasHeight-40
setBatBottom = canvasHeight-30

def move_ball():
    global ballMoveX,ballMoveY, score, bounceCount,batSpeed,ballsize,ballsizecheck
    (ballLeft, ballTop, ballRight, ballBottom) = c.coords(ball)
    
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
#        ballsize = ballsize + 100
    if ballMoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
        
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft,batTop,batRight,batBottom) = c.coords(bat)

        #Ball bounced to bat
        if (ballMoveX > 0 and (ballRight + ballMoveX > batLeft and ballLeft < batRight) 
        or ballMoveX < 0 and (ballRight > batLeft and ballLeft + ballMoveX < batRight)):
            PlaySound("sounds/Windows Critical Stop.wav", SND_ASYNC)
            clr = randint(0x0,0xFFFFFF)
            
            clrtxt = str(hex(clr))
            clrname = clrtxt.replace('0x','#')
                
            while len(clrname) != 7:
                clrname = clrname.replace('#','#0')            
            c.config(background=clrname)
            ballMoveY = -ballMoveY
            score = score +1
            bounceCount = bounceCount+ 1
            randfill=lambda: random.randint(100,255)
            batfill='#%02X%02X%02X' % (randfill(),randfill(),randfill())
            c.itemconfig(bat,fill=batfill)
        ###################################
            if bounceCount == 3:                
                ballsize = ballsize + 3
                bounceCount = 0
                ChangeBallSize()
                batSpeed = batSpeed+3
                ranfill=lambda: random.randint(100,255)
                ballfill='#%02X%02X%02X' % (ranfill(),ranfill(),ranfill())
                c.itemconfig(ball,outline=ballfill)
#                batSpeed = batSpeed + 9000
                
                if ballMoveX > 0:
                    ballMoveX = ballMoveX+3
                else:
                    ballMoveX = ballMoveX-3
                ballMoveY = ballMoveY - 1 
    c.move(ball,ballMoveX,ballMoveY)

def check_game_over():
    (ballLeft,ballTop,ballRight,ballBottom) = c.coords(ball)
    if ballTop > canvasHeight:
        my = tkinter.messagebox.askyesno(title="GAME OVER",message="Your score is " + str(score) + "\n" + "Play again?") 
        if my == True:
            reset()
        else:
            close()
def close():
    global wo
    wo = False
    w.destroy()
    
def reset():
    global score, bounceCount, batSpeed
    global rightPressed, leftPressed
    global ballMoveX, ballMoveY, ballsize
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY = -4
    c.coords(bat, 10, setBatTop, 110, setBatBottom)
    c.coords(ball, 10, setBatTop-20, 30, setBatTop)
    score = 0
    bounceCount = 0
    batSpeed = 6
    ballsize=10
w.protocol("WM_DELETE_WINDOW",close)  
w.bind("<KeyPress>",op)
w.bind("<KeyRelease>",on_key_release)
reset()
main_loop()

























































































































































































































































































































































































































