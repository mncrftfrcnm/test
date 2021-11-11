import getpass
import sys
while True:
    getpasser = getpass.ge
    125690.tpass()
    with open('passwords.txt') as f:
        if not(getpasser) in f.read():
            with open('passwords.txt','a',encoding='utf-32') as f2:
                f2.write(getpasser+',')
                print('it is good password. Well done!')
                break
        else:
            print('write your password again, please.')
