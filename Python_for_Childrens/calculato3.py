import math
import time
wert = True
aliens = 3
il = True
yu = int(input("choose: 1)computer mode 2) easy mode:"))
print("quickly! aliens are invading the planet")
print("you need to activate defence platforms")
while il == True:
    passd = "ALieN"
    if yu == int(2):
        tav = int(input("please enter the anwer:45 + 12 = (print only answer)(print only number(s)):"))

        if tav == int(57):
            print("good")
            tav = int(input("please enter the anwer 2**3 = (print only answer)(print only number(S)):"))

            if tav == int(8):
                print("you win")
                il = False
                break
            else:
                aliens = aliens**2
                print("bad")
                print("theire are ",aliens,"aliens")
                if aliens >= 1844674407370955:
                    print("you lose")
                    il = False
                    break    
        else:
            print("bad")
            aliens = aliens**3
            print("theire are ",aliens,"aliens")
            if aliens >= 1844674407370955:
                print("you lose")
                il = False
                break
    if yu == int(1):
        tav = int(input("please enter the anwer:450/2 = (print only answer)(print only number(s)):"))

    if tav == int(225):
        print("good")
        tav = int(input("please enter the anwer 2**64 = (print only answer)(print only number(S)):"))

        if tav == int(18446744073709551616):
            print("cool")
            tav = input("password:")
            if tav == passd:
                passd = "VoDa"
                tav =  input("second password:")
                if tav == passd:
                    print("you win")
                    il = False
                    wert = False
                    break
                
                else:
                    aliens = aliens**2
                    print("bad")
                    print("theyre are ",aliens,"aliens")


                    if aliens >= 1844674407370955:
                        print("you lose")
                        il = False

                        break

            else:
                aliens = aliens**2
                print("bad")
                print("theire are ",aliens,"aliens")


                if aliens >= 1844674407370955:
                    print("you lose")
                    il = False

                    break
                    
        else:
            aliens = aliens**2
            print("bad")
            print("theire are ",aliens,"aliens")

        if aliens >= 1844674407370955:
            print("you lose")
            il = False
            break
            
    else:
        print("bad")
        print("theire are ",aliens,"aliens")
        if aliens >= 1844674407370955:
            print("you lose")
            il = False
            break
while wert == False:
    trar = input("choose: 1)+ 2)/ 3)* 4)- 5)** 6)sqrt 7)modf 8)log1p 9)hypot 10)number pi 11)number e(if you want to stop game print False):")
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
    if trar == "False":
        wert = True
        break