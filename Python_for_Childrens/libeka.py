import vpython
from vpython import *
import random
import pygame
import dolibe_vp
import pygame.mixer
from pyjoycon import *
import pyjoycon
from pyjoycon import GyroTrackingJoyCon, get_R_id
import time
x = 0
joycon_id = get_R_id()
joygyr = GyroTrackingJoyCon(*joycon_id)
joycon_id = get_R_ids()
######################(joycon_id)
ts = []
side = 10.0
thk = 2.3
s2 = 2*side - thk
s3 = 2*side + thk
blocks = []
xs = []
ys = []
zs = []
buls = []
xb = []
yc = []
a = 0
zd = []
wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3), texture=textures.wood)
blocks.append(wallR)
xs.append(side)
ys.append(0)
zs.append(0)

wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3), texture=textures.gravel)
blocks.append(wallL)
xs.append(-side)
ys.append(0)
zs.append(0)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3), texture=textures.rug)
blocks.append(wallB)
xs.append(0)
ys.append(-side)
zs.append(0)

wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3), texture=textures.stucco)
blocks.append(wallT)
xs.append(0)
ys.append(side)
zs.append(0)

wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), texture=textures.rock)
blocks.append(wallBK)
xs.append(0)
ys.append(0)
zs.append(-side)
wallBKC = box(pos=vector(0, 0, side), size=vector(s2, s2, thk), texture=textures.flower)
blocks.append(wallBKC)
xs.append(0)
ys.append(0)
zs.append(side)
for itm in range(len(blocks)):
    zs[itm] -= 10



    blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
class MyJoyCon(
        pyjoycon.GyroTrackingJoyCon,
        pyjoycon.ButtonEventJoyCon,
    ): pass
######################(joycon_id[0])
ghtipo = str(joycon_id[0]).split(', ')
ghtipo[0] = int(ghtipo[0].replace('(', ''))
ghtipo[2] = ghtipo[2].replace(')', '')
joycon = MyJoyCon(ghtipo[0], int(ghtipo[1]), ghtipo[2])
joycon.get_status()
joycon_id = get_L_ids()
######################(joycon_id[0])
ghtipo = str(joycon_id[0]).split(', ')
ghtipo[0] = int(ghtipo[0].replace('(', ''))
ghtipo[2] = ghtipo[2].replace(')', '')
joycon2 = MyJoyCon(ghtipo[0], int(ghtipo[1]), ghtipo[2])
joycon2.get_status()

pygame.init()
scene.width = scene.height = 1000
scene.background = color.gray(0.9)
scene.range = 2.2

scene.caption = "Click to pick an object and make it red."
scene.append_to_caption("\nNote picking of individual curve segments.")
drone = box(pos=vector(0,0,0), color=color.cyan, opacity=1, size = vector(0.1, 0.1, 0.1))
# for x in range(5):
#     for y in range(5):
#         for z in range(5):
#             gh = random.randint(0,0)
#             if gh == 0:
#                 xs.append(x)
#                 ys.append(y)
#                 zs.append(z)
#                 blocks.append(sphere(pos=vector(x*10,y*10,z*10), color=color.cyan, size=.4*vector(3,3,3)))
#             if gh == 1:
#                 cone(pos=vector(x,y,z), axis=vector(2,2,-.2), color=color.blue, size=vector(2,2,2))            
#             if gh == 2:
#                 sphere(pos=vector(x, y, z), color=color.white, size=.4*vector(2,2,2)) 

gh = 1
ga = 1
gr = 0.05
rgear = 0.7
tgear = ga/10 # gear thickness
support = extrusion(pos=vector(7,gh/2,10), path=[vector(0,0,0), vector(0,gh,0), vector(0,gh,ga), vector(0,0,ga)],
            shape=shapes.circle(radius=gr), color=vector(1,.7,0))
support.clone(pos=vector(7+2*rgear,gh/2,10))
gear1 = extrusion(pos=support.pos+vector(0,gh/2,0), path=[vector(0,0,-tgear/2), vector(0,0,tgear/2)],
            shape=shapes.gear(radius=rgear), color=color.gray(0.85), texture=textures.metal)

gear1.rotate(angle=-0.4*2*pi/20, axis=vector(0,0,1)) # default i           
v0 = vertex(pos=vector(-.5,1.2,0), color=color.green)
v1 = vertex(pos=vector(1,1.2,0), color=color.red)
v2 = vertex(pos=vector(1,2,0), color=color.blue)
v3 = vertex(pos=vector(-.5,2,0), color=color.yellow)
dirka = drone.pos
gear1.pos = drone.pos

dist = distant_light(direction=dirka, color=color.yellow) 
v = arrow(pos=vector(-1,-1.3,5), color=color.purple)
# t1 = text(text='YOU ARE THE BEST PARENTS!', pos=vector(0,0,0), 
#           color=color.yellow)
lasthit = None
lastpick = None
lastcolor = None
a = 0
b = 0
c = 0
si = 1
def getevent():
    global lasthit, lastpick, lastcolor

    if lasthit != None:

        if lastpick != None: lasthit.modify(lastpick, color=lastcolor)
        else: lasthit.color = vector(lastcolor)
        lasthit = lastpick = None
    
    hit = scene.mouse.pick
    if hit != None:
        
        lasthit = hit
        lastpick = None

        if isinstance(hit, curve):  # pick individual point of curve
            lastpick = hit.segment
            lastcolor = hit.point(lastpick)['color']
            hit.modify(lastpick, color=color.red)
        elif isinstance(hit, quad):
            lasthit = hit.v0
            lastcolor = vector(lasthit.color) # make a copy
            lasthit.color = color.red
        else:
            lastcolor = vector(hit.color) # make a copy
            hit.color = color.red

scene.bind("mousedown", getevent)
while True:
        a+=10
        b+=1
        si += 0.000000000000000000000000001

        x += 0.01
        time.sleep(0)

        isstickmove=joycon.stick_r
        # if isstickmove[1] > 2000:
            
        #     ship.rect.x += 3
        #     if pygame.sprite.spritecollideany(ship,blocks):
        #         ship.rect.x -= 3
        #     t = 2
        #     #('up')
        # elif isstickmove[1] < 1000:
        #     #ship.y += 3
        #     #('down')
        #     ship.rect.x -= 3
        #     if pygame.sprite.spritecollideany(ship,blocks):
        #         ship.rect.x += 3
        #     t=3
        
        # elif isstickmove[0] > 3000:
        #     #ship.x += 3
        #     #('r')
        #     ship.rect.y += 3
        #     if pygame.sprite.spritecollideany(ship,blocks):
        #         ship.rect.y -= 3
        #     t=1
        # elif isstickmove[0] < 1000:
        #     #ship.x -= 3
        #     #('l')
        #     t=0
        #     ship.rect.y -= 3
        #     if pygame.sprite.spritecollideany(ship,blocks):
        #         ship.rect.y += 3

        # isstickbut = joycon2.stick_l_btn
        # isstickmove=joycon2.stick_l

        # if isstickmove[1] > 3000:

        #     ship2.rect.x -= 3
        #     t2 = 3
        #     if pygame.sprite.spritecollideany(ship2,blocks):
        #         ship2.rect.x += 3
        #     #('up')
        # elif isstickmove[1] < 2000:
        #     #ship.y += 3
        #     #('down')
        #     t2 = 2
        #     ship2.rect.x += 3
        #     if pygame.sprite.spritecollideany(ship2,blocks):
        #         ship2.rect.x -= 3
        
        # elif isstickmove[0] > 3000:
        #     #ship.x += 3
        #     #('r')
        #     ship2.rect.y -= 3
        #     t2 = 0

        #     if pygame.sprite.spritecollideany(ship2,blocks):
        #         ship2.rect.y += 3
        if isstickmove[1] > 2000:
            #ship.x -= 3
            #('l')
            t2 = 1
            for itm in range(len(blocks)):
                    ys[itm] -= 0.01

                    ######################('ll')

                    blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
        if isstickmove[1] < 1000:
            #ship.x -= 3
            #('l')
            t2 = 1
            for itm in range(len(blocks)):
                    ys[itm] += 0.01

                    ######################('ll')

                    blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])





        if isstickmove[0] > 3000:
            #ship.x -= 3
            #('l')
            t2 = 1
            # scene.forward = scene.forward.rotate(angle=+0.005, axis=vec(0,1,0))
            for block in blocks:
                # block.rotate(angle=+0.005, axis=vec(0,1,0))
                block.rotate(angle=+0.005, axis=vec(0,1,0), origin=vector(gear1.pos))
            print(len(blocks))
            c -= 5
            #gear1.rotate(angle=+0.5, axis=vec(c, 0, 0))
            print(c)
        if isstickmove[0] < 1000:
            #ship.x -= 3
            #('l')
            t2 = 1
            # scene.forward = scene.forward.rotate(angle=+0.005, axis=vec(0,1,0))
            for block in blocks:
                # block.rotate(angle=+0.005, axis=vec(0,1,0))
                #block.rotate(angle=-0.5, axis=drone.pos)
                block.rotate(angle=-0.005, axis=vec(0,1,0), origin=vector(gear1.pos))
            # scene.forward = scene.forward.rotate(angle=-0.005, axis=vec(0,1,0))

        isstickbut = joycon2.stick_l_btn
        isstickmove=joycon2.stick_l
        
        if isstickmove[1] >= 2500:
          for itm in range(len(blocks)):
              zs[itm] += 0.01
              blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
                
        # for itm in range(len(blocks)):
        #     if  drone.pos.x == xs[itm] and drone.pos.y == ys[itm] and drone.pos.z == zs[itm]:
        #         print('ppp')
        #     print(drone.pos.x, xs[itm], drone.pos.y, ys[itm], drone.pos.z, zs[itm])
    
        for itm in range(len(buls)):
            try:
                
                zd[itm] -= 0.01
                buls[itm].pos = vector(0,0,zd[itm])
                buls[itm].range -= 1
                if buls[itm].range <= 0:
                    buls.pop(itm)
                    zd.pop(itm)
                    yc.pop(itm)
                    xb.pop(itm)

            except IndexError:
                pass

        dist.direction = drone.pos
        if isstickbut != 0:
            if a >= 0:
                a = 0
                wallpT = drone.clone()
                wallpT.range = 1000
            

                buls.append(wallpT)
                xb.append(0)

                yc.append(0)
                zd.append(0)
            gear1.rotate(angle=-0.1, axis=vector(0,0,1))
            pass
        time.sleep(0.005)

        # for itm in range(len(blocks)):
        #     if  drone.pos.x == xs[itm] and drone.pos.y == ys[itm] and drone.pos.z == zs[itm]:
        #         print('ppp')
    



        