from tkinter import*
w = Tk()
tryp = 100
def clicked(event):
    global tryp
    c.configure(width = tryp)
    c.configure(height = tryp)
    tryp = tryp + 50

c = Canvas(w, relief = FLAT, background = "#D2D2D2")
c.pack()
buttonBG = c.create_rectangle(0, 0, 100, 30, fill="grey40", outline="grey60")
buttonTXT = c.create_text(50, 15, text="press it!")
c.tag_bind(buttonBG, "<Button-1>", clicked)
c.tag_bind(buttonTXT, "<Button-1>", clicked)

w.mainloop()



