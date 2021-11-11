#filename = 'liberint.txt'
import sys
x,y = 0,0
    
#[1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]

def do_liberint(pygame,Block,blocks,ai_settings,screen,t):
    global x,y
    

    for yu in t:

        if yu == '0':
            x+=58
            
            
        if yu == '1':
            block = Block(ai_settings,screen)  
            blocks.add(block)
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y      

            #x+=56        
            x+=58
        
        if yu == '3':
            block = Block(ai_settings,screen)  
            blocks.add(block)
            block.image = pygame.image.load('warrior.gif')
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y      

            #x+=56        
            x+=58
        
        if yu == '4':
            block = Block(ai_settings,screen)  
            blocks.add(block)
            block.image = pygame.image.load('bomb.gif')
            block.rect.x = x
            block.rect.y = y
            block.x = x
            block.y = y      

            #x+=56        
            x+=58
        
        if yu == '2':
            x = 0
            y+=58
            #y += 112

        

