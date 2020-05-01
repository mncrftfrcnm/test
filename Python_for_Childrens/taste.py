from random import *
d = ""
k = ""
m = []
ytrtr = input("what word do you wanna:")
t = str(ytrtr)
tr = len(ytrtr)
print(t)
for x in range(tr):
    m.append(t[x])
a = m
# 
# 
c = randint(0,tr-1)
print(c)
m.remove(a[c])
d = m[0]
if len(m) > 2:
    k = m[1]

if len(m) == 2:
    k = m[1]
t = str(a)

print(t)














