import pygame
import pyjoycon
from pyjoycon import *


class MyJoyCon(
        pyjoycon.GyroTrackingJoyCon,
        pyjoycon.ButtonEventJoyCon,
    ): pass

joycon_id = get_R_ids()
print (joycon_id)

pygame.init()
screen = pygame.display.set_mode((800, 600))

#yellow joycon right (140\6, 8199, '9458cbb41938')
#blue joycon left   

joycon = MyJoyCon(1406, 8199, 'e0f6b5c308dc')
joycon.get_status()
comm="x01"
subcomm=""
arg=""

#joycon._write_output_report(comm.encode(),subcomm.encode(),arg.encode())
#joycon._write_output_report(x00 01,0x00,0)
while 1:
    pygame.time.wait(int(1000/60))
    joycon._write_output_report(comm.encode(),subcomm.encode(),arg.encode())
 #   ...

 #   for event_type, status in joycon.events():
        #print(event_type, status)
        
 #       print("joycon color RGB:=",joycon.color_body)
        #joycon.set
  #  ...

    pygame.display.flip()

