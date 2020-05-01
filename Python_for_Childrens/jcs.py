from random import *
from tkinter import*

from tkinter import *
w = Tk()
def clicked(event):
    clr = randint(0x0,0xFFFFFF)
                  
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')

    c.configure(background = clrname)
    #w.quit()
def clicked2(event):
    c.quit() 
c = Canvas(w, relief = FLAT, background = "#D2D2D2")
c.pack()
buttonBG = c.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
buttonTXT = c.create_text(50, 15, text="press it!")

buttonBG2 = c.create_rectangle(100, 150, 100, 30, fill="grey40", outline="grey60")
buttonTXT2 = c.create_text(100, 150, text="no! press it!")
c.tag_bind(buttonBG, "<Button-1>", clicked)
c.tag_bind(buttonTXT, "<Button-1>", clicked)
c.tag_bind(buttonBG2, "<Button-1>", clicked2)
c.tag_bind(buttonTXT2, "<Button-1>", clicked2)
w.mainloop()