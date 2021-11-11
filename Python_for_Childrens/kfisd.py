from pyjoycon import GyroTrackingJoyCon, get_R_id
import time

joycon_id = get_R_id()
joycon = GyroTrackingJoyCon(1406, 8198, 'e0f6b5c00b14')


while 2:
    print("joycon pointer:  ", joycon.pointer)
    print("joycon rotation: ", joycon.rotation)
    print("joycon direction:", joycon.direction)
    print()
    time.sleep(2)