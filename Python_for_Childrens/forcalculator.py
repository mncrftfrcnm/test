from math import *
from tkinter import *
WinTk = Tk()
WinWidth=750
hh=0

Canv = Canvas(WinTk, width=WinWidth, height=500, bg="white")
Canv.pack()

def MathObjects():
    Canv.create_rectangle(0,100,1000,1000,fill="lightgrey")
    Tr = Canv.create_polygon(50,90,100,20,140,90,fill="blue")
    Sq= Canv.create_polygon(170,90,170,20,240,20,240,90,fill="green")
    Cir=Canv.create_oval(270,20,340,90,fill="yellow")
    Canv.tag_bind(Tr, "<Button-1>",trisngle)
    Canv.tag_bind(Sq, "<Button-1>",gle)
    Canv.tag_bind(Cir, "<Button-1>",ci)

#Triangle
def trisngle(event):
    Canv.delete("all")
    MathObjects()
    TboxHeight=Entry(Canv)
    TboxBase=Entry(Canv)
    Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
    Canv.create_text(WinWidth/2,200,text="Input height of the triangle:",font="Calibri 14")
    Canv.create_window(WinWidth/2,220,window=TboxHeight)
    Canv.create_text(WinWidth/2,240,text="Input base of the triangle:",font="Calibri 14")
    Canv.create_window(WinWidth/2,260,window=TboxBase)


    clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
    def ll(event):
        Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
        global hh
        HeightTr=TboxHeight.get()
        BaseTr=TboxBase.get()
        hh = float(HeightTr)*float(BaseTr)/2
        Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
    Canv.tag_bind(clearitxt, "<Button-1>",ll)

#Rectangle
def gle(event):
    Canv.delete("all")
    MathObjects()
    TboxHeight=Entry(Canv)
    TboxBase=Entry(Canv)
    Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
    Canv.create_text(WinWidth/2,200,text="Input height of the rectangle:",font="Calibri 14")
    Canv.create_window(WinWidth/2,220,window=TboxHeight)
    Canv.create_text(WinWidth/2,240,text="Input width of the rectangle",font="Calibri 14")
    Canv.create_window(WinWidth/2,260,window=TboxBase)


    clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
    def ll(event):
        Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
        global hh
        HeightTr=TboxHeight.get()
        BaseTr=TboxBase.get()
        hh = float(HeightTr)*float(BaseTr)
        Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
    Canv.tag_bind(clearitxt, "<Button-1>",ll)

#Circle    
def ci(event):
    Canv.delete("all")
    MathObjects()
    TboxHeight=Entry(Canv)
    Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
    Canv.create_text(WinWidth/2,200,text="Input radius of the circle:",font="Calibri 14")
    Canv.create_window(WinWidth/2,220,window=TboxHeight)


    clearitxt=Canv.create_text(WinWidth/2,300,text='Square',font="Calibri 14")
    def ll(event):
        Canv.create_rectangle(WinWidth/2-100,310,WinWidth/2+100,330,fill="white")
        global hh
        HeightTr=TboxHeight.get()
        hh = pi*float(HeightTr)*float(HeightTr)
        Canv.create_text(WinWidth/2,320,text=hh,font="Calibri 14")
    Canv.tag_bind(clearitxt, "<Button-1>",ll)

MathObjects()
WinTk.mainloop()
yy = input("i")




















