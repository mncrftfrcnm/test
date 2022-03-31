from random import *
spisok = ['buter', 'tea', 'pankeiks', 'milk', 'cucumber', 'bulka', 'eggs', 'blini', 'podogretyi buter', 'grenki', 'kasha mannaya' ,'kasha ovsyanaya', 'yaishnica', 'omlet']
tre = input('mum: ')
tre2 = input('Vov: ')
if tre == '' and tre2 == '':
    print(choice(spisok))
elif tre != tre2:
    print(randint(0,1))
elif tre == tre2:
    print(tre)
elif tre == '':
    print(tre2)
elif tre2 == '':
    print(tre)
