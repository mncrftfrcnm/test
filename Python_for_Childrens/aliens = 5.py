aliens = 5
password = "ALIENS"
print("quickly! aliens are invading the planet")
print("you need to activate defence platforms")
print("hope you know the password")
print()
print("-----------------------------------------------------------------------------------------------")
print("                             WELCOME TO THE DEFENCE NETWORK"                                    )
print("-----------------------------------------------------------------------------------------------")
print()
guess = input("please enter the password: ").upper()
if guess == password:
    print("YOU WIN")
while guess != password:
    aliens = aliens**2
    print("there are", aliens, "aliens, try again")
#    if aliens > 74000000000:
#        break
    print("password hint things attack you now")
    guess = input("please enter the password: ").upper()
    if aliens > 74000000000:
        print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO YOU LOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    if guess == password:
        print("YOU WIN")











