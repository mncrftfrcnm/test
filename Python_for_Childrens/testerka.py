from pyjoycon import *
import pyjoycon
joycon_id = get_R_ids()
print(joycon_id)
class MyJoyCon(
        pyjoycon.GyroTrackingJoyCon,
        pyjoycon.ButtonEventJoyCon,
    ): pass
print(joycon_id[0])
ghtipo = str(joycon_id[0]).split(', ')
ghtipo[0] = int(ghtipo[0].replace('(', ''))
ghtipo[2] = ghtipo[2].replace(')', '')
joycon = MyJoyCon(ghtipo[0], int(ghtipo[1]), ghtipo[2])
joycon.get_status()
joycon_id = get_L_ids()
print(joycon_id[0])
ghtipo = str(joycon_id[0]).split(', ')
ghtipo[0] = int(ghtipo[0].replace('(', ''))
ghtipo[2] = ghtipo[2].replace(')', '')
joycon = MyJoyCon(ghtipo[0], int(ghtipo[1]), ghtipo[2])
joycon.get_status()
