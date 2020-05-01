import threading
from threading import Timer
import time

def doSomething():
    print (time.time())

OurTimer=Timer(5.0, doSomething)
OurTimer.start()
