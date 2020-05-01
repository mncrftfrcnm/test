from time import *
from tkinter import *
w = Tk()
WinWidth=750
Wincenter=WinWidth/2
g = Canvas(w, width=WinWidth, height=500, bg="white")
g.pack()
answ = 0

#Clear screen
def Clear_all():
    g.create_rectangle(0,0,1000,1000,fill="white")

#Play again
def Play_again():
    playag=g.create_rectangle(Wincenter-37,250,Wincenter+57,270,fill="white")
    playagtxt=g.create_text(Wincenter+10,259,text='Play again',font="Calibri 14")
    def playagev(event):
        Clear_all()
        Question1()
        Play_again()
    g.tag_bind(playag,"<Button-1>",playagev)
    g.tag_bind(playagtxt,"<Button-1>",playagev)


def Question1():
    #Making questions
    question=g.create_text(Wincenter,20,text="You see 2 doors",font="Calibri 16")
    question=g.create_text(Wincenter,40,text="Choose 1 or 2",font="Calibri 16")
    #
    #Making answers
    answ1i=g.create_rectangle(Wincenter,70,Wincenter+20,90,fill="white")
    answ1txt=g.create_text(Wincenter+10,79,text='1',font="Calibri 14")
    answ2i=g.create_rectangle(Wincenter,100,Wincenter+20,120,fill="white")
    answ2txt=g.create_text(Wincenter+10,109,text='2',font="Calibri 14")
    #
    #Making events
    def answ1ev(event):
        Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20")
    def answ2ev(event):
        Clear_all()
        Play_again()
        Question2()
    g.tag_bind(answ1i,"<Button-1>",answ1ev)
    g.tag_bind(answ1txt,"<Button-1>",answ1ev)
    g.tag_bind(answ2i,"<Button-1>",answ2ev)
    g.tag_bind(answ2txt,"<Button-1>",answ2ev)

def Question2():
    #Making questions
    question=g.create_text(Wincenter,20,text="You see 3 doors",font="Calibri 16")
    question=g.create_text(Wincenter,40,text="Choose 1 or 2 or 3",font="Calibri 16")
    #
    #Making answers 
    answ1i=g.create_rectangle(Wincenter,70,Wincenter+20,90,fill="white")
    answ1txt=g.create_text(Wincenter+10,79,text='1',font="Calibri 14")
    answ2i=g.create_rectangle(Wincenter,100,Wincenter+20,120,fill="white")
    answ2txt=g.create_text(Wincenter+10,109,text='2',font="Calibri 14")

    answ3i=g.create_rectangle(Wincenter,130,Wincenter+20,150,fill="white")
    answ3txt=g.create_text(Wincenter+10,139,text='3',font="Calibri 14")
    #
    #Making events
    def answ1ev(event):
        Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20") 
    def answ2ev(event):
        Gamesay=g.create_text(Wincenter,200,text="YOU LOSE!",font="Calibri 20")
    def answ3ev(event):
        Gamesay=g.create_text(Wincenter,200,text="YOU WIN!",font="Calibri 20")
        
    g.tag_bind(answ1i,"<Button-1>",answ1ev)
    g.tag_bind(answ1txt,"<Button-1>",answ1ev)   
    g.tag_bind(answ2i,"<Button-1>",answ2ev)
    g.tag_bind(answ2txt,"<Button-1>",answ2ev)   
   
    g.tag_bind(answ3i,"<Button-1>",answ3ev)
    g.tag_bind(answ3txt,"<Button-1>",answ3ev)

#Main program
###################
Question1()
Play_again()
w.mainloop()
###################




