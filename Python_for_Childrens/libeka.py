import vpython
from vpython import *
import random
import pygame
import dolibe_vp
pygame.init()
scene.width = scene.height = 1000
scene.background = color.gray(0.9)
scene.range = 2.2
blocks = []
dolibe_vp.do_liberint('vp_libe.txt', blocks)
xs = []
ys = []
zs = []
scene.caption = "Click to pick an object and make it red."
scene.append_to_caption("\nNote picking of individual curve segments.")
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
v0 = vertex(pos=vector(-.5,1.2,0), color=color.green)
v1 = vertex(pos=vector(1,1.2,0), color=color.red)
v2 = vertex(pos=vector(1,2,0), color=color.blue)
v3 = vertex(pos=vector(-.5,2,0), color=color.yellow)
extrusion(path=[vector(-1.8,-1.3,0), vector(-1.4,-1.3,0)],
            shape=shapes.circle(radius=.5, thickness=0.4), color=color.yellow)

lasthit = None
lastpick = None
lastcolor = None

def getevent():
    global lasthit, lastpick, lastcolor
    scene.empty()
    for ghy in blocks:
        blocks.remove(ghy)
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
# while True:
#         for event in pygame.event.get():
#             print(len(blocks),event) 
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_1:
                    
#                     for itm in range(len(blocks)):
#                         xs[itm] += 1
#                         blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
#             print(len(blocks),event) 
#         for itm in range(len(blocks)):
#             tre = random.randint(0,3)
#             if tre == 0:
#                 xs[itm] += 0.001
#                 zs[itm] += 0.001

#             blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])