from tkinter import *
mm = Tk()
g = Canvas(mm, width=750, height=500, bg="white")
g.pack()
tt = 0
w1i=g.create_rectangle(10,285,30,305,fill="white")
w2i=g.create_rectangle(10,310,30,330,fill="white")
w3i=g.create_rectangle(10,335,30,355,fill="white")
w1txt=g.create_text(20,294,text='1',font="Calibri 14")
w2txt=g.create_text(20,319,text='2',font="Calibri 14")
RF = g.create_text(20,319,text=tt,font="Calibri 14")
def i(event):
    global tt
    tt = 1
def it(event):
    global tt
    tt = 1
g.tag_bind(w1txt, "<Button-1>",i)
g.tag_bind(w1i, "<Button-1>",it)
u = input("y")





