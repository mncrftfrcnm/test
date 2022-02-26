for x in range(105):
    y = (105-x)/5
    if x/2 != int(x/2):
        if y/2 == int(y/2):
            print(x, y, x+y*5)
passer = 0
for k in range(100):
    try:
        
        for g in range(100):
            y = g
            for p in range(100):
                x = p
                if x/3 == int(x/3):
                    if (x+y)/k == k:
                        print(k, x, y)
                        passer = 1            
                if passer == 1:
                    break
            if passer == 1:
        
                break
    except ZeroDivisionError:
        pass
    if passer == 0:
        print('error')
    passer = 0