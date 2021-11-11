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
    from dolibe2 import *
    def chekupdown_fleet_duraction(ai_settings,aliens):

        ai_settings.fleet_direction *= -1
        ai_settings.alien_speed_factor += 0.01

    def chekupdown_fleet_edges(ai_settings,aliens):
        for alien in aliens.sprites():
            if alien.chek_edges():
                chekupdown_fleet_duraction(ai_settings,aliens)
                break

except ConnectionRefusedError:
    print('please run again')

else:
    images = ['cat1.gif','cat2.gif','tree.gif','tree.gif']
    ch = 1000
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 10
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 2
            self.bullet_color = 60,60,60
            self.bullet_width = 100
            self.bullet_height = 106
            self.bullet_allowed =  3
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
            self.y -= self.speed_factor
            self.rect.y = self.y
            

        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
            
        
    class Ship():
        def __init__(self,ai_settings,screen):
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
        def __init__(self,ai_settings,screen):
            super(Alien, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            
            

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

            if let == 2:
                self.x -= 10
            if let == 3:
                self.x += 10

                
            self.rect.y = self.y
            self.rect.x = self.x
            if self.rect.x <= 0:
                self.x = self.ai_settings.screen_width /2
            if self.rect.x >= self.ai_settings.screen_width:
                self.x = self.ai_settings.screen_width /2
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
    def run_game2():
        global ch
        ch = 10000
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()

        alienbullets = Group()
        
        alien = Alien(ai_settings,screen,alienbullets,alienBullet)
        aliens.add(alien)
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
                    if event.key == pygame.K_b:
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        
                        ship.movin_right = True


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True


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
  
        
            bullets.update(bullets,aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            
                          #print('you lose')
            #break
            ship.blitme()
            alien.blitme()
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            bullets.update(bullets,aliens)
            pygame.display.flip()
            if pygame.sprite.spritecollideany(ship,alienbullets):
                print('you lose')
                sys.exit()
            if pygame.sprite.spritecollideany(ship,aliens):
                print('you lose')
                sys.exit()

            ert = randint(-10,80)
            if ert == 0:
                alienbul = alienBullet2(ai_settings,screen,alien,ship)
                alienbullets.add(alienbul)




            for bullet in alienbullets.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    alienbullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            
            for bullet in alienbullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            if pygame.sprite.spritecollideany(alien,bullets):
                ch -= 1
                bullets.remove(bullet)
#                print(ch)
                if ch <= 0:
                    print('you win')
                    break

 #           print(len(alienbullets))
            ship.blitme()
            alien.blitme()
            bullets.draw(screen)
            alienbullets.update(bullets,aliens)
            pygame.display.flip()           
    def run_game():
        global ch
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()

        alienbullets = Group()
        
        libe = [1,3,4,1,3,4,2,0,1,3,1,3,4,4,1,3]
        do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
 
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
                    if event.key == pygame.K_b:
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        
                        ship.movin_right = True


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True


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
#276
            ship.update()
  
    
            bullets.update(bullets,aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
            
                          #print('you lose')
            #break
            ship.blitme()
            
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            bullets.update(bullets,aliens)
        
            if pygame.sprite.spritecollideany(ship,alienbullets):
                print('you lose')
                sys.exit()



            for bullet in alienbullets.copy():
                if bullet.rect.bottom >= ai_settings.screen_height:
                    alienbullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            
            for bullet in alienbullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)

 #           print(len(alienbullets))
            ship.blitme()
        
            bullets.draw(screen)
            aliens.draw(screen)
            alienbullets.update(bullets,aliens)
            pygame.display.flip()
    
    run_game()
