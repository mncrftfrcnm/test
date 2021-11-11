import pygame
import time
import sys
import random

pygame.init()
screen = pygame.display.set_mode((100, 120))

tank = pygame.image.load('tank_left.gif')
x=20
y=20
direct=1
#1 left
#2 right
#3 up
#4 down

def tank_image_choice(direct_number):
    global tank
    if direct_number==1:
        tank = pygame.image.load('tank_left.gif')
    if direct_number==2:
        tank = pygame.image.load('tank_right.gif')
    if direct_number==3:
        tank = pygame.image.load('tank_up.gif')
    if direct_number==4:
        tank = pygame.image.load('tank_down.gif')


#Tank moving
while 1:
    pygame.time.wait(int(1000/60))
    if direct==1:
        if x>70:
            numberList = [2,3,4]
            direct=random.choice(numberList)
            tank_image_choice(direct)
        x+=1
    if direct==2:
        if x<20:
            numberList = [1,3,4]
            direct=random.choice(numberList)
            tank_image_choice(direct)
        x-=1
    if direct==3:
        if y<20:
            numberList = [1,2,4]
            direct=random.choice(numberList)
            tank_image_choice(direct)
        y-=1
    if direct==4:
        if y>70:
            numberList = [1,2,3]
            direct=random.choice(numberList)
            tank_image_choice(direct)
        y+=1

    screen.fill((0,0,0))
    screen.blit(tank,(x,y))
    pygame.display.flip()
    pygame.display.update()