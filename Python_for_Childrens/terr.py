import random
place =["earth","pluto"]
man = ["olga","olya"]
rt = ["designer","grandma"]
w = True
while w == True:
    print(random.choice(man))
    print("her planet is", random.choice(place))
    print("she is",random.choice(rt))
    print("she is very cool",random.choice(rt))
    r = input("if you want to stop game print F(else print enter):")
    if r == "F":
        w = False
        break
