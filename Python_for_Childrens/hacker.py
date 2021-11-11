import getpass
tre = getpass.getpass()
methodik = 0
spisok = []
for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for e in range(9):
                    for f in range(9):
                        a = str(a)
                        b = str(b)
                        c = str(c)
                        d = str(d)
                        e = str(e)
                        f = str(f)
                        print(a+b+c+d+e+f)
                        if a+b+c+d+e+f == str(tre):
                            print(a+b+c+d+e+f)
                            break
                        methodik+=1
                        