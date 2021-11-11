from pyjoycon import GyroTrackingJoyCon, get_R_id
import pyjoycon
from random import *
import time
from math import *
from turtle import *
t = Turtle()
joycon_id = get_R_id()
# joycon = GyroTrackingJoyCon(1406, 8199, '9458cbb41938')
joy = pyjoycon.PythonicJoyCon(1406, 8199, '9458cbb41938')
# joycon2 = GyroTrackingJoyCon(1406, 8198, '9458cbb3aeaa')
#
# joycon3 = pyjoycon.ButtonEventJoyCon(1406, 8199, '9458cbb41938')
butka = 1
spisok = []
# x = joycon.get_gyro_x()
# z = joycon.get_gyro_z()
for num in range(10):
    print(end='  ')
    time.sleep(1)

while True:
    # if joycon.pointer != None:
    #     if joycon.pointer + 0.000001:
    #         print('up')
    # if joycon.pointer == None:

        
    #     print('down')
    # x = 1
    # for x in range(1000):
    #     x = randint(1,20)
    #     joycon.set_player_lamp_flashing(x)
    #     joycon2.set_player_lamp_flashing(x)
    #     time.sleep(0.5)

    # print(joycon.get_gyro_x())
    # print(joycon.get_gyro_y())
    # print(joycon.get_gyro_y())
    # time.sleep(1)
    # for event_type, status in joycon3.events():
    #     if status == 1:
            
    #         if event_type == 'b':
    #             butka -= 1
    #         if event_type == 'x':
    #             butka += 1
    # joycon.set_player_lamp_flashing(butka)
    # for event_type, status in joycon3.events():
    #     if status == 1:
            
    #         if event_type == 'r':
    #             string = str(joycon.get_gyro_x())+','+str(joycon.get_gyro_z())
    #             spisok.append(string)
                
                
    #             with open('label_territory.txt','w') as f:
    #                 f.write(str(spisok))
    # if joycon.get_gyro_x() > x+1000 or joycon.get_gyro_x() < x-1000:
    #     x = joycon.get_gyro_x()
    #     print('x=',x)
    # elif joycon.get_gyro_z() > z+1000 or joycon.get_gyro_z() < z-1000:
    #     z = joycon.get_gyro_z()
    #     print('z=',z))
    print(str(joy.disconnect_device()))


