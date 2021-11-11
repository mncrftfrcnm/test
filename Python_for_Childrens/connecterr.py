# wifi (2books)
# import mysql.connector

# cnx = mysql.connector.connect(user='scott', password='password',
#                               host='127.0.0.1',
#                               database='employees')
# cnx.close()
# from mysql.connector import (connection)

# cnx = connection.MySQLConnection(user='scott', password='password',
#                                  host='127.0.0.1',
#                                  database='employees')
# cnx.close()
# import mysql.connector
# from mysql.connector import errorcode

# try:
#   cnx = mysql.connector.connect(user='scott',
#                                 database='employ')
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cnx.close()
# import subprocess

# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
# results = results.decode("ascii")
# results = results.replace("\r","")
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)
# import mysql.connector

# config = {
#   'user': 'scott',
#   'password': 'password',
#   'host': '127.0.0.1',
#   'database': 'employees',
#   'raise_on_warnings': True
# }

# cnx = mysql.connector.connect(**config)

# cnx.close()
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
# import os
# os.name.find('MinePfi')
# os.listdir(path=".")
#turtle
# t = Turtle()
# t.pu()
# t.goto(x,y)
# x,y = t.pos()

#pygame
#     def run_game2():
#         global ch,dobollet,t,bulets,t2
#         forrand = 1000
#         pygame.init()
#         pygame.joystick.init()
#         joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
#         print(len(joysticks))
#         for joystick in joysticks:
#             joystick.init()
#         ai_settings =Settings()
#         screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#         pygame.display.set_caption('Alien Invasion')
#         ship = Ship(ai_settings,screen)
#         bullets = Group()
#         aliens = Group()
#         ships = Group()
#         ships.add(ship)
#         blocks = Group()
#another commands
#help()

#try:

#if ...:

#import

#print()

#an another libraris
#time:
#sleep()

#timeht:
#get time

#sys:
#exit()

#tkinter

# import googlesearch
# googlesearch.search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0)
# query : query string that we want to search for.
# tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
# lang : lang stands for language.
# num : Number of results we want.
# start : First result to retrieve.
# stop : Last result to retrieve. Use None to keep searching forever.
# pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
# Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever
# try: 
#     from googlesearch import search 
# except ImportError:  
#     print("No module named 'google' found") 
  
# # to search 
# query = "mario"
  
# for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
#     print(j)

#contrls
#+h
#+c
#+v
#+y
#+z