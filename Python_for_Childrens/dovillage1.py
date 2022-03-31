#filename = 'liberint.txt'
import sys
from random import *
filename = 'liberint.txt'
# yt = str(ty)
t = []
images = ['treesmall.gif','bushsmall.gif']
#[1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
x,y = 0,0
def do_liberint(pygame, Block, blocks, ai_settings, screen, liberint, rupees, NPC,npcs):
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
        elif yu == 'r':
            block = Block(ai_settings,screen,'1money.gif')
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y
            rupees.add(block)
            x+=58
        elif yu == '8':
            block = NPC(ai_settings=ai_settings,screen=screen,text='My name is Tatiana Ponteleevna. You must stay hear all your life.muahahahhahahahahahahaaa!')
            block.rect.x = x
            block.rect.y = y
            block.image = pygame.image.load('book.gif')
            npcs.add(block)
            block.x = x
            block.y = y
            x+=58
        elif yu == '9':
            block = NPC(ai_settings=ai_settings,screen=screen,text="Hello. I'm Vova's friend. The school is boring. I'm playing vidio games at home. I will play vidiogames. ")
            block.rect.x = x
            block.rect.y = y
            block.image = pygame.image.load('pupil.gif')
            npcs.add(block)
            block.x = x
            block.y = y
            x+=58
