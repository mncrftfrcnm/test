#filename = 'liberint.txt'
import sys
from random import *
filename = 'liberint.txt'
# yt = str(ty)
t = []
images = ['treesmall.gif','bushsmall.gif']
#[1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
x,y = 0,0
def do_liberint(pygame, Block, blocks, ai_settings, screen, liberint, mega, leftright, aliens, guns=0, Alien=0):
    global x,y

    x,y = 0,0
    filename = liberint
    # yt = str(ty)
    t = []
    with open(filename, 'r') as file_object:
        contents = file_object.read()
        for yuu in contents:
            t.append(yuu)
            

    for yu in t:

        if yu == '0':
            x += 58
        elif yu == '1':
            block = Block(ai_settings,screen,'Block.gif')
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            blocks.add(block)
            x+=58
        elif yu == '2':
            y+=58
            x = 0
        elif yu == '3':
            block = mega(ai_settings,screen)

            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            aliens.add(block)
            x+=58
        elif yu == '3':
            block = mega(ai_settings,screen)
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            aliens.add(block)
            x+=58
        elif yu == '4':
            block = leftright(ai_settings, screen)
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            aliens.add(block)
            x+=58
        elif yu == '5':
            block = Alien(ai_settings, screen)
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            guns.add(block)
            x+=58
            