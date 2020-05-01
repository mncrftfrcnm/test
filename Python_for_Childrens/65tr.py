ab = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
se = input("please enter a message to encrypt: ")
sa = int(input("please enter a whole number from 1-25 to be your key: "))
es = ""
for eryb in se:
    p = ab.find(eryb)
    np = p + sa
    es = es + ab[np]
print("your message is ",es)












