from turtle import *
import time
t = input("first animal ( turtle or square or triangle or circle or classic or arrow): ")
tr = str(t)
ert = []
trt = len(t)
t2 = input("second animal( turtle or square or triangle or circle or classic or arrow ): ")
tr2 = str(t2)
trt2 = len(t2)
tre = []
for x in range(trt-2):
    tre.append(tr[x])
for x in range(trt2-1):
    ert.append(tr2[x])
tyu = ""
rty = []
rty.append(tre)
rty.append(ert)
for x in rty:
    tyu = tyu + str(x)
print(tyu)
screen = Screen()
t3 = Turtle()
t3.shape(t)
t4 = Turtle()
t4.shape(t2)
t4.forward(-5)
def f():
    t3.forward(10)
    time.sleep(0.01)
    t4.forward(10)
listen()
screen.onkey(f,"Right")
fjklfas = input("cool")