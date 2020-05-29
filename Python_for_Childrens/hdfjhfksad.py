fn = 'fgfg.txt'
while True:
    with open(fn,'r+') as filebject:
        fg = filebject.read()
        trtrt = input('what do you want to write: ')
        filebject.write(trtrt)
        
        print(fg)