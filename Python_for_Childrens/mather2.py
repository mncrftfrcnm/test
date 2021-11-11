from random import randint
from datetime import datetime
import time
zy = 0
massive = []
chek = True
tre = randint(10, 10)
massive = []

for setr in range(tre):
    massive.append(randint(0, 100))
print(massive)
massive2 = massive.copy()
for z in range(len(massive)):
    for x in range(len(massive)-z-1):
        y = x + 1
        print(x,y)

        if massive[x] < massive[y]:
            massive[x], massive[y] = massive[y], massive[x]
            chek += 1
        zy += 1
    if chek == 0:
        break
    chek = 0


print(massive)
print(zy)






zy = 0
massive = massive2.copy()
print(massive)
for z in range(len(massive)):
    for x in range(len(massive)-z-1):
        y = x + 1

        if massive[x] > massive[y]:
            massive[x], massive[y] = massive[y], massive[x]
            chek = False
        zy += 1
    if chek == True:
        break
    chek = 0


print(massive)
print(zy)
