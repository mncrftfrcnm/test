from tkinter import *
from threading import Timer

x_movement = 3
def move_Timer(object):
    canvas.move(object, x_movement, 0)
    canvas.xview_scroll(3, UNITS)
    Timer(30/1000, lambda: move_Timer(object)).start()


def move_after(object):
    canvas.move(object, x_movement, 0)
    canvas.xview_scroll(3, UNITS)
    master.after(30, lambda: move_after(object))


master = Tk()

canvas_width = 1000
canvas_height = 600
canvas_scrollregion_width = 3000
canvas_scrollregion_height = 3000
canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="black")
canvas.configure(scrollregion=(0, 0, canvas_scrollregion_width,     canvas_scrollregion_height), yscrollincrement='1', xscrollincrement='1')
x = (master.winfo_screenwidth() / 2) - (canvas_width // 2)
y = (master.winfo_screenheight() / 2) - (canvas_height // 2)
master.geometry('%dx%d+%d+%d' % (canvas_width + 4, canvas_height + 4, x, y))
canvas.pack()

x1, y1 = canvas_scrollregion_width/2, canvas_scrollregion_height/2
ball = canvas.create_oval(x1, y1, x1 + 50, y1 + 50, fill="red")
canvas.xview_moveto((x1 - canvas_width/2)/canvas_scrollregion_width)
canvas.yview_moveto((y1 - canvas_height/2)/canvas_scrollregion_height)


master.bind("d", lambda event: move_Timer(ball))
master.bind('<Right>', lambda event: move_after(ball))
master.bind("<Button-1>", lambda event: print(canvas.canvasx(event.x),canvas.canvasy(event.y)))
master.mainloop()