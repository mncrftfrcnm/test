from tkinter import*
from random import*
tryp = 100
etr = 0
#yu = int(input("how many window do you wanna:"))
for x in range(0,33):
    w = Tk()
    clr = randint(0x0,0xFFFFFF)
    
    clrtxt = str(hex(clr))
    clrname = clrtxt.replace('0x','#')
        
    while len(clrname) != 7:
        clrname = clrname.replace('#','#0')
    c = Canvas(w, relief = FLAT, background = clrname)
    c.pack()
    c.configure(width = tryp)
    c.configure(height = tryp)
    tryp = tryp + 50
    etr = etr + 50
    
w.mainloop()







