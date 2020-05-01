import time
import random
y = 100
jmcs = 5
yp = True
oj = 0
p = 0
r = 0
re = 2
uypow = 0
wop = 0 
level = 0
print("if your moneys = 0 or < 0 you lose")
yty = 0
ghuo = 0
while yp == True:
    t = random.randint(0,3+ghuo)
    if t == 3:
        print("you have got mugged !")
        y = y -10
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")        
    gh = int(input("what do you wanna:1)see your moneys 2)build house(+1 money and +50 money for another house), 50 moneys 3)do vidio game(*2 all your moneys and for another vidio games *2 ),100 4)insurance 5) deffense,30 6)shop,30 7)level up,10 8)upgread,10,(level 10)(the house + 10 muneys,  the level up + 5): "))
    if gh == 5:
        uypow = 30
        uypow = uypow - wop
        y = y -uypow
        ghuo = ghuo +3
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                yp = False
                break
    if gh == 2:
        uypow = 50
        uypow = uypow - wop
        y = y -uypow
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                yp = False
                break










        p = p + 1
        y = y + p + r +oj
        r = r + 50
    if gh == 3:
        y = y-100
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                break
        y = y * re
        re = re * 2
    if gh == 1:
        print(y)
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                break
    if gh == 4:
        nbv = int(input("how many moneys do you wanna:"))
        yty = yty + nbv
        y = y - nbv
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                break
    if gh == 6:
        y = y-30
        for x in range(3):
            jhkh = random.randint(10,100)
            yuy = random.randint(1,2)
            if yuy == 1:
                print("hooray you have some maneys")
                y = y + jhkh
            else:
                print("hooray you have deffense")
                ghuo = ghuo+3

    if gh == 7:
        level =level + jmcs
        uypow = 10
        uypow = uypow - wop
        y = y - uypow
#        y = y - v
        if y == 0 or y < 0:
            y = y + yty
            if y == 0 or y < 0:
                print("you lose")
                yp = False
                break

    if gh == 8:

        if y == 0 or y < 0 or level < 0 or level == 0:
            y = y + yty
            yty = yty - y
            level = level + yty
            if y == 0 or y < 0 or level < 0 or level == 0:
                print("you lose")
                yp = False
                break
        level =level - 10
        jmcs = jmcs + 5
        oj = oj + 10
        uypow = 10
        uypow = uypow - wop
        y = y - uypow
#        y = y - v
        
































