import tkinter
from tkinter import *
import time
w = tkinter.Tk()

Canv = Canvas(w, width=300, height=500, bg="white")                     
Canv.pack()
Canv.create_text(100,240,text=".",font="Calibri 14")
time.sleep(1)
Canv.delete("all")
       
Canv.create_text(100,240,text="..",font="Calibri 14")
time.sleep(1)
w.mainloop()