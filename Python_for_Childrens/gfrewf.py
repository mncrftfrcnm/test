import tkinter as tk
from random import *

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.pack()

shape_id = canvas.create_oval(0, 0, 100, 100,fill="white")

def move_oval(event):
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    canvas.coords(shape_id, event.x - 50, event.y - 50, event.x + 50, event.y + 50)
    canvas.configure(background=clrname)
canvas.bind('<1>', move_oval)

root.mainloop()