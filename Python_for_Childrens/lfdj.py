from pyjoycon import GyroTrackingJoyCon, get_R_id
import time
import math
import pyjoycon
joycon_id = get_R_id()

joycon = pyjoycon.(1406, 8199, '9458cbb41938')
while True:
    if joycon:
        print('left')
    time.sleep(0.1)
    