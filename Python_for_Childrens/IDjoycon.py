# import pygame
# import pyjoycon
# from pyjoycon import *

# class MyJoyCon(
#         pyjoycon.GyroTrackingJoyCon,
#         pyjoycon.ButtonEventJoyCon,
#     ): pass
# joycon_id = get_R_ids()
# print (joycon_id)

# pygame.init()
# screen = pygame.display.set_mode((800, 600))

# #pink joycon right (1406, 8199, '9458cbb41938')
# #blue joycon left   

# joycon = MyJoyCon(1406, 8199, 'e0f6b5c308dc')
# joycon.get_status()
# print(joycon.color_body)

#joycon1 = MyJoyCon(1406, 8199, 'e0f6b5c308dc')
#joycon1.get_status()
#print("1406, 8199, 'e0f6b5c308dc'=",joycon1.color_body)

#JoyCon buttons press events
#while 1:
#    pygame.time.wait(int(1000/60))

    #for event_type, status in joycon.events():
    #    print("ButtonEventJoyCon:")
    #    print(event_type, status)
#    isstickbut = joycon.stick_r_btn
#    isstickmove=joycon.stick_r
#    if isstickmove[1] > 2000:
#        print('up')
#    elif isstickmove[1] < 2000:
#        print('down')
    # else:
    #     print('idfujfeg')
    # if isstickmove[0] > 2000:
    #     print('right')
    # elif isstickmove[0] < 2000:
    #     print("left")5
    # else:
    #     print('idfujfeg')
#    pygame.display.flip()
# ert = joycon.get_gyro_x()
from pyjoycon import GyroTrackingJoyCon, get_R_id
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(1406, 8199, '9458cbb41938')
while True:
  #forward  # print("joycon pointer:  ", joycon.pointer)
    # print("joycon rotation: ", joycon.rotation)

    direction = joycon.direction[2]
    if direction >=0:
        print('up')
    elif direction <= 0:
        print('down')
    
    time.sleep(0.9)
# import wexpect
# ssh = wexpect.spawn('ssh cisco@192.168.100.1')