
from tkinter import *
from random import *
import tkinter.messagebox
import time
import random
import winsound
from winsound import PlaySound,SND_ASYNC,Beep
import threading
from threading import Timer,Thread
from time import sleep
wait_seconds = 1
WinWidth=750
w = tkinter.Tk()
class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            
            w = tkinter.Tk()
            #Canv = Canvas(w, width=300, height=500, bg="white")                     
            #Canv.pack() 
            w.mainloop()
            

    
            
            
            
            
            
            
beep  = beeper()
beep.start()
