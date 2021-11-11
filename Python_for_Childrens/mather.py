from random import randint
massive = []
tre = randint(5, 5)
massive = []
for setr in range(tre):
    massive.append(randint(0, 900))
print(massive)
massive2 = []
for x in range(1,len(massive)):
    for y in range(x):
        
        if massive[x] < massive[y]:
            massive[y], massive[x] = massive[x], massive[y]   
        elif massive[x] > massive[y]:
            break
            
print(massive)
