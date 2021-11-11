tr = [0,1,0,1,2,1,0,1]
def do_liberint(ship,Block,ai_settings,screen,blocks):
    x,y = 0,0
    for yu in tr:
        if yu == 0:
            x+=ship.rect.x
        if yu == 1:
            print('do and add block')
            x+=ship.rect.x
        if yu == 0:
            x = 0
            y+=ship.rect.y
        
        

