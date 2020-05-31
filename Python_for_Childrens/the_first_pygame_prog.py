
def dkl(fo):
    try:
        with open(fo) as fn:
            c = fn.read()
    except FileNotFoundError:
        pass
    else:
        w = c.split()
        nm = len(w)
        print(nm)
fw = ['fgfg.txt','snow2.txt','snow22.txt']
for f in fw:
    dkl(f)