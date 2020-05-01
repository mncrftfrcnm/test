from tkinter import*
from random import *
from turtle import *
w = Tk()
tryp = 100
def clicked(event):
    global tryp
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    c.configure(width = tryp)
    c.configure(height = tryp)
    c.configure(background=clrname)
    tryp = randint(100,1000)
def clicked2(event):
    tryp = 909000
    c.configure(width = tryp)
    c.configure(height = tryp)
def clicked3(event):

    while True:
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        color(clrname)
        clr = randint(0x0,0xFFFFFF)
        
        clrtxt = str(hex(clr))
        clrname = clrtxt.replace('0x','#')
            
        while len(clrname) != 7:
            clrname = clrname.replace('#','#0')
        Screen().bgcolor(clrname)
        ert = randint(-900,900)
        tre = randint(-900,900)
        penup()
        setpos(ert,tre)
        pendown
        write(ert)
        right(90)
        forward(20)
        write(tre)
        left(90)

c = Canvas(w, relief = FLAT, background = "#D2D2D2")
c.pack()
buttonBG = c.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey")
buttonTXT = c.create_text(50, 15, text="press it!")
c.tag_bind(buttonBG, "<Button-1>", clicked)
c.tag_bind(buttonTXT, "<Button-1>", clicked)
c.tag_bind(buttonBG, "<Button-3>", clicked2)
c.tag_bind(buttonTXT, "<Button-3>", clicked2)
c.tag_bind(buttonTXT, "<Button-2>", clicked3)
c.tag_bind(buttonBG, "<Button-3>", clicked3)
w.mainloop()



