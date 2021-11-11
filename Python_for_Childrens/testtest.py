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
    import threading
    from threading import Timer,Thread
    from time import sleep
    import turtle
    from turtle import *
    import sys 
    import pygame
    import pyjoycon
    from pyjoycon import *

    class MyJoyCon(
            pyjoycon.GyroTrackingJoyCon,
            pyjoycon.ButtonEventJoyCon,
        ): pass

    joycon_id = get_R_ids()
    joycon = MyJoyCon(1406, 8199, '9458cbb41938')
    joycon.get_status()
    def chekupdown_fleet_duraction(ai_settings,aliens):

        ai_settings.fleet_direction *= -1
        ai_settings.alien_speed_factor += 0.01

    def chekupdown_fleet_edges(ai_settings,aliens):
        for alien in aliens.sprites():
            if alien.chek_edges():
                chekupdown_fleet_duraction(ai_settings,aliens)
                break
    brek = 0
    point = 0
    bulsets = 1
    wea = 0

except ConnectionRefusedError:
    print('please run again')

else:
    images = ['cat1.gif','cat2.gif','tree.gif','tree.gif']
    ch = 1000
    class Settings():

        def __init__(self):
            self.screen_width = 1400
            self.bullet_speed_factor = 0.8
            self.screen_height = 1000
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 2
            self.bullet_color = 60,60,60
            self.bullet_width = 6
            self.bullet_height = 20
            self.bullet_allowed =  3
    class Bullet2(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,mx,my):
            super(Bullet2, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            

            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.aliens = aliens
            self.bullets = bullets
            

            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom                                             
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.my = my
            self.mx = mx
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            global ch
            global ch
            if self.mx < self.rect.x:
                self.rect.x -=1
            if self.mx > self.rect.x:
                self.rect.x +=1
            if self.my < self.rect.y:
                self.rect.y -=1
            if self.my > self.rect.y:
                self.rect.y +=1
        def draw_bullet(self):                                                                                           
            pygame.draw.rect(self.screen,self.color,self.rect)    
    
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets):
            super(Bullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            

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
            self.y -= self.speed_factor
            self.rect.y = self.y
            

        def draw_bullet(self):                                                                                           
            pygame.draw.rect(self.screen,self.color,self.rect)    
            
        
    class Ship():
        def __init__(self,ai_settings,screen):
            self.screen = screen
            self.image = pygame.image.load('supercat.gif')

            
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
            self.ch = 1000
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
            self.ty = 1
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def update(self):
            if self.tu == 0:

                if self.ship.rect.x < self.rect.x:
                    self.rect.x -=1
                if self.ship.rect.x > self.rect.x:
                    self.rect.x +=1
                if self.rect.x == self.ship.rect.x:
                    self.tu = 1   
            if self.tu == 1:
                
                
                self.attack+=self.ty
                self.rect.y += self.ty
                if self.attack == 800:
                    self.ty *= -1
                if self.attack == 0:
                    self.ty *= -1
                    self.tu = 0
                

    class Alien2(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Alien2, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            self.ship = ship
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            
            self.image = pygame.image.load("fire.gif")
            
            self.rect = self.image.get_rect()
            
    
            self.go = 0
            self.ship = ship
            self.color = ai_settings.bullet_color
            self.speed_factor = 2
            

        def update(self):
            if self.rect.y <self.ship.rect.y:
                
                self.rect.y += 0.5
            if self.rect.x >self.ship.rect.y:
                
                self.rect.x -= 0.5
            if self.rect.y >self.ship.rect.y:
                
                self.rect.y -= 0.5
            if self.rect.y <self.ship.rect.y:
                
                self.rect.y += 0.5
                    
        def blitme(self):
            
            self.screen.blit(self.image,self.rect)
    class Alien3(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Alien2, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            self.ship = ship
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            
            self.image = pygame.image.load("fire.gif")
            
            self.rect = self.image.get_rect()
            
    
            self.go = 0
            self.ship = ship
            self.color = ai_settings.bullet_color
            self.speed_factor = 2
            

        def update(self):
            if self.rect.y >= self.ai_settings.screen_height or self.rect.y <= self.ai_settings.screen_height:
                
                self.rect.y += 1
            if self.rect.x >self.ship.rect.y:
                
                self.rect.x -= 0.5
        def blitme(self):
            
            self.screen.blit(self.image,self.rect)            
    # class alienBullet(Sprite):
    #     def __init__(self,ai_settings,screen,alien):
    #         super(alienBullet, self).__init__()
    #         self.screen = screen
    #         self.ai_settings = ai_settings
    #         randdom = randint(0,1)
        
    #         if randdom == 0:
    #             self.image = pygame.image.load("leave.gif")
    #         if randdom == 1:
    #             self.image = pygame.image.load("branch.gif")
    #         self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
    #         self.alien_rect = alien.image.get_rect()
    #         self.aliens = alien
    
    #         self.go = 0
    #         self.alien_rect.centerx = self.alien_rect.centerx
    #         self.alien_rect.bottom = self.alien_rect.bottom
    #         self.rect.centerx = alien.rect.centerx
    #         self.rect.top = alien.rect.top
    #         self.rect.bottom = self.rect.bottom
    #         self.y = float(self.rect.y)
    #         self.x = float(self.rect.x)
    #         self.alien_rect.y = float(self.alien_rect.y)
    #         self.alien_rect.x = float(self.alien_rect.x)

    #         self.color = ai_settings.bullet_color
    #         self.speed_factor = ai_settings.bullet_speed_factor
            

    #     def update(self,bullets,aliens):
    #         self.y += 1
    #         self.rect.y = self.y    
    #     def draw_bullet(self):
            
    #         pygame.draw.rect(self.screen,self.color,self.rect)
    class alienBullet(Sprite):
        def __init__(self,ai_settings,screen,alienx,alieny,shipx,shipy):
            super(alienBullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
        
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.shipy = shipy
            self.shipx = shipx

    
            self.go = 0
            self.rect.centerx = alienx
            self.rect.top = alieny
            self.rect.bottom = alieny
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,bullets,aliens):
            if self.shipx < self.rect.x:
                self.rect.x -=1
            if self.shipx > self.rect.x:
                self.rect.x +=1
            if self.shipy < self.rect.y:
                self.rect.y -=1
            if self.shipy > self.rect.y:
                self.rect.y +=1
        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)
    def run_game3():
        global ch,brek,bulsets,wea
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        bullets2 = Group()
        aliens = Group()

        alienbullets = Group()
        alien = Alien3(ai_settings,screen,ship)
        aliens.add(alien)

        mx,my = 0,0
        ch = 200
        

        
        libe = [1,3,4]
        #do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
        bg_color = (20,250,200)
        
        while True:

            if bulsets != 1:
                uytru = 1
                for uytru in range(bulsets):


                    le = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le)
                    le.rect.x+=uytru*10

                    le2 = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le2)
                    le2.rect.x-=uytru*10
                    #.x = alien.x
            if len(aliens) <=0:
                print('you win')
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
                        
                        ship.movin_right = True


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True
                    if event.key == pygame.K_i:
                        wea += 1
                        if wea == 2:
                            wea = 0


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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mox,moy = pygame.mouse.get_pos()
                    mx = mox
                    my = moy
            #ship.update()
  

        #if alien.tu == 3:


            bullets.update(bullets,aliens)
            
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
            isstickbut = joycon.stick_r_btn
            isstickmove=joycon.stick_r
            if isstickmove[1] > 3000:
                
                ship.rect.x += 3
                print('up')
            elif isstickmove[1] < 1000:
                #ship.y += 3
                print('down')
                ship.rect.x -= 3
            
            elif isstickmove[0] > 3000:
                #ship.x += 3
                print('r')
                ship.rect.y += 3
            elif isstickmove[0] < 1000:
                #ship.x -= 3
                print('l')
                ship.rect.y -= 3
            for event_type, status in joycon.events():
                if status == 1:
                    if event_type == 'x':
                        bul = Bullet(ai_settings,screen,ship,alien,bullets)
                        bullets.add(bul)

            if pygame.sprite.spritecollideany(ship,alienbullets):
                print('you lose')
                brek = 1
                sys.exit()
            if 1 == 1:
                ert = randint(-300,1000)
                if ert == 0:
                    alienbullets.empty()
                    alienbul = alienBullet(ai_settings,screen,alien.rect.x,alien.rect.y,ship.rect.x,ship.rect.y)
                    alienbullets.add(alienbul)


            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    alienbullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            for bullet in alienbullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)

            if pygame.sprite.spritecollideany(ship,aliens):
                brek = 1
                sys.exit()


                

 #           print(len(alienbullets))
            ship.blitme()
            alienbullets.update(1,1)
            alienbullets.draw(screen)
            # if alien.rect.y <ship.rect.y:
            #     alien.y += 0.5
            #     alien.rect.y += 0.5
            # if alien.rect.x >ship.rect.y:
            #     alien.x -= 0.5
            #     alien.rect.x -= 0.5
            # if alien.rect.y >ship.rect.y:
            #     print("op")
            #     alien.y -= 0.5
            #     alien.rect.y -= 0.5
            # if alien.rect.y <ship.rect.y:
            #     alien.y += 0.5
            #     alien.rect.y += 0.5
            aliens.draw(screen)
            alien.update()
            alienbullets.update(bullets,aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,False)
            if collisions:
                ch -= 5
                if ch <= 0:
                    print('win')
                    break
            pygame.display.flip()
    def run_game2():
        global ch,brek,bulsets,wea
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        bullets2 = Group()
        aliens = Group()

        alienbullets = Group()
        alien = Alien2(ai_settings,screen,ship)
        aliens.add(alien)

        mx,my = 0,0
        ch = 100
        

        
        libe = [1,3,4]
        #do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
        bg_color = (20,250,200)
        
        while True:

            if bulsets != 1:
                uytru = 1
                for uytru in range(bulsets):


                    le = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le)
                    le.rect.x+=uytru*10

                    le2 = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le2)
                    le2.rect.x-=uytru*10
                    #.x = alien.x
            if len(aliens) <=0:
                print('you win')
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
                        
                        ship.movin_right = True


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True
                    if event.key == pygame.K_i:
                        wea += 1
                        if wea == 2:
                            wea = 0


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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mox,moy = pygame.mouse.get_pos()
                    mx = mox
                    my = moy
            #ship.update()
  

        #if alien.tu == 3:


            bullets.update(bullets,aliens)
            
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
            isstickbut = joycon.stick_r_btn
            isstickmove=joycon.stick_r
            if isstickmove[1] > 2000:
                
                ship.rect.x += 3
                print('up')
            elif isstickmove[1] < 1000:
                #ship.y += 3
             #   print('down')
                ship.rect.x -= 3
            
            elif isstickmove[0] > 2000:
                #ship.x += 3
            #    print('r')
                ship.rect.y += 3
            elif isstickmove[0] < 1000:
                #ship.x -= 3
            
                ship.rect.y -= 3
            for event_type, status in joycon.events():
                if status == 1:
                    if event_type == 'x':
                        bul = Bullet(ai_settings,screen,ship,alien,bullets)
                        bullets.add(bul)

            if pygame.sprite.spritecollideany(ship,alienbullets):
                print('you lose')
                brek = 1
                sys.exit()
            if 1 == 1:
                ert = randint(-300,1000)
                if ert == 0:
                    alienbullets.empty()
                    alienbul = alienBullet(ai_settings,screen,alien.rect.x,alien.rect.y,ship.rect.x,ship.rect.y)
                    alienbullets.add(alienbul)


            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    alienbullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            for bullet in alienbullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)

            if pygame.sprite.spritecollideany(ship,aliens):
                brek = 1
                sys.exit()


                

 #           print(len(alienbullets))
            ship.blitme()
            alienbullets.update(1,1)
            alienbullets.draw(screen)
            # if alien.rect.y <ship.rect.y:
            #     alien.y += 0.5
            #     alien.rect.y += 0.5
            # if alien.rect.x >ship.rect.y:
            #     alien.x -= 0.5
            #     alien.rect.x -= 0.5
            # if alien.rect.y >ship.rect.y:
            #     print("op")
            #     alien.y -= 0.5
            #     alien.rect.y -= 0.5
            # if alien.rect.y <ship.rect.y:
            #     alien.y += 0.5
            #     alien.rect.y += 0.5
            aliens.draw(screen)
            alien.update()
            alienbullets.update(bullets,aliens)
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,False)
            if collisions:
                ch -= 5
                if ch <= 0:
                    print('win')
                    break
            pygame.display.flip()
    # def shop():
    #     pygame.init()
    #     ai_settings =Settings()
    #     screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #     pygame.display.set_caption('Alien Invasion')
    #     ship = Ship(ai_settings,screen)
    #     bullets = Group()
    #     bullets.add(ship)
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 mouse_x,mouse_y = pygame.mouse.get_pos()
    #                 for alien in bullets.sprites():
                        

            screen.fill(ai_settings.bg_color)
    def run_game():
        global ch,brek,bulsets,wea
        ch = 50
        pygame.init()
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        ship2 = Ship(ai_settings,screen)
        bullets = Group()
        bullets2 = Group()
        aliens = Group()

        alienbullets = Group()
        alien = Alien(ai_settings,screen,alienbullets,alienBullet,ship)
        aliens.add(alien)
        pygame.time.wait(int(1000/60))

    #for event_type, status in joycon.events():
    #    print("ButtonEventJoyCon:")
    #    print(event_type, status)
        isstickbut = joycon.stick_r_btn
        isstickmove=joycon.stick_r
        if isstickmove[1] > 2000:
            print('up')
        elif isstickmove[1] < 2000:
            print('down')
        else:
            print('idfujfeg')
        if isstickmove[0] > 2000:
            print('right')
        elif isstickmove[0] < 2000:
            print("left")
        else:
            print('idfujfeg')
        libe = [1,3,4]
        mx,my = 0,0
        #do_liberint(ship,Alien,aliens,ai_settings,screen,libe,'robot.gif','supercat.gif','fire.gif',pygame)
        bg_color = (20,250,200)
        aliens.add(alien)
        while True:
                


                #if wea == 1:

                    
            # if bulsets != 1:
                
            #     for uytru in range(bulsets):


            #         le = Bullet(ai_settings,screen,ship,aliens,bullets)
            #         bullets.add(le)
            #         le.rect.x+=uytru*10

            #         le2 = Bullet(ai_settings,screen,ship,aliens,bullets)
            #         bullets.add(le2)
            #         le2.rect.x-=uytru*10

            if bulsets != 1:
                
                for uytru in range(bulsets):


                    le = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le)
                    le.rect.x+=uytru*10

                    le2 = Bullet(ai_settings,screen,ship,aliens,bullets)
                    bullets.add(le2)
                    le2.rect.x-=uytru*10

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
                    if event.key == pygame.K_i:
                        wea += 1
                        if wea == 2:
                            wea = 0

                        
                        


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
            isstickbut = joycon.stick_r_btn
            isstickmove=joycon.stick_r
            if isstickmove[1] > 2000:
                
                ship.rect.x += 3
                print('up')
            elif isstickmove[1] < 1000:
                #ship.y += 3
                print('down')
                ship.rect.x -= 3
            
            elif isstickmove[0] > 3000:
                #ship.x += 3
                print('r')
                ship.rect.y += 3
            elif isstickmove[0] < 1000:
                #ship.x -= 3
                print('l')
                ship.rect.y -= 3
            for event_type, status in joycon.events():
                if status == 1:
                    if event_type == 'x':
                        bul = Bullet(ai_settings,screen,ship,alien,bullets)
                        bullets.add(bul)



#             isstickmove=joycon.stick_l
#             if isstickmove[1] > 3000:
                
#                 ship2.rect.x += 3
#                 print('up')
#             elif isstickmove[1] < 1000:
#                 #ship.y += 3
#                 print('down')
#                 ship2.rect.x -= 3
            
#             elif isstickmove[0] > 3000:
#                 #ship.x += 3
#                 print('r')
#                 ship2.rect.y += 3
#             elif isstickmove[0] < 1000:
#                 #ship.x -= 3
#                 print('l')
#                 ship2.rect.y -= 3
# #276
#             #ship.update()
  
            alien.update()
        #if alien.tu == 3:


            bullets.update(bullets,aliens)
            
                          #print('you lose')
            #break
            ship.blitme()
            ship2.blitme()
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
            if pygame.sprite.spritecollideany(ship,alienbullets):
                print('you lose')
                sys.exit()
            ert = randint(-10,90)
            # if ert == 0:
            #     alienbul = alienBullet(ai_settings,screen,alien)
            #     alienbullets.add(alienbul)



            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    alienbullets.remove(bullet)
            for bullet in bullets2.copy():
                if bullet.rect.x == bullet.mx and bullet.rect.y == bullet.my:
                    bullets.remove(bullet)
                    bullets2.remove(bullet)
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            if pygame.sprite.spritecollideany(alien,bullets):
                ch -= 10
                bullets.remove(bullet)
#                print(ch)
                if ch <= 0:
                    print('you win')
                    break
            if pygame.sprite.spritecollideany(ship,aliens):
                brek = 1
                print('lose')
                sys.exit()
            collisions = pygame.sprite.groupcollide(bullets,aliens,True,False)
#            collisions = pygame.sprite.groupcollide(bullets,alienbullets,True,True)

 #           print(len(alienbullets))
            ship.blitme()
            alien.blitme()

            alienbullets.update(bullets,aliens)
            
            pygame.display.flip()
#    while True:
        
        # shop()
 #       while True:

            
run_game()
            #if brek == 1:
             #   break
            #sleep(0.5)
run_game2()
            #if brek == 1:
             #   break
        #brek = 0