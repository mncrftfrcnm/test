import tkinter
from tkinter import *
import time
from tkinter import Tk, Canvas, Frame, Button
from tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT
w = tkinter.Tk()

Canv = Canvas(w, width=300, height=500, bg="white")                     
Canv.pack()
button1 = Button(self, text = "Quit", command = self.quit, anchor = W)