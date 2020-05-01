import random
nur = random.randint(1,10)
go = int(input("choose number from 1 to 10: "))
if go == nur:
    print("you win")
while go != nur:
    if go < nur:
        print("too low")
    else:
        print ("too high")
    go = int(input("try again:"))
    if go == nur:
        print("you win")