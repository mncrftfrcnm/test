try:
    import pygame
    import time
    import sys
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
    import sys 
    from PIL import Image
    pupd = 0
    def get_number_rows(ai_settings,ship_height,alien_height):
        available_spase_y = ((ai_settings.screen_height - -1*alien_height) - ship_height)
        number_rows = int(available_spase_y / (1*alien_height))
        return number_rows
    def create_alien(ai_settings,screen,aliens,alien_number,row_number,alienbullets,alienBullet):
        alien = Alien(ai_settings,screen,alienbullets,alienBullet)

        alien_width = alien.rect.width
        available_spase_x = ai_settings.screen_width - 2*alien_width
        number_aliens_x = int(available_spase_x / (2*alien_width))
        alien.x = alien_width + 2*alien_width*alien_number
        alien.rect.x = alien.x
 #   alien_width = alien.rect.width
    
        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.y = alien.y
        aliens.add(alien)

except ConnectionRefusedError:
    print('please run again')

else:
    images = ['cat1.gif','cat2.gif','tree.gif','tree.gif']
    ch = 1000000000000000000
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 10
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 1
            self.bullet_color = 60,60,60
            self.bullet_width = 300
            self.bullet_height = 300
            self.bullet_allowed =  3788768767666767676655356655444444647575687
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien):
            super(Bullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.alien_rect = alien.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
            
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            global ch
            global ch
            tre = randint(0,3)
            if tre == 0:
                self.y -= 1
            if tre == 1:
                self.y += 1
            if tre == 2:
                self.x -= 1
            if tre == 3:
                self.x += 1
            self.rect.y = self.y
            self.rect.x = self.x
        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
    class Bullet2(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien):
            super(Bullet2, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.alien_rect = alien.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
            
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            global ch
            global ch
            tre = randint(0,0)
            if tre == 0:
                self.y -= 1
            self.rect.y = self.y
            

            

        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
            
    class Bullet3(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien):
            super(Bullet3, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
        
            self.alien_rect = alien.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
            
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

            
            

            

        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)
            
        
    class Ship(Sprite):
        def __init__(self,ai_settings,screen):
            super(Ship, self).__init__()
            self.screen = screen

            self.image = pygame.image.load("tree.gif")
            self.rect = self.image.get_rect()
            self.movin_right = False
            self.movin_left = False
            self.ai_settings = ai_settings
        
            
            
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom
            self.senter = float(self.rect.centerx)
            self.movin_down = False
            self.movin_up = False
                
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom


        def update(self):
            if self.movin_right and self.rect.right < self.screen_rect.right:
                #self.rect.centerx += 1
                self.senter += self.ai_settings.ship_speed_factor

            if self.movin_left and self.rect.left > 0:
                #self.rect.centerx -= 1
                self.senter -= self.ai_settings.ship_speed_factor
            if self.movin_up:
                self.rect.bottom -= 1
            if self.movin_down:
                self.rect.bottom += 1
            self.rect.centerx = self.senter
        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Alien(Sprite):
        def __init__(self,ai_settings,screen,alienBullets,alienBullet):
            super(Alien, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("fire.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)
            self.rect.x = self.rect.width
            self.x = float(self.rect.x)

        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def update(self):
            let = randint(0,4)
            if let == 0:
                self.y -= 10
             
            if let == 1:
                self.y += 10
            if let == 2:
                self.x -= 10
            if let == 3:
                self.x += 10

                
            self.rect.y = self.y
            self.rect.x = self.x
            if self.x == 0:
                self.x = self.ai_settings.screen_width /2
            if self.x == self.ai_settings.screen_width:
                self.x = self.ai_settings.screen_width /2

            
    class alienBullet(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(alienBullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.alien_rect = alien.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
            
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
            global ch
            global ch
            self.y += self.speed_factor
            self.rect.y = self.y
            

        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
           
    def run_game():
        global ch,pupd
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        bullets2 = Group()
        bullets3 = Group()
        bullets4 = Group()
        aliens = Group()
        ships = Group()
        ship = Ship(ai_settings,screen)
        ships.add(ship)

        alienbullets = Group()
            
        alien = Alien(ai_settings,screen,alienbullets,alienBullet)
        alien_width = alien.rect.width*1
        available_spase_x = ai_settings.screen_width - 0*alien_width
        number_aliens_x = int(available_spase_x / (1*alien_width))
        number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
        alien.y = -90
        alien.rect.y = alien.y
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
            
        
        
        #    print(alien.rect.y)
           
                create_alien(ai_settings,screen,aliens,alien_number,row_number,alienbullets,alienBullet)
        bg_color = (20,250,200)
        while True:
            
        

            for event in pygame.event.get():

                
            #for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        first = randint(0,220)
                        second = randint(0,220)
                        three = randint(0,220)
                        ai_settings.bg_color = (first,second,three)
                    if event.key == pygame.K_w:
                        new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien)
                        bullets.add(new_bullet)
                    if event.key == pygame.K_e:
                        new_bullet = Bullet2(ai_settings,screen,ship,aliens,bullets2,alien)
                        bullets2.add(new_bullet)
                    if event.key == pygame.K_r:
                        new_bullet = Bullet3(ai_settings,screen,ship,aliens,bullets3,alien)
                        bullets3.add(new_bullet)
                    if event.key == pygame.K_t:
                        new_bullet = Bullet3(ai_settings,screen,ship,aliens,bullets3,alien)
                        bullets4.add(new_bullet)

                    if event.key == pygame.K_c:
                        
                        for row_number in range(number_rows):
                            for alien_number in range(number_aliens_x):
                                
                            
                            
                            #    print(alien.rect.y)
                            
                                create_alien(ai_settings,screen,aliens,alien_number,row_number,alienBullet,alienbullets)
                    if event.key == pygame.K_b:
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        
                        ship.movin_right = True


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                    if event.key == pygame.K_t:
                        for alien in aliens.sprites():
                            aliens.remove(alien)
                    
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True
                    if event.key == pygame.K_q:
                        if pupd == 1:
                            pup = 0
#                    if event.key == pygame.K_q:
                        if pupd == 0:
                            pup = 1
                        pupd = pup

                    if event.key == pygame.K_DOWN:
                        ship.movin_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        ship.movin_right = False               
                    if event.key == pygame.K_LEFT:               
                        ship.movin_left = False               
                    if event.key == pygame.K_UP:               
                        
                        ship.movin_up = False
                    
                    if event.key == pygame.K_2:
                        ship.image = pygame.image.load(random.choice(images))
                    if event.key == pygame.K_DOWN:
                        ship.movin_down = False
            ship.update()
            alien.update()
            #collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            bullets.update(aliens,bullets)
            bullets2.update(aliens,bullets2)
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            print(len(bullets))
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
                if pygame.sprite.spritecollideany(alien,bullets):
                    ch = ch -1 
            if pupd == 0:
                collisions = pygame.sprite.groupcollide(ships,aliens,False,True)
            ship.blitme()
            alien.blitme()
            for bullet in bullets.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    bullets.remove(bullet)
                if bullet.rect.bottom <= 0:
        
                    bullets.remove(bullet)
                if bullet.rect.bottom >= ai_settings.screen_width:
                    bullets.remove(bullet)
                if bullet.rect.bottom <= -ai_settings.screen_width:
                    bullets.remove(bullet)
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
            for bullet in bullets2.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    bullets2.remove(bullet)

            for bullet in bullets2.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
            for bullet in bullets2.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    bullets2.remove(bullet)

            for bullet in bullets2.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
            for bullet in bullets3.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    bullets3.remove(bullet)

            for bullet in bullets3.sprites():
                
                bullet.draw_bullet()
                collisions = pygame.sprite.groupcollide(bullets3,aliens,True,True)
                bullets3.remove(bullet)        
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            
            
            collisions = pygame.sprite.groupcollide(bullets2,aliens,True,True)
            aliens.draw(screen)
            ship.blitme()
            pygame.display.flip()
            
    run_game()