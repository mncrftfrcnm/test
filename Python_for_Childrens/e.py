import time
aliens = 3
keyword = "ALieN"
il = True
yu = int(input("choose: 1)computer mode 2) easy mode:"))
print("quickly! aliens are invading the planet")
print("you need to activate defence platforms")
while il == True:
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
                print("their are ",aliens,"aliens")
                if aliens >= 1844674407370955:
                    print("you lose")
                    il = False
        else:
            print("bad")
            aliens = aliens**3
            print("their are ",aliens,"aliens")
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
            
            
            tav = input("please password:")
            if tav == keyword:
                print("cool")
                keyword = "Vova"
                tav = input("please password:")
                if tav == keyword:
                    print("YOU WIN")
                    il = False
                    break
                
                else:
                    aliens = aliens**2
                    print("bad")
                    print("their are ",aliens,"aliens")
                    if aliens >= 1844674407370955:
                        print("you lose")
                        il = False
                        break
                        il = False
            
            else:
                aliens = aliens**2
                print("bad")
                print("their are ",aliens,"aliens")
                if aliens >= 1844674407370955:
                    print("you lose")
                    il = False
                    break
                    il = False
        else:
            print("bad")
            print("their are ",aliens,"aliens")
        if aliens >= 1844674407370955:
            print("you lose")
            il = False
            
    else:
        print("bad")
        print("their are ",aliens,"aliens")
        if aliens >= 1844674407370955:
            print("you lose")
            il = False
