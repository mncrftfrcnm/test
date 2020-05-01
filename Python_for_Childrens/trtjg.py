from tkinter import *
from random import *
mm = Tk()

g = Canvas(mm, width=750, height=500, bg="white")
g.pack()
lx, ly = 0,0
g.create_line(80,0,80,1000)
colline = "black"
wtext=1

def sj(event):
    global lx, ly
    lx = event.x
    ly = event.y
    if (lx<=80): 
       lx=80

def onc(event):
    sj(event)

def od(event):
    if event.x<=80:
        event.x=80
    g.create_line(lx,ly,event.x,event.y,fill=colline,width=wtext)
    sj(event)

g.bind("<Button-1>",onc)
g.bind("<B1-Motion>",od)

ri = g.create_rectangle(10,10,30,30,fill="red")
bli = g.create_rectangle(10,35,30,55,fill="blue")
bi = g.create_rectangle(10,60,30,80,fill="black")
wi = g.create_rectangle(10,85,30,105,fill="white")
pi = g.create_rectangle(10,110,30,130,fill="purple")
unit = g.create_rectangle(10,135,30,155,fill="#DD00DD")
gre = g.create_rectangle(10,160,30,180,fill="green")
el = g.create_rectangle(10,185,30,205,fill="#00EE00")

w1i=g.create_rectangle(10,285,30,305,fill="white")
w2i=g.create_rectangle(10,310,30,330,fill="white")
w3i=g.create_rectangle(10,335,30,355,fill="white")
w1txt=g.create_text(20,294,text='1',font="Calibri 14")
w2txt=g.create_text(20,319,text='2',font="Calibri 14")
w3txt=g.create_text(20,344,text='3',font="Calibri 14")
M=g.create_text(20,369,text='M',font="Calibri 14")
cleari=g.create_rectangle(10,435,57,455,fill="white")
clearitxt=g.create_text(33,444,text='s',font="Calibri 14")
def ll(event):
    global colline
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    colline = clrname
def lI(event):
    global colline
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    colline = clrname
    
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
def clearhh(event):
    g.create_rectangle(80,0,1000,1000,fill="white")

def w1(event):
    global wtext
    wtext = 1

def w2(event):
    global wtext
    wtext = 5

def w3(event):
    global wtext
    wtext = 9
def uuu(event):
    g.create_rectangle(80,0,1000,1000,fill="white")



def sr(event):
    global colline
    colline="red"
def sbl(event):
    global colline
    colline="blue"
def sb(event):
    global colline
    colline="black"
def sw(event):
    global colline
    colline="white"

def sp(event):
    global colline
    colline="purple"
def sy(event):
    global colline
    colline="#00EE00"

def un(event):
    global colline
    colline="#DD00DD"

def ug(event):
    global colline
    colline="green"
    
clr = randint(0x0,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
        
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')
g.tag_bind(ri,"<Button-1>",sr)
g.tag_bind(bli, "<Button-1>",sbl)
g.tag_bind(bi, "<Button-1>",sb)
g.tag_bind(wi, "<Button-1>",sw)
g.tag_bind(pi, "<Button-1>",sp)
g.tag_bind(unit, "<Button-1>",un)
g.tag_bind(gre, "<Button-1>",ug)
g.tag_bind(el, "<Button-1>",sy)
g.tag_bind(w1i, "<Button-1>",w1)
g.tag_bind(w2i, "<Button-1>",w2)
g.tag_bind(w3i, "<Button-1>",w3)
g.tag_bind(w1txt, "<Button-1>",w1)
g.tag_bind(w2txt, "<Button-1>",w2)
g.tag_bind(w3txt, "<Button-1>",w3)
g.tag_bind(cleari, "<Button-1>",clearhh)
g.tag_bind(clearitxt, "<Button-1>",uuu)

clr = randint(0x0,0xFFFFFF)
    
clrtxt = str(hex(clr))
clrname = clrtxt.replace('0x','#')
        
while len(clrname) != 7:
    clrname = clrname.replace('#','#0')
g.tag_bind(M, "<Button-1>",ll)
ueeee = input("g")
mm.mainloop()








