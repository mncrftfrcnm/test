from tkinter import*
import tkinter
w = tkinter.Tk()
Canv = Canvas(w, width=300, height=500, bg="white")                     
Canv.pack()
filename = PhotoImage(file = "constellation-milky-way-star-space-sky-is.jpg")
image = canvas.create_image(50, 50, anchor=NE, image=filename)