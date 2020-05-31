from turtle import *
t = input("first animal: ")
tr = str(t)
ert = []
trt = len(t)
t2 = input("second animal: ")
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