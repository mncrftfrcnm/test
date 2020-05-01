k = []
mn = int(input("how many elements do you wanna:"))
for x in range(mn):
    b = input("what element do you wanna:")
    k.append(b)
print(k)
mau = 0

v = 1
for x in range(mn):
    if int(k[x]) > int(k[mau]): 
       mau = x
iu = 0
ui = 1
print("max = "+k[mau])
lkj = 0
#iu = iu + 2
#ui = ui + 1

for x in range(mn):   
    lkj = lkj + int(k[x])
#    lkj = lkj + int(k[x+1])
print(lkj)
lkj = 1
for x in range(mn):   
    lkj = lkj * int(k[x])
#    lkj = lkj + int(k[x+1])
print(lkj)
















































