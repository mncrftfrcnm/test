import tkinter
import tkinter.messagebox
import time
import random
import winsound
from winsound import *
import threading
from threading import Timer

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

class beeper(threading.Thread):
    def run(self):
        self.keeprunning = True
        while self.keeprunning:
            first = randint(37,32000)
            second = randint(100,1000)
            PlaySound("C:\windows\media\Ring02.wav",False)
            

while True:
    jjj = int(input("how many time do you want to sleep:"))
    for x in range(jjj):
        print(jjj-x)
        
        time.sleep(1)
    PlaySound("C:\windows\media\Ring04.wav",False)
    PlaySound("C:\windows\media\Ring01.wav",False)
    PlaySound("C:\windows\media\Ring02.wav",False)
    PlaySound("C:\windows\media\Ring03.wav",False)
    PlaySound("C:\windows\media\Ring05.wav",False)
    PlaySound("C:\windows\media\Ring06.wav",False)
    PlaySound("C:\windows\media\Ring07.wav",False)
    PlaySound("C:\windows\media\Ring08.wav",False) 
    PlaySound("C:\windows\media\Ring09.wav",False)
    PlaySound("C:\windows\media\Ring10.wav",False)
    PlaySound("C:\windows\media\Alarm01.wav",False)
    PlaySound("C:\windows\media\Alarm02.wav",False)
    PlaySound("C:\windows\media\Alarm03.wav",False)
    PlaySound("C:\windows\media\Alarm04.wav",False)
    PlaySound("C:\windows\media\Alarm05.wav",False)
    PlaySound("C:\windows\media\Alarm06.wav",False)
    PlaySound("C:\windows\media\Alarm07.wav",False)
    PlaySound("C:\windows\media\Alarm08.wav",False)
    PlaySound("C:\windows\media\Alarm10.wav",False)
    PlaySound("C:\windows\media\Alarm09.wav",False)
