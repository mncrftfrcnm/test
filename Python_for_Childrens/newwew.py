fn = 'fgfg.txt'
with open(fn,'r+') as filebject:
    fg = filebject.read()
    rret = input("what do you want to write: ")
    filebject.write(rret)
    
#    print(fg)
