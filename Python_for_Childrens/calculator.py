import math
wert = False
while wert == False:
    trar = input("choose: 1)+ 2)/ 3)* 4)- 5)** 6)sqrt 7)modf 8)log1p 9)hypot 10)number pi 11)number e 12)frexp 13)tan 14)fmod 15)gamma 16)lgamma 17)copysign 18)factorial 19)atan2 20)atan 21)copysign 22)exp 23)fabs 24)frexp 25)pow(if you want to stop game print False):")
    if trar == "1":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"+", tre, "=", ert +  tre)
    if trar == "2":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"/", tre, "=", ert / tre)
    if trar == "3":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"*", tre, "=", ert * tre)
    if trar == "4":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"-", tre, "=", ert - tre)









    if trar == "5":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        print(ert,"**", tre, "=", ert**tre)

    if trar == "6":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = ert ** (1./tre)
        print(ert,"**", tre, "=", retw) 
    
    if trar == "7":
        ert = int(input("choose number:"))
        retw = math.modf(ert)
        print(retw)

    if trar == "8":
        ert = int(input("choose number:"))
        retw = math.log1p(ert)
        print(retw)

    if trar == "9":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.hypot(ert,tre)
        print(retw)

    if trar == "10":
        retw = math.pi
        print(retw)
    
    if trar == "11":
        retw = math.e
        print(retw)
    if trar == "12":
        ert = int(input("choose number:"))
        retw = math.frexp(ert)
        print(retw)
    if trar == "13":
        ert = int(input("choose number:"))
        retw = math.tan(ert)
        print(retw)

    if trar == "14":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.fmod(ert,tre)
        print(retw)

    if trar == "15":
        ert = int(input("choose number:"))
        retw = math.gamma(ert)
        print(retw)

    if trar == "16":
        ert = int(input("choose number:"))
        retw = math.lgamma(ert)
        print(retw)
    if trar == "17":
        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.copysign(ert,tre)
        print(retw)

    if trar == "18":
        ert = int(input("choose number:"))
        retw = math.factorial(ert)

        print(retw)
    if trar == "19":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.atan2(ert,tre)
        
        
        print(retw)

    if trar == "20":
        ert = int(input("choose number:"))
        retw = math.atan(ert)

    if trar == "21":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.copysign(ert,tre)
        print(retw)

    if trar == "22":

        tre = int(input("choose number:"))
        retw = math.exp(tre)
        print(retw)

    if trar == "23":

        tre = int(input("choose number:"))
        retw = math.fabs(tre)
        print(retw)

    if trar == "24":

        tre = int(input("choose number:"))
        retw = math.frexp(tre)
        print(retw)

    if trar == "25":

        ert = int(input("choose first number:"))
        tre = int(input("choose second number:"))
        retw = math.pow(ert,tre)
        print(retw)


    if trar == "26":

        
    if trar == "False":
        wert = True
        break
    