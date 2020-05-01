from random import *
from words import mass
sco = 0
y = []
d = ""
k = ""
kb = ""
jrfjg = []
ytrtr = mass[randint(0,len(mass)-1)]
t = str(ytrtr)
d = ""
k = ""
m = []
t = str(ytrtr)
tr = len(ytrtr)
for x in range(tr):
    m.append(t[x])
a = m
i = tr
#         print(a)аров
while True:

    ytrtr = mass[randint(0,len(mass)-1)]
    d = ""
    k = ""
    m = []
    t = str(ytrtr)
    tr = len(ytrtr)
    for x in range(tr):
        m.append(t[x])
    a = m
    i = tr

    for x in range(i):
        kb = ""
        for x in range(tr):    
            c = randint(0,len(a)-1)
            kb = kb + a[c]
            y.append(a[c])
            a.remove(a[c])
        for x in range(tr):
            a.append(t[x])
        else:
            i  = i + 1
    if kb != ytrtr:    
        print(kb)

    

    ryt = input("what word is it:")
    if ytrtr == ryt:
        sco = sco + 1
        print("Your score is", sco)
    else:
        print("You lose. Right word was: "+ytrtr)
        print("Your score is", sco)
        break