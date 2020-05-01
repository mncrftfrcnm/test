print("you are in dark room")
print("you see 4 doors")
pc = input("choose  1,2,3 or 4: ")
if pc == "3": 
    print("you can either")
    print("1)you can run away ")
    print("2)try to steal some gold")
    dc = input("choose 1 or 2:")
    if dc == "2":
        print("you lose")
    elif dc == "1":
        print("you win")
    else:
        print("you lose")


elif pc == "2":
    print("you lose")
elif pc == "4":
    print("you lose")
elif pc == "1":
    print("you lose")
    
else:
    print("you lose")