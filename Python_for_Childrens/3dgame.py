import vpython
from vpython import *
import random
import pygame
import dolibe_vp
pygame.init()
scene.width = scene.height = 1000
scene.background = color.gray(0.9)
scene.range = 2.2
side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
xs = []
ys = []
zs = [] 
blocks = []
wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
blocks.append(wallR)
xs.append(side)
ys.append(0)
zs.append(0)

wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
blocks.append(wallL)
xs.append(-side)
ys.append(0)
zs.append(0)

wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
blocks.append(wallB)
ys.append(-side)
xs.append(0)
zs.append(0)

wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
blocks.append(wallT)
ys.append(side)
xs.append(0)
zs.append(0)

wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))
blocks.append(wallBK)
ys.append(0)
xs.append(0)
zs.append(side)


scene.caption = "Click to pick an object and make it red."
scene.append_to_caption("\nNote picking of individual curve segments.")
box(pos=vector(0,3,0), color=color.cyan, opacity=1)

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

lasthit = None
lastpick = None
lastcolor = None

while True:
    
#         for event in pygame.event.get():
#             print(len(blocks),event) 
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_1:
                    
#                     for itm in range(len(blocks)):
#                         xs[itm] += 1
#                         blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
#             print(len(blocks),event) 
        for itm in range(len(blocks)):
            tre = random.randint(0,3)
            if tre == 0:
                zs[itm] += 0.0001

            blocks[itm].pos = vector(xs[itm],ys[itm],zs[itm])
        scene.forward = scene.forward.rotate(angle=-0.00000005, axis=vec(0,1,0))