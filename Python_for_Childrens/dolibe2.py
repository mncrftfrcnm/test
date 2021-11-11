tr = [1,1,1]
x,y = 0,0
def do_liberint(ship,Block,blocks,ai_settings,screen,libe,f1,f2,f3,pygame):
    global x,y
    tr = libe
    print('1 for 1 image, 2 for enter, 0 for nothing image,3 for 2 image,4 for 3 image')
    

    for yu in tr:
        if yu == 3:
            block = Block(ai_settings,screen)        
            blocks.add(block)
            block.image = pygame.image.load(f2)
            block.rect.x = x
            block.rect.y = y
            x += 56            
        if yu == 4:
            block = Block(ai_settings,screen)        
            blocks.add(block)
            block.image = pygame.image.load(f3)
            block.rect.x = x
            block.rect.y = y
            x += 56            
        if yu == 0:
            x+=56
            print(x)
        if yu == 1:
            block = Block(ai_settings,screen)        
            blocks.add(block)
            block.image = pygame.image.load(f1)
        
            
            block.rect.x = x
            block.rect.y = y
            x += 56
            
        if yu == 2:
            x = 0
            y+=56

    print(y)
        

