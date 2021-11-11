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
    yt = 0
        

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
    ch = 100000
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 10
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 2
            self.bullet_color = 103.92,103.92,103.92
            self.bullet_width = 20
            self.bullet_height = 20
            self.bullet_allowed =  3
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,mx,my):
            super(Bullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            

            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.aliens = aliens
            self.bullets = bullets
            

            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = ship.rect.bottom                                             
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.my = my
            self.mx = mx
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self):
            global ch
            global ch
            if self.mx < self.rect.x:
                self.rect.x -= 1
            if self.mx > self.rect.x:
                self.rect.x += 1
            if self.my < self.rect.y:
                self.rect.y -= 1
            if self.my > self.rect.y:
                self.rect.y += 1
        def draw_bullet(self):                                                                                           
            pygame.draw.rect(self.screen,self.color,self.rect)    
      
    class bg(Sprite):
        def __init__(self,ai_settings,screen):
            self.screen = screen

            self.image = pygame.image.load("screenshot.jpg")
            self.rect = self.image.get_rect()

        def update(self):
            pass
        def blitme(self):
            self.screen.blit(self.image,self.rect)            
        
    class Ship(Sprite):
        def __init__(self,ai_settings,screen):
            super(Ship, self).__init__()
            self.screen = screen

            self.image = pygame.image.load("warrior.gif")
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
                self.senter += 2

            if self.movin_left and self.rect.left > 0:
                #self.rect.centerx -= 1
                self.senter -= 2
            if self.movin_up and self.rect.y > 0:
                self.rect.bottom -= 2
            if self.movin_down and self.rect.y < 800:
                self.rect.bottom += 2
            self.rect.centerx = self.senter
        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Alien(Sprite):
        def __init__(self,ai_settings,screen,alienBullets,alienBullet,ship):
            super(Alien, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.ship = ship
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("fire.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)
        
            self.x = float(self.rect.x)
            self.tu = 0
            self.attack = 0 
            self.ty = 3
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def update(self):
            if self.tu == 0:

                if self.ship.rect.x < self.rect.x:
                    self.rect.x -=3
                if self.ship.rect.x > self.rect.x:
                    self.rect.x +=3
                if self.rect.x == self.ship.rect.x:
                    self.tu = 1   
            if self.tu == 1:
                
                
                self.attack+=self.ty
                self.rect.y += self.ty
                if self.attack == 103.920:
                    self.ty *= -1
                if self.attack == 0:
                    self.ty *= -1
                    self.tu = 0
                

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
        def __init__(self,ai_settings,screen,alien,ship):
            super(alienBullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
        
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.ship = ship
    
            self.go = 0
            self.rect.centerx = alien.rect.centerx
            self.rect.top = alien.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            if self.ship.rect.x < self.rect.x:
                self.rect.x -=2
            if self.ship.rect.x > self.rect.x:
                self.rect.x +=2
            if self.ship.rect.y < self.rect.y:
                self.rect.y -=2
            if self.ship.rect.y > self.rect.y:
                self.rect.y +=2
        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
        
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.score = 0
        self.high_score = 0
        self.sc = (200,200,200)
        self.tc = (10,300,100)
        self.font = pygame.font.SysFont(None,48)
        self.prep_high_score()
    
        
    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
    def prep_high_score(self):
        high_score = int(round(self.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        # self.score_image = self.font.render(high_score,True,self.tc,self.sc)
        # self.score_rect = self.score_image.get_rect()
    
        # self.score_rect.centerx = self.screen_rect.centerx
        # self.score_rect.top = self.score_rect.top

    def run_game():
        global ch,yt
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        aliens = Group()

        alienbullets = Group()
        alien = Alien(ai_settings,screen,alienbullets,alienBullet,ship)
        aliens.add(alien)
        
        libe = [1,3,4]
        #do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
        bg_color = (20,250,200)
        aliens.add(alien)
        ship2 = Ship(ai_settings,screen)
        ship2.rect.x = 2
        ty = 0
        ship2.rect.y = 2
        imga = bg(ai_settings,screen)
        ship.rect.x = 1112
        ship.rect.y = 668
        items = Group()
        turrels = Group()
        bullets2 = Group()

        item = Ship(ai_settings,screen)
        item.rect.y = randint(100,ai_settings.screen_height-100)
        item.rect.x = randint(100,ai_settings.screen_width-100)
        items.add(item)
        bullets3 = Group()
        bullets4 = Group()
        turrels2 = Group()
        
        while True:
            turrels.empty()
            turrels2.empty()
            ty = 0
            print('1p')
            ty = randint(1,3)
            print(ty)
            tre = randint(0,10)


            ty = 0
            print('1p')
            ty = randint(1,3)
            print(ty)
            
            while True:
                if ty == 100:
                    break

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
                            if len(bullets) < 2:
                                ship.rect.x+=74
                            ty -= 1

                        if event.key == pygame.K_LEFT:
                            if len(bullets) < 2:
                                ship.rect.x-=74
                            ty -= 1

                        if event.key == pygame.K_UP:
                            if len(bullets) < 2:
                                ship.rect.y-=74
                            ty -= 1


                        if event.key == pygame.K_DOWN:
                            if len(bullets) < 2:
                                ship.rect.y+=74
                            ty -= 1
                        if event.key == pygame.K_RALT:
                            if len(bullets) < 1:
                                bul = Bullet(ai_settings,screen,ship,aliens,bullets,ship2.rect.x,ship2.rect.y)
                                bullets.add(bul)
                        if event.key == pygame.K_TAB:
                            ty = 0

                    
                #for event in pygame.event.get():

                        if event.key == pygame.K_1:
                            first = randint(0,220)
                            second = randint(0,220)
                            three = randint(0,220)
                            ai_settings.bg_color = (first,second,three)
                        if event.key == pygame.K_b:
                            sys.exit()
                        if event.key == pygame.K_d:
                            if len(bullets2) < 2:
                                ship2.rect.x+=74
                            ty -= 1

                        if event.key == pygame.K_a:
                            if len(bullets2) < 2:
                                ship2.rect.x-=74
                            ty -= 1
                        if event.key == pygame.K_w:
                            if len(bullets2) < 2:
                                ship2.rect.y-=74
                            ty -= 1

                        if event.key == pygame.K_s:
                            if len(bullets2) < 2:
                                ship2.rect.y+=74
                            ty -= 1
                        if event.key == pygame.K_e:
                            if len(bullets2) < 1 and ship2.rect.y <= ship.rect.y+540 and ship2.rect.x <= ship.rect.x+540 and ship2.rect.y >= ship.rect.y-540 and ship2.rect.x >= ship.rect.x-540:
                                
                                bul = Bullet(ai_settings,screen,ship2,aliens,bullets,ship.rect.x,ship.rect.y)
                                bullets2.add(bul)
                        if event.key == pygame.K_q:
                            if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

                                print('2p win')
                                sys.exit() 
                                ty -= 1
                    
                        if event.key == pygame.K_PAGEDOWN:
                            if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

                                print('1p win')
                                sys.exit()

                        if event.key == pygame.K_DELETE:
                            
                            if len(bullets) < 1 and ship2.rect.y <= ship.rect.y+540 and ship2.rect.x <= ship.rect.x+540 and ship2.rect.y >= ship.rect.y-540 and ship2.rect.x >= ship.rect.x-540:
                                
                                bul = Bullet(ai_settings,screen,ship,aliens,bullets,ship2.rect.x,ship2.rect.y)
                                bullets.add(bul)
                            # elif ship2.rect.y <= ship.rect.y-=103.92 and ship2.rect.x >= ship.rect.x-=103.92:

                            #     print('1p win') 
                            #     ty = 1

                        if event.key == pygame.K_TAB:
                            ty = 0
    #276         print(len(alienbullets))
                # screen.fill(ai_settings.bg_color)
                imga.blitme()
                for bullet in bullets.sprites():
                    
                    bullet.draw_bullet()
                        
                    first = randint(0,200)
                    second = randint(0,200)
                    three = randint(0,200)
                    ai_settings.bullet_color = (first,second,three)
                for bullet in bullets2.sprites():
                    
                    bullet.draw_bullet()
                        
                    first = randint(0,200)
                    second = randint(0,200)
                    three = randint(0,200)
                    ai_settings.bullet_color = (first,second,three)
                for bullet in bullets2.copy():
                    if bullet.rect.y == bullet.my and  bullet.rect.x == bullet.mx:
                        bullets2.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx+1:
                        bullets2.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx-1:
                        bullets2.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx+1:
                        bullets2.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx-1:
                        bullets2.remove(bullet)
                for bullet in bullets.copy():
            
                    if bullet.rect.y == bullet.my and  bullet.rect.x == bullet.mx:
                        bullets.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx+1:
                        bullets.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx-1:
                        bullets.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx+1:
                        bullets.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx-1:
                        bullets.remove(bullet)
                        
                if pygame.sprite.spritecollideany(ship,bullets2):
                    print('2p win')
                    sys.exit()
                if pygame.sprite.spritecollideany(ship2,bullets):
                    print('1p win')
                    sys.exit()
                for bullet in bullets4.sprites():
                    
                    bullet.draw_bullet()
                        
                    first = randint(0,200)
                    second = randint(0,200)
                    three = randint(0,200)
                    ai_settings.bullet_color = (first,second,three)
                for bullet in bullets3.sprites():
                    
                    bullet.draw_bullet()
                        
                    first = randint(0,200)
                    second = randint(0,200)
                    three = randint(0,200)
                    ai_settings.bullet_color = (first,second,three)
                for bullet in bullets4.copy():
                    if bullet.rect.y == bullet.my and  bullet.rect.x == bullet.mx:
                        bullets4.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx+1:
                        bullets4.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx-1:
                        bullets4.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx+1:
                        bullets4.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx-1:
                        bullets4.remove(bullet)
                for bullet in bullets3.copy():
            
                    if bullet.rect.y == bullet.my and  bullet.rect.x == bullet.mx:
                        bullets3.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx+1:
                        bullets3.remove(bullet)
                    if bullet.rect.y == bullet.my+1 and  bullet.rect.x == bullet.mx-1:
                        bullets3.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx+1:
                        bullets3.remove(bullet)
                    if bullet.rect.y == bullet.my-1 and  bullet.rect.x == bullet.mx-1:
                        bullets3.remove(bullet)
                        
                if pygame.sprite.spritecollideany(ship,bullets4):
                    print('2p win')
                if pygame.sprite.spritecollideany(ship2,bullets3):
                    print('1p win')

                ship.blitme()
                items.draw(screen)
                bullets2.update()
                bullets.update()
                bullets3.update()
                bullets4.update()
                ship2.blitme()
                turrels.draw(screen)
                tre = randint(0,100)

                if pygame.sprite.spritecollideany(ship,items):
                    ty += 5
                    item2 = Ship(ai_settings,screen)
                    item2.rect.y = item.rect.y
                    item2.rect.x = item.rect.x

                    item.rect.y = randint(100,ai_settings.screen_height-100)
                    item.rect.x = randint(100,ai_settings.screen_width-100)
 
                    
                    # item.rect.y = randint(100,ai_settings.screen_height-100)
                    # item.rect.x = randint(100,ai_settings.screen_width-100)

                    turrels.add(item2)
                if pygame.sprite.spritecollideany(ship2,items):
                    ty += 5
                    item2 = Ship(ai_settings,screen)
                    item2.rect.y = item.rect.y
                    item2.rect.x = item.rect.x
                    item.rect.y = randint(100,ai_settings.screen_height-100)
                    item.rect.x = randint(100,ai_settings.screen_width-100)
 
                    
                    # item.rect.y = randint(100,ai_settings.screen_height-100)
                    # item.rect.x = randint(100,ai_settings.screen_width-100)

                    turrels2.add(item2)
                    item2.image = pygame.image.load('supercat.gif')
                turrels.draw(screen)
                turrels2.draw(screen)
                





                pygame.display.flip()
            ty = 0
            print('2p')
            ty = randint(1,3)
            print(ty)
            while True:
                if ty <= 0:
                    break
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
                            
                            ship2.rect.x+=74
                            ty -= 1

                        if event.key == pygame.K_LEFT:
                            ship2.rect.x-=74
                            ty -= 1
                        if event.key == pygame.K_UP:
                            
                            ship2.rect.y-=74
                            ty -= 1

                        if event.key == pygame.K_DOWN:
                            ship2.rect.y+=74
                            ty -= 1
                        if event.key == pygame.K_g:
                            if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

                                print('2p win') 
                                ty -= 1
                                
                            # elif ship2.rect.y <= ship.rect.y-=103.92 and ship2.rect.x >= ship.rect.x-=103.92:

                            #     print('1p win') 
                            #     ty = 1
                            else:
                                print('you cant do it')
                        if event.key == pygame.K_TAB:
                            ty = 0

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
    #276         print(len(alienbullets))
                imga.blitme()
                ship.blitme()
                ship2.blitme()

                items.empty()

                


                pygame.display.flip()
    # def run_game2():
    #     global ch,yt
    #     pygame.init()
    #     ai_settings =Settings()
    #     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #     pygame.display.set_caption('Alien Invasion')
    #     ship = Ship(ai_settings,screen)
    #     bullets = Group()
    #     aliens = Group()

    #     alienbullets = Group()
    #     alien = Alien(ai_settings,screen,alienbullets,alienBullet,ship)
    #     aliens.add(alien)
        
    #     libe = [1,3,4]
    #     #do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
    #     bg_color = (20,250,200)
    #     aliens.add(alien)
    #     ship2 = Ship(ai_settings,screen)
    #     ship2.rect.x = 2
    #     ty = 0
    #     ship2.rect.y = 2

    #     imga = bg(ai_settings,screen)
    #     ship.rect.x = 1112
    #     ship.rect.y = 668
    #     items = Group()
        


        
    #     while True:
    #         tre = randint(0,10)
    #         print(uyty)
    #         if tre == uyty:
    #             print('item')
    #             item = Ship(ai_settings,screen)
    #             item.rect.y = randint(100,ai_settings.screen_height-100)
    #             item.rect.x = randint(100,ai_settings.screen_width-100)
    #             items.add(item)
    #         ty = 0
    #         print('1p')
    #         ty = randint(1,3)
    #         print(ty)
            
    #         while True:
    #             if ty <= 0:
    #                 break

    #             for event in pygame.event.get():

                    
    #             #for event in pygame.event.get():

    #                 if event.type == pygame.KEYDOWN:
    #                     if event.key == pygame.K_1:
    #                         first = randint(0,220)
    #                         second = randint(0,220)
    #                         three = randint(0,220)
    #                         ai_settings.bg_color = (first,second,three)
    #                     if event.key == pygame.K_b:
    #                         sys.exit()
    #                     if event.key == pygame.K_RIGHT:
                            
    #                         ship.rect.x+=74
    #                         ty -= 1

    #                     if event.key == pygame.K_LEFT:
    #                         ship.rect.x-=74
    #                         ty -= 1

    #                     if event.key == pygame.K_UP:
                            
    #                         ship.rect.y-=74
    #                         ty -= 1


    #                     if event.key == pygame.K_DOWN:
    #                         ship.rect.y+=74
    #                         ty -= 1
    #                     if event.key == pygame.K_g:
    #                         if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

    #                             print('1p win') 
    #                             ty -= 1
    #                         # elif ship2.rect.y <= ship.rect.y-=103.92 and ship2.rect.x >= ship.rect.x-=103.92:

    #                         #     print('1p win') 
    #                         #     ty = 1
    #                         else:
    #                             print('you cant do it')
    #                     if event.key == pygame.K_TAB:
    #                         ty = 0
    #                 elif event.type == pygame.KEYUP:
    #                     if event.key == pygame.K_RIGHT:
    #                         ship.movin_right = False               
    #                     if event.key == pygame.K_LEFT:               
    #                         ship.movin_left = False               
    #                     if event.key == pygame.K_UP:               
                            
    #                         ship.movin_up = False
                        
    #                     if event.key == pygame.K_2:
    #                         ship.image = pygame.image.load(random.choice(images))
    #                     if event.key == pygame.K_DOWN:
    #                         ship.movin_down = False
        

                    
    #             #for event in pygame.event.get():

    #     #            if event.type == pygame.KEYDOWN:
    #                     if event.key == pygame.K_1:
    #                         first = randint(0,220)
    #                         second = randint(0,220)
    #                         three = randint(0,220)
    #                         ai_settings.bg_color = (first,second,three)
    #                     if event.key == pygame.K_b:
    #                         sys.exit()
    #                     if event.key == pygame.K_RIGHT:
                            
    #                         ship2.rect.x+=74
    #                         ty -= 1

    #                     if event.key == pygame.K_LEFT:
    #                         ship2.rect.x-=74
    #                         ty -= 1
    #                     if event.key == pygame.K_UP:
                            
    #                         ship2.rect.y-=74
    #                         ty -= 1

    #                     if event.key == pygame.K_DOWN:
    #                         ship2.rect.y+=74
    #                         ty -= 1
    #                     if event.key == pygame.K_g:
    #                         if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

    #                             print('2p win') 
    #                             ty -= 1
                                
    #                         # elif ship2.rect.y <= ship.rect.y-=103.92 and ship2.rect.x >= ship.rect.x-=103.92:

    #                         #     print('1p win') 
    #                         #     ty = 1
    #                         else:
    #                             print('you cant do it')
    #                     if event.key == pygame.K_TAB:
    #                         ty = 0
    # #276         print(len(alienbullets))
    #             # screen.fill(ai_settings.bg_color)
    #             imga.blitme()
    #             ship.blitme()

    #             ship2.blitme()
    #             if pygame.sprite.spritecollideany(ship,aliens):
    #                 print('2p win')
    #             items.draw(screen)
    #             fires.draw(screen)
    #             items.draw(screen)

                
    #             tre = randint(0,1000)

    #             pygame.display.flip()
    #         ty = 0
    #         print('2p')
    #         ty = randint(1,3)
    #         print(ty)
    #         while True: 
    #             if ty <= 0:
    #                 break
    #             for event in pygame.event.get():

                    
    #             #for event in pygame.event.get():

    #                 if event.type == pygame.KEYDOWN:
    #                     if event.key == pygame.K_1:
    #                         first = randint(0,220)
    #                         second = randint(0,220)
    #                         three = randint(0,220)
    #                         ai_settings.bg_color = (first,second,three)
    #                     if event.key == pygame.K_b:
    #                         sys.exit()
    #                     if event.key == pygame.K_RIGHT:
                            
    #                         ship2.rect.x+=74
    #                         ty -= 1

    #                     if event.key == pygame.K_LEFT:
    #                         ship2.rect.x-=74
    #                         ty -= 1
    #                     if event.key == pygame.K_UP:
                            
    #                         ship2.rect.y-=74
    #                         ty -= 1

    #                     if event.key == pygame.K_DOWN:
    #                         ship2.rect.y+=74
    #                         ty -= 1
    #                     if event.key == pygame.K_g:
    #                         if ship2.rect.y <= ship.rect.y+180 and ship2.rect.x <= ship.rect.x+180 and ship2.rect.y >= ship.rect.y-180 and ship2.rect.x >= ship.rect.x-180:

    #                             print('2p win') 
    #                             ty -= 1
                                
    #                         # elif ship2.rect.y <= ship.rect.y-=103.92 and ship2.rect.x >= ship.rect.x-=103.92:

    #                         #     print('1p win') 
    #                         #     ty = 1
    #                         else:
    #                             print('you cant do it')
    #                     if event.key == pygame.K_TAB:
    #                         ty = 0

    #                 elif event.type == pygame.KEYUP:
    #                     if event.key == pygame.K_RIGHT:
    #                         ship.movin_right = False               
    #                     if event.key == pygame.K_LEFT:               
    #                         ship.movin_left = False               
    #                     if event.key == pygame.K_UP:               
                            
    #                         ship.movin_up = False
                        
    #                     if event.key == pygame.K_2:
    #                         ship.image = pygame.image.load(random.choice(images))
    #                     if event.key == pygame.K_DOWN:
    #                         ship.movin_down = False
                    
    # #276         print(len(alienbullets))
    #             imga.blitme()
    #             ship.blitme()
    #             ship2.blitme()
    #             items.draw(screen)

    #             if pygame.sprite.spritecollideany(ship2,aliens):
    #                 print('1p win')



                

    #             pygame.display.flip()
    re = '1'
    if re == '1':
        run_game()
    # if re == '2':
    #     run_game2()



#seseesseeeesessees