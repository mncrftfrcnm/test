import getpass
import sys
tre = getpass.getpass()
methodik = 0
spisok = []
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        a = str(a)
                        b = str(b)
                        c = str(c)
                        d = str(d)
                        e = str(e)
                        f = str(f)
                        #print(a+b+c+d+e+f,tre)
                        if a+b+c+d+e+f == str(tre):
                            print(a+b+c+d+e+f)
                            sys.exit()
                            
                        methodik+=1
                        