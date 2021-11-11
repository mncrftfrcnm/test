import chardet

with open('passwords.txt',encoding='utf-8') as f:
    with open('passwords.txt','w',encoding='utf-8') as f2:
        f2.write(str(f.read().encode('utf-32')))
