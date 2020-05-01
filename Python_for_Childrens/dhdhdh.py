import random
woman =["a queen","a pirate","a big rabbit"]
man = ["killer","robot","mario"] 
place = ["at the super market","on pluto"]
shewore =["bag", "fairy wings", "robot"]
hewore = ["purple suit", "a shark costume","Mario costume"]
womansay = ["who are you?","how many beans make five","why"]
masay = ["beep boop","don't eat frogs","are you stupid"]
ws = ["eat frogs", "hi is stupid", "she is stupid"]
do = [" fight to the end","woman and man got married", "run away"]
ret = ["happy", "weard", "ill"]
w = True
while w == True:
    print(random.choice(woman),"met",random.choice(man), random.choice(place))
    print("she was wearing",random.choice(shewore))
    print("he was wearing",random.choice(hewore))
    print("she said",random.choice(womansay))
    print("he said",random.choice(masay))
    print("world said",random.choice(ws))
    print("they are", random.choice(do))
    print("they are", random.choice(ret))
    rt = input("if you want to stop game print F(else print enter):")
    if rt == "F":
        w = False
        break