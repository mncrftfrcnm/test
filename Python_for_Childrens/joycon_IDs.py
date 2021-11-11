import pygame
import pyjoycon
from pyjoycon import *

class MyJoyCon(
        pyjoycon.GyroTrackingJoyCon,
        pyjoycon.ButtonEventJoyCon,
    ): pass

joycon_id = get_L_ids()
joycon_id2 = get_R_ids()
print (joycon_id,joycon_id2)

#L violet
#(1406, 8198, '9458cbb3aeaa'), (1406, 8198, 'e0f6b5c00b14')
#R yellow
#(1406, 8199, '9458cbb41938'), (1406, 8199, 'e0f6b5c308dc')