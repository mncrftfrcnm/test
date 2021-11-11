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
    from winsound import PlaySound,SND_ASYNC,Beep
    import threading
    from threading import Timer,Thread
    from time import sleep
    import turtle
    from turtle import *
    from dolibe import *
    import sys 
    from PIL import Image
    t = 0
    t2 = 0
    
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
                print(block.rect.x)
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
            self.bullet_speed_factor = 1
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 1
            self.bullet_color = 60,60,60
            self.bullet_width = 100
            self.bullet_height = 106
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
            self.rect = self.image.get_rect()
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
            
            self.screen.blit(self.image,self.rect)
            
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
        def blitme(self):
            self.screen.blit(self.image,self.rect)

        def chek_edges(self):
            screen_rect = self.screen.get_rect()
            if self.rect.right >= screen_rect.right:
                return True
            if self.rect.left <= 0:
                return True
            
        def update(self):


            if self.rect.x > self.ship.rect.x:
                self.x -= 0.1
            if self.rect.x < self.ship.rect.x:
                self.x += 0.1
            if self.rect.y > self.ship.rect.y:
                self.y -= 0.1
            if self.rect.y < self.ship.rect.y:
                self.y += 0.1

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
        print(len(joysticks))
        for joystick in joysticks:
            joystick.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()
        ships = Group()
        ships.add(ship)
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
    
    
        alienbullets = Group()
        score = 0
        liberint = 'liberint.txt'
        do_liberint(pygame,Block,blocks,ai_settings,screen,liberint)
        for power in poweraps.sprites():
            power.image = pygame.image.load('bomb.gif')
        

        bg_color = (20,250,200)
        while True:
            col = pygame.sprite.groupcollide(ships,poweraps,False,True)
            # if cr == 0:
                
            #     for alien in aliens.sprites():
                    
            #         alien.x += 1
            #         alien.rect.x = alien.x
            # elif cl == 0:
            #     #updatenow = 1
            #     for alien in aliens.sprites():
            #         alien.x -= 1
            #         alien.rect.x = alien.x
            if cr == 0:

                ship.x += 1
                ship.rect.x = ship.x
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.x -=1
                    ship.rect.x = ship.x



            if cl == 0:

                ship.x -= 1
                ship.rect.x = ship.x
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.x +=1
                    ship.rect.x = ship.x


            if cd == 0:
                ship.y += 1
                ship.rect.y = ship.y
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.y -=1
                    ship.rect.y = ship.y
                if ship.rect.y >= ai_settings.screen_height:
                    ship.y = ai_settings.screen_height/2
                    ship.rect.y = ship.y
                    for alien in blocks.sprites():
                        alien.y -= 10#ai_settings.screen_height
                        alien.rect.y = alien.y
                    for alien in poweraps.sprites():
                        alien.y -= 10
                        alien.rect.y = alien.y
                    for alien in aliens.sprites():
                        alien.y -= 10
                        alien.rect.y = alien.y
                    for alien in die_blocks.sprites():
                        alien.y -= 10
                        alien.rect.y = alien.y 
            if cu == 0:
                #for alien in blocks.sprites():
                ship.y -= 1
                ship.rect.y = ship.y
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.y +=1
                    ship.rect.y = ship.y
                if ship.rect.y <= 0:
                    ship.y = ai_settings.screen_height
                    ship.rect.y = ship.y
                    for alien in blocks.sprites():
                        alien.y += 10#ai_settings.screen_height
                        alien.rect.y = alien.y
                    for alien in poweraps.sprites():
                        alien.y += 10
                        alien.rect.y = alien.y
                    for alien in aliens.sprites():
                        alien.y += 10
                        alien.rect.y = alien.y
                    for alien in die_blocks.sprites():
                        alien.y += 10
                        alien.rect.y = alien.y 
            for event in pygame.event.get():

                
            #for event in pygame.event.get():

# #                if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_1:
#                         first = randint(0,220)
#                         second = randint(0,220)
#                         three = randint(0,220)
#                         ai_settings.bg_color = (first,second,three)
#                     if event.key == pygame.K_b:
#                         sys.exit()
#                     if event.key == pygame.K_RIGHT:
                        
#                         #ship.movin_right = True
#                         cr = 0
#                         t = 2
#                     if event.key == pygame.K_LEFT:
#                         #ship.movin_left = True
#                         cl = 0
#                         t = 3
                    # if event.key == pygame.K_r:
                    #     #ship.movin_left = True
                    #     if len(bullets) <= bulets:
                    #         new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,0)
                    #         bullets.add(new_bullet)
                    # if event.key == pygame.K_UP:
                        
                    #     cu = 0
                    #     t = 0
                if event.type == pygame.JOYAXISMOTION:
                    buttons = joystick.get_numaxes()
                    for i in range(buttons):
                        but = joystick.get_axis(0)
                        if but < -.5:

                            cl = 0
                            cr = 1
                            cu = 1
                            cd = 1
                            t = 3
                        but = joystick.get_axis(0)
                        if but > .5:

                            cl = 1
                            cr = 0
                            cu = 1
                            cd = 1
                            t = 2
                        but = joystick.get_axis(1)
                        if but <  -.5:

                            cl = 1
                            cr = 1
                            cu = 0
                            cd = 1
                            t = 0
                        but = joystick.get_axis(1)
                        if but > .5:

                            cl = 1
                            cr = 1
                            cu = 1
                            cd = 0
                            t = 1
                        
                if event.type == pygame.JOYHATMOTION:
                
                    buttons = joystick.get_numhats()
                    for i in range(buttons):
                        but = joystick.get_hat(i)
                        if but == (-1,0):

                            cl = 0
                            cr = 1
                            cu = 1
                            cd = 1
                            t = 3
                        but = joystick.get_hat(i)
                        if but == (1,0):

                            cl = 1
                            cr = 0
                            cu = 1
                            cd = 1
                            t = 2
                        but = joystick.get_hat(i)
                        if but == (0,1):

                            cl = 1
                            cr = 1
                            cu = 0
                            cd = 1
                            t = 0
                        but = joystick.get_hat(i)
                        if but == (0,-1):

                            cl = 1
                            cr = 1
                            cu = 1
                            cd = 0
                            t = 1
    
                if event.type == pygame.JOYBUTTONDOWN:
                    numbutt = joystick.get_numbuttons()
                    for but in range(numbutt):

                        button = joystick.get_button(1)
                    # print(button)  
                    #pass
                        if button:
                            cl = 1
                            cr = 0
                            cu = 1
                            cd = 1
                            t = 3
                        button = joystick.get_button(2)
                    # print(button)  
                    #pass
                        if button:
                            cl = 0
                            cr = 1
                            cu = 1
                            cd = 1
                            t = 2
                        button = joystick.get_button(3)
                    # print(button)  
                    #pass
                        if button:
                    
                            cl = 1
                            cr = 1
                            cu = 0
                            cd = 1
                            t = 0
                        button = joystick.get_button(0)
                    # print(button)  
                    #pass
                        if button:
                            cl = 1
                            cr = 1
                            cu = 1
                            cd = 0
                            t = 1
                        button = joystick.get_button(5)
                    # print(button)  
                    #pass
                        if button:
                            block = Block(ai_settings,screen)
                            if t == 1:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.y+=100
                                block.rect.y = block.y
                            blocks.add(block)
                            if t == 0:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.y-=100
                                block.rect.y = block.y
                            blocks.add(block)
                            if t == 2:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.x+=100
                                block.rect.x = block.x
                            blocks.add(block)
                            if t == 3:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.x-=100
                                block.rect.x = block.x
                            blocks.add(block)
                        
                        # new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                        # bullets.add(new_bullet)

                
                elif event.type == pygame.JOYBUTTONUP:
                        #buttons = joystick.get_numbuttons()
                    button = joystick.get_button(False)
                    
                    
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LEFT:

                        cl = 0
                        cr = 1
                        cu = 1
                        cd = 1
                        t = 3
                        
                    if event.key == pygame.K_RIGHT:

                        cl = 1
                        cr = 0
                        cu = 1
                        cd = 1
                        t = 2
                        #but = joystick.get_hat(i)
                    if event.key == pygame.K_DOWN:

                        cl = 1
                        cr = 1
                        cu = 1
                        cd = 0
                        t = 1
                    if event.key == pygame.K_f:
                        tytyty = 0
                        if tytyty == 0:
                            block = Block(ai_settings,screen)
                            if t == 1:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.y+=100
                                block.rect.y = block.y
                            blocks.add(block)
                            if t == 0:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.y-=100
                                block.rect.y = block.y
                            blocks.add(block)
                            if t == 2:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.x+=100
                                block.rect.x = block.x
                            blocks.add(block)
                            if t == 3:
                                block.y = ship.rect.y
                                block.x = ship.rect.x
                                block.rect.y = block.y
                                block.rect.x = block.x
                                block.x-=100
                                block.rect.x = block.x
                    #but = joystick.get_hat(i)
                    if event.key == pygame.K_UP:

                        cl = 1
                        cr = 1
                        cu = 0
                        cd = 1
                        t = 0
                    if event.key == pygame.K_v:
                        new_bullet = Bullet(ai_settings,screen,ship2,aliens,bullets,alien,t2)
                        bullets.add(new_bullet)
                        
                    
#                 elif event.type == pygame.KEYUP:
#                     if event.key == pygame.K_RIGHT:
                        
#                         ship.movin_right = False
#                         cr = 1

#                     if event.key == pygame.K_LEFT:
#                         ship.movin_left = False
#                         cl = 1
#                     if event.key == pygame.K_UP:
                        
#                         cu = 1

#                     if event.key == pygame.K_DOWN:
#                         cd = 1
#                     if event.key == pygame.K_2:
#                         ship.image = pygame.image.load(random.choice(images))
#                     if event.key == pygame.K_DOWN:
#                         ship.movin_down = False
# #276
#276
            ship.update(blocks,ship)
  
        
            bullets.update(bullets,aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            
                          #print('you lose')
            #break
            ship.blitme()

                
 #           pygame.display.flip()
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0 or bullet.rect.bottom >= 900 or bullet.rect.centerx <= 0 or bullet.rect.centerx >= 1000:
                    bullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            # for bullet in alienbullets.copy():
            #     if bullet.rect.bottom >= 900:
            #         bullets.remove(bul
            # screen.fill(ai_settings.bg_color)
            
            # for bullet in alienbullets.sprites():
                
            #     bullet.draw_bullet()
                    
            #     first = randint(0,200)
            #     second = randint(0,200)
            #     three = randint(0,200)
            #     ai_settings.bullet_color = (first,second,three)
            #     collisins = pygame.sprite.groupcollide(blocks,bullets,True,True)
            if pygame.sprite.spritecollideany(ship,aliens):
                print('you lose')
                sys.exit()

            for alien in poweraps.sprites():
                if pygame.sprite.spritecollideany(ship,poweraps):
                    poweraps.remove(alien)
                    bulets += 1
            
                
            for alien in aliens.sprites():

                if pygame.sprite.spritecollideany(alien,blocks):
                    alien.duraction *= -1
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
                if collisions:
                    moneys+=1
                
                
                collisions = pygame.sprite.groupcollide(bullets,blocks,True,False)
                

                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)

            bullets.update(bullets,aliens)
            ship.blitme()
            #chekupdown_fleet_edges(ai_settings,aliens)
            #alien.blitme()
            bullets.draw(screen)
            alienbullets.update(bullets,aliens)
            aliens.draw(screen)
            if updatenow == 0:

                aliens.update()
    
            blocks.draw(screen)
            blocks.update()
            # if len(poweraps) <= 0:
            #     print('you win')
            #     break
            if bezero == 34:
                cl = 1
                cu = 1
                cd = 1
                cr = 1
            
            poweraps.draw(screen)
            
            #bezero = 0
            die_blocks.draw(screen)
                
            pygame.display.flip()
            
            

    while True:
        run_game()
    