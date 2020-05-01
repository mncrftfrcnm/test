ytu = input("a)new recept b)read old recept:")
f = open('file.txt', 'w')
if ytu == "a":
    f = open('file.txt', 'x')
    print(f.read())
else:
    trrt = input("please print name:")
    f = open('file.txt', 'r')
    print(f.read())