import random
woman =["a queen","a pirate","a big rabbit"]
man = ["killer","robot","mario"] 
place = ["at the super market","on pluto"]
shewore =["bag", "fairy wings", "robot"]
hewore = ["purple suit", "a shark costume","Mario costume"]
womansay = ["who are you?","how many beans make five","why"]
mansay = ["beep boop","don't eat frogs","are you stupid?"]
werday = ["i am meiting", "errant nonsense", "eat frogs"]
do = ["woman and man fight to the end","woman and man got married"]
ere = True
while ere == True:
    print(random.choice(woman),"met",random.choice(man))
    print("she was wearing",random.choice(shewore))    
    print("he was wearing",random.choice(hewore))
    print("she said",random.choice(womansay))
    print("he said",random.choice(mansay))
    print("world said",random.choice(werday))
    rew = input("if you want to stop press F(else press enter):")
    if rew == "F":
        ere = False
        break
        

