try:
    import pygame
    import time
    import sys
    false = False
    dobollet = False
    from pygame.sprite import Sprite
    from pygame.sprite import Group
    from random import *
    from tkinter import *
    from random import *
    import tkinter.messagebox
    import time
    import random
    import winsound
    from time import sleep
    import turtle
    from turtle import *
    from dolibe import *
 
    import pygame.mixer_music
    import pygame
    import pyjoycon
    from pyjoycon import *

    class MyJoyCon(
            pyjoycon.GyroTrackingJoyCon,
            pyjoycon.ButtonEventJoyCon,
        ): pass
    class MyJoyCon2(
            pyjoycon.GyroTrackingJoyCon,
            pyjoycon.ButtonEventJoyCon,
        ): pass

    joycon_id = get_R_ids()
    joycon_id = get_L_ids()
    print (joycon_id)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    #pink joycon right (1406, 8199, '9458cbb41938')
    #blue joycon left   

    joycon = MyJoyCon(1406, 8199, 'e0f6b5c308dc')
    joycon.get_status()
    # joycon2 = MyJoyCon(1406, 8199, 'e0f6b5c00b14')
    # joycon2.get_status()
    # joycon3 = MyJoyCon(1406, 8199, '9458cbb3aeaa')
    # joycon3.get_status()
    # joycon2 = MyJoyCon(1406, 8199, '9458cbb3aeaa')
    # joycon2.get_status()
#(1406, 8198, 'e0f6b5c00b14'),(1406, 8198, '9458cbb3aeaa'), (1406, 8198, 'e0f6b5c00b14')

    
    pygame.mixer.init()
    bulets = 0
    def chekupdown_fleet_duraction(ai_settings,aliens):

        ai_settings.fleet_direction *= -1

    def chekupdown_fleet_edges(ai_settings,aliens):
        for alien in aliens.sprites():
            if alien.chek_edges():
                chekupdown_fleet_duraction(ai_settings,aliens)
                break

    def do_bombfiled(Block,screen,blocks,ai_settings,ship):
        global xy
        for y in range(6):
            
            for x in range(6):
                block = Block(ai_settings,screen,x*(ai_settings.screen_width/5),y*(ai_settings.screen_height/5))
                
                blocks.add(block)
                x += 1
        
                #print(len(blocks))


except ConnectionRefusedError:
    print('please run again')

else:
    images = ['cat1.gif','cat2.gif','tree.gif','tree.gif']
    ch = 1000
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 3
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 1
            self.bullet_color = 60,60,60
            self.bullet_width = 10
            self.bullet_height = 10 
            self.bullet_allowed =  3
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien,t):
            super(Bullet, self).__init__()
            
            self.t = t
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

            self.aliens = aliens
            self.bullets = bullets
            

            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            
            global ch
            global ch
            if self.t == 0:
                self.y -= self.speed_factor
                self.rect.y = self.y
                
            if self.t == 1:
                self.y += self.speed_factor
                self.rect.y = self.y
            if self.t == 2:
                self.x += self.speed_factor
                self.rect.x = self.x
            if self.t == 3:
                self.x -= self.speed_factor
                self.rect.x = self.x
                
        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)  
            
    class Block(Sprite):
        def __init__(self,ai_settings,screen):
            super(Block, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("block.gif")
            self.rect = self.image.get_rect()

            
            

            self.y = float(self.rect.y)
            #elf.rect.x = self.rect.width
            self.x = float(self.rect.x)

        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def update(self):
            
            pass
    class Ship(Sprite):
        def __init__(self,ai_settings,screen):
            super(Ship,self).__init__()
            self.screen = screen
            self.canr = True
            self.canl = True
            self.canu = True
            self.cand = True
            self.image = pygame.image.load("supercat.gif")
            self.rect = self.image.get_rect()
            self.movin_right = False
            self.movin_left = False
            self.ai_settings = ai_settings
        
            
            
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
            self.x = float(self.rect.x)
            self.senter = float(self.rect.x)
            self.y = float(self.rect.y)
            self.movin_down = False
            self.movin_up = False
                
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom/2
            self.x = float(self.rect.x)
            self.senter = float(self.rect.x)
            self.y = float(self.rect.y)
            


        def update(self,blocks,ship):
            if self.movin_right and self.rect.right < self.screen_rect.right:
                #self.rect.centerx += 1
                self.senter += self.ai_settings.ship_speed_factor
                self.canr = False
                self.rect.centerx = self.senter
                if pygame.sprite.spritecollideany(ship,blocks):
                    if self.canr == False:
                        print('ouch right')
            if self.movin_left and self.rect.left > 0:
                #self.rect.centerx -= 1
                self.senter -= self.ai_settings.ship_speed_factor
                self.rect.centerx = self.senter
                if pygame.sprite.spritecollideany(ship,blocks):
                    if self.canr == False:
                        print('ouch left')
            if self.movin_up:
                self.rect.bottom -= 1
            if self.movin_down:
                self.rect.bottom += 1

        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Alien(Sprite):
        def __init__(self,ai_settings,screen,alienBullets,alienBullet,ship):
            super(Alien, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            
            

            self.image = pygame.image.load("robot.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)
            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            self.ship = ship
            self.direction = 0
        def blitme(self):
            self.screen.blit(self.image,self.rect)

        def chek_edges(self):
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                return True
            if self.rect.left <= 0:
                return True
            
        def update(self):


            if self.direction == 0:
                self.x -= 1
                self.rect.x = self.x

                self.image = pygame.image.load('tank_right.gif')
            if self.direction == 1:
                self.x += 1
                self.rect.x = self.x

                image = pygame.image.load('tank_left.gif')
            if self.direction == 2:
                self.y -= 1
                self.rect.y = self.y

                image = pygame.image.load('tank_up.gif')
            if self.direction == 3:
                self.y += 1
                self.rect.y = self.y

                image = pygame.image.load('tank_down.gif')

            self.rect.x = self.x
            self.rect.y = self.y
    class Alien_what_go_left_and_right(Sprite):
        def __init__(self,ai_settings,screen):
            super(Alien_what_go_left_and_right, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            n = randint(1,4)
            ns = str(n)
            

            self.image = pygame.image.load("robot"+ns+".gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.duraction = 0.6
            
            self.y = float(self.rect.y)
            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            #self.ship = ship
        def blitme(self):
            self.screen.blit(self.image,self.rect)

        def chek_edges(self):
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                return True
            if self.rect.left <= 0:
                return True
            
        def update(self):


            self.x += self.duraction
            self.rect.x = self.x
    class Alien_what_go_up_and_down(Sprite):
        def __init__(self,ai_settings,screen):
            super(Alien_what_go_up_and_down, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            #self.alienBullet = alienBullet
            

            self.image = pygame.image.load("robot.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.duraction = -1
            self.y = float(self.rect.y)
            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            
        def blitme(self):
            self.screen.blit(self.image,self.rect)

        def chek_edges(self):
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                return True
            if self.rect.left <= 0:
                return True
            
        def update(self):


            self.y += self.duraction
            self.rect.y = self.y
            
            

    class alienBullet2(Sprite):
        def __init__(self,ai_settings,screen,alien,ship):
            super(alienBullet2, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            self.ship = ship
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.alien_rect = alien.image.get_rect()
            self.aliens = alien
    
            self.go = 0
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = alien.rect.centerx
            self.rect.top = alien.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = 2
            

        def update(self,bullets,aliens):
            global ch
            global ch
            if self.go == 0:
                self.y += self.speed_factor
                self.rect.y = self.y
                rand = randint(-1000,1000)
                if rand == 0:
                    self.ai_settings.bullet_height = 345
                    self.ai_settings.bullet_width = 345
                    
        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)            
            
    class alienBullet(Sprite):
        def __init__(self,ai_settings,screen,alien):
            super(alienBullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
        
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.alien_rect = alien.image.get_rect()
            self.aliens = alien
    
            self.go = 0
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = alien.rect.centerx
            self.rect.top = alien.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            self.y += 1
            self.rect.y = self.y    
        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)

    def run_game():
        global ch,dobollet,t,bulets,t2
        forrand = 1000
        pygame.init()
        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for joystick in joysticks:
            joystick.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        ship2 = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()
        ships = Group()
        ships.add(ship)
        ships2 = Group()
        ships2.add(ship2)
        blocks = Group()
        cu = 1
        cd = 1
        cr = 1
        moneys = 0
        cl = 1
        cu2 = 1
        cd2 = 1
        cr2 = 1
        ship.y -= 47
        ship.rect.y = ship.y
        moneys = 0
        cl2 = 1
        tank = 0
        fuster = 1
        poweraps = Group()
        updatenow = 0
        bezero = 0
        die_blocks = Group()
        tr = '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0,0,0,0,0,0,1,4,0,3,3,3,0,7,0,1,1,1,1,2,1,0,0,0,0,0,0,1,4,7,6,3,0,0,1,0,0,0,0,0,1,2,1,0,0,1,0,0,0,1,4,4,3,3,0,1,0,0,1,0,0,1,2,1,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,7,7,6,0,1,2,1,0,0,1,0,0,4,1,0,0,0,1,0,0,0,0,1,0,0,1,2,1,0,0,0,0,0,4,1,0,7,6,6,0,1,0,3,0,4,3,0,0,1,2,1,0,4,0,7,7,4,0,0,0,3,1,0,3,0,0,0,0,0,1,2,1,0,4,1,7,7,4,1,4,4,0,1,1,1,1,1,1,0,4,1,2,1,3,4,3,1,7,7,1,1,7,7,7,7,7,7,7,0,0,0,1,2,1,3,4,3,1,7,7,7,7,6,7,7,7,6,7,7,7,7,0,0,0,1,2,1,3,4,3,1,1,7,7,1,1,1,1,1,7,7,7,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1'
        filename = 'liberint.txt'
#        t = []



    
    
        alienbullets = Group()
        score = 0
    
        
        do_liberint(pygame,Block,blocks,ai_settings,screen,poweraps,filename,Alien_what_go_up_and_down,Alien_what_go_left_and_right,aliens,aliens)
        for power in poweraps.sprites():
            power.image = pygame.image.load('bomb.gif')
            
        
        

        bg_color = (20,250,200)
        invis = 0
        ships.add(ship)
        for block in blocks.sprites():

            if pygame.sprite.spritecollideany(block,ships):
                blocks.remove(block)
                


       #shoot = mixer.Sound('Contra.mp3')
        #shoot.play(-1)

#        shoot = mixer.Sound("C:\windows\media\Ring02.wav")C:\windows\downloads\
        while True:
            for block in aliens.sprites():

                if pygame.sprite.spritecollideany(block,blocks):
                    block.direction += 1 
                    
                    if block.direction == 4:
                        block.direction = 0
                    

            if random.randint(0,100) == 23:
                alien = Alien(ai_settings,screen,0,0,ship)
                aliens.add(alien)

                while pygame.sprite.spritecollideany(alien,blocks):
                    alien.x = randint(0,ai_settings.screen_width)
                    alien.y = randint(0,ai_settings.screen_height)
                    alien.rect.x = alien.x
                    alien.rect.y = alien.y
            # for event_type, status in joycon1.events():
            #     if status == 1:
            #         if 
            isstickmove=joycon.stick_r
            if isstickmove[1] > 3000:
                
                ship.rect.x += 1
                t = 2
                ship.image = pygame.image.load('tank_left.gif')
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.x -= 1

            elif isstickmove[1] < 1000:
                #ship.y += 3
                print('down')
                ship.rect.x -= 1
                t = 3
                ship.image = pygame.image.load('tank_right.gif')
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.x += 1
            elif isstickmove[0] > 3000:
                #ship.x += 3
                print('r')
                ship.rect.y += 1
                t = 1
                ship.image = pygame.image.load('tank_down.gif')
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.y -= 1
            elif isstickmove[0] < 1000:
                #ship.x -= 3
                print('l')
                ship.rect.y -= 1
                ship.image = pygame.image.load('tank_up.gif')
                t = 0
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.y += 1
            # isstickmove=joycon2.stick_l
            # if isstickmove[1] > 3000:
                
            #     ship2.rect.x += 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.x -= 1
            # elif isstickmove[1] < 1000:
            #     #ship.y += 3
            #     print('down')
            #     ship.rect.x -= 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.x += 1
            # elif isstickmove[0] > 3000:
            #     #ship.x += 3
            #     print('r')
            #     ship2.rect.y += 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.y -= 1
            # elif isstickmove[0] < 1000:
            #     #ship.x -= 3
            #     print('l')
            #     ship2.rect.y -= 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.y += 1

            for event_type, status in joycon.events():
                if status == 1:
                    if event_type == 'x':
                        bul = Bullet(ai_settings,screen,ship,1,1,1,t)
                        bullets.add(bul)

                print(event_type, status)
            # for event_type, status in joycon3.events():
            #     print("ButtonEventJoyCon:")
            #     print(event_type, status)
            # for event_type, status in joycon4.events():
            #     print("ButtonEventJoyCon:")
            #     print(event_type, status)
            if len(alienbullets) <=0:
                for alien in aliens.sprites():
                    if randint(0,500) == 34:

                        bul = Bullet(ai_settings,screen,alien,2,1,alien,0)
                        alienbullets.add(bul)

            screen.fill(ai_settings.bg_color)
            for bul in bullets.sprites():
                bul.draw_bullet()
            for bul in alienbullets.sprites():
                bul.draw_bullet()
            blocks.draw(screen)
            die_blocks.draw(screen)
            ships.draw(screen)
            ships2.draw(screen)
            bullets.update(1,1)
            collision = pygame.sprite.groupcollide(bullets,blocks,True,false)
            collision = pygame.sprite.groupcollide(alienbullets,blocks,True,false)
            collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
            collision = pygame.sprite.groupcollide(bullets,alienbullets,True,True)
            collision = pygame.sprite.groupcollide(ships,alienbullets,True,True)
            aliens.draw(screen)
            aliens.update()
            alienbullets.update(2,1)
            pygame.display.flip()
run_game()