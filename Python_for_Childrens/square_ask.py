from math import sqrt
eq = input('Enter a quadratic equation type ax2 + bx + c: ')
ytr = eq.split(' ')
print()
a = ytr[0].replace('x2', '')
if a == '':
    a = '1'
print(a)
n = ytr[1]
print(n)
b = ytr[2].replace('x', '')
if b == '':
    b = '1'
print(b)
n2 = ytr[3]
print(n2)
c = ytr[4]
print(c)
d = int(b)**2 - 4*(int(a))*(int(n2+c))
print(f'D: {d}')
if d < 0:
    print('There are no actual answers, because the discriminant is negative.')
else:
    try:
        x_1 = (-1*(int(n+b)) + sqrt(d))/(2*int(a)) 
    except ValueError:
        x_1 = (-1*(int(n+b)) - sqrt(d*-1))/(2*int(a))
    
    print(f'x_1: {x_1}')
    if d != 0:
        try:
            x_2 = (-1*(int(n+b)) - sqrt(d))/(2*int(a))
        except ValueError:
            x_2 = (-1*(int(n+b)) + sqrt(d*-1))/(2*int(a))
        print(f'x_2: {x_2}')
