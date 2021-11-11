from pyjoycon import *
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(1406, 8199, '9458cbb41938')


while 1:
    if joycon.gyro[0][0] >= 12:
        print('right')
    time.sleep(1)