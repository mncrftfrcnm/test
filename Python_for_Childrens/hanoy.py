s1 = [12,11,10,9,8,7,6,5,4,3,2,1]
s2 = []
s3 = []
s1 = []
for x in range(20):
    s1.append(x)
s1 = s1[::-1]
def replaser(stergen_otkuda_perenos,vspomogatelniy,kuda_perenos,colichestvo):
    if colichestvo == 1:
        kuda_perenos.append(stergen_otkuda_perenos.pop(-1))
    else:
        replaser(stergen_otkuda_perenos,kuda_perenos,vspomogatelniy,colichestvo-1)
        kuda_perenos.append(stergen_otkuda_perenos.pop(-1))
        replaser(vspomogatelniy,stergen_otkuda_perenos,kuda_perenos,colichestvo-1)

replaser(s1,s2,s3,len(s1))
print(s1, s2, s3)
