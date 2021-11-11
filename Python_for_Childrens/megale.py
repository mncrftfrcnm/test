from random import *
u = 50
#tre = input('how many elements do you wanna: ')
for x in range(3):
    
    te = randint(100,999)
    print(te,'=',te-u)
    u += 50
    
te = randint(100,999)
t = str(te)
tre = (t+" = ")
ert = int(input(tre))
if ert == te-u:
    print('you win')
if ert != te-u:
    print('you lose')

