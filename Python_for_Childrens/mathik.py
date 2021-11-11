import random
import threading
import time
score = 0
score2 = 0
n = 0
dif = 10
symb = '+'
print(2/10)
time1 = 0
time2 = 0
class beeper(threading.Thread):
    def run(self):
        global time1

        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            time1+=1
                
class beeper2(threading.Thread):
    def run(self):
        global time2

        self.keeprunning = True
        while self.keeprunning:
            time.sleep(1)
            time2+=1


beep  = beeper()
beep.start()
while n == 0:
    for p in range(10):
        x = random.randint(1,dif)
        z = random.randint(1,dif)
        y = random.randint(1,dif)
        ran = random.randint(0,3)
        if ran == 0:
            an = x+y
            symb = '+'
        if ran == 1 and dif >=3:
            an = x-y
            symb = '-'
        if ran == 2 and dif >=6:
            an = x*y
            symb = '*'
        if ran == 3 and dif >=8:
            x = z*y
            an = x/y
            symb = '/'

        tre = float(input(f'''{x}{symb}{y} = '''))
        if tre == an:
            print('right')
            score += 1
        else:
            print('your score is {}'.format(score))
            n=1
            break
    if n == 1:
        break
    dif += 1


beep.keeprunning = False
beep  = beeper2()
beep.start()
n = 0
dif = 10
symb = '+'
while n == 0:
    for p in range(10):
        z = random.randint(1,dif)
        y = random.randint(1,dif)
        x = random.randint(1,dif)
        ran = random.randint(0,3)
        if ran == 0:
            an = x+y
            symb = '+'
        if ran == 1 and dif >=3:
            an = x-y
            symb = '-'
        if ran == 2 and dif >=6:
            an = x*y
            symb = '*'
        if ran == 3 and dif >=8:
            x = z*y
            an = x/y
            symb = '/'

        tre = float(input(f'''{x}{symb}{y} = '''))
        if tre == an:
            print('right')
            score2 += 1
        else:
            print('your score is {}'.format(score2))
            n=1
            break
    if n == 1:
        break
    dif += 1
beep.keeprunning = False
if score > score2:
    print('p1 wins.')
if score < score2:
    print('p2 wins.')
if score == score2:
    if time1 < time2:

        print('p1')
    if time1 >time2:
    
        print('p2')
    if time1 == time2:
        
        print('draw')
