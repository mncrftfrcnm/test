from tkinter import *            
mm = Tk()
g = Canvas(mm, width=750, height=500, bg="white")
g.pack()
while True:
    jhg = input("what color do you wanna:")
    
    g.configure(background=jhg)
    jh = input("what width do you wanna:")
    g.configure(width=jh)
    jh = input("what height do you wanna:")
    g.configure(height=jh)