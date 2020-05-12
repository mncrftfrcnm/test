import random
ert = random.randint(0,10)

uy = True
while uy == True:
    tre = int(input("choose number from 0 to 10:"))
    if ert < tre:
        print("too high")
    
    if ert == tre:
        print("cool")
        uy = False
        break
    if ert > tre:
        print("too small")
    































