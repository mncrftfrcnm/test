
ad = {"we":"vorag","come":"thang", "in":"zon","peace":"argh", "helo":"kodar","can":"znak","i":"az","borrow":"liftit","some":"zum"}
eg = input("what do you want to translate:")
ew = eg.lower().split()
aw = []
for w in ew:
    if w in ad:
        aw.append(ad[w])
    else:
        aw.append(w)
    print("in alien say ","".join(aw))



