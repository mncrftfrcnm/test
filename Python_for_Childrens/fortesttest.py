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
    import sys 
    from PIL import Image
    from dolibe import *
    from dolibe2 import *
    db = 0
    ch = 20
    wea = 0
    t = 0
    def chekupdown_fleet_edges(ai_settings,aliens):
        for alien in aliens.sprites():
            if alien.chek_edges():
                alien.dur *= -1 
                #alien.x+=1
                alien.rect.x = alien.x
                break

except ConnectionRefusedError:
    print('please run again')

else:
    images = ['cat1.gif','cat2.gif','robot.gif','robot.gif']
    
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 10
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 1
            self.bullet_color = 60,60,60
            self.bullet_width = 100
            self.bullet_height = 106
            self.bullet_allowed =  3
            self.fleet_diraction = -1
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien,turn):
            super(Bullet, self).__init__()
            self.trex = 1
            self.trey = 1

            self.screen = screen
            self.ai_settings = ai_settings
        
                
                #if randdom == 0:
            self.image = pygame.image.load("leave.gif")
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
                
            self.image = pygame.image.load("branch.gif")
        
            self.alien_rect = alien.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
                
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = ship.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)
                
            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            self.turn = turn
                

        def update(self):
            global ch
            global ch
            if self.turn == 0:
                self.x += 1
                self.rect.x = self.x
            if self.turn == 1:
                self.x -= 1
                self.rect.x = self.x
            # if self.turn == 0:
            #     self.x += 1
            #     self.rect.x = self.x
            # if self.turn == 0:
            #     self.x += 1
            #     self.rect.x = self.x
            

        def draw_bullet(self):
                
            self.screen.blit(self.image,self.rect)
                        
    class Ship(Sprite):
        def __init__(self,ai_settings,screen):
            super(Ship,self).__init__()
            self.screen = screen
            self.tre = 0

            self.image = pygame.image.load("robot.gif")
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
            self.y = float(self.rect.y)
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom


        def update(self):
            # global 
            # ai_settings = Settings()
            # screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
            if self.movin_right and self.rect.right < self.screen_rect.right:
                #self.rect.centerx += 1
                self.senter += self.ai_settings.ship_speed_factor
     
                #self.rect.centerx += 1
            if self.movin_left and self.rect.left > 0:
                #self.rect.centerx -= 1
                self.senter -= self.ai_settings.ship_speed_factor
            if self.movin_up:
                self.rect.bottom -= 1
            if self.movin_down:
                self.rect.bottom += 1
            self.rect.centerx = self.senter
            self.tre = 0
        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Button(Sprite):
        def __init__(self,ai_settings,screen):
            super(Button,self).__init__()
            self.screen = screen
            self.tre = 0

            self.image = pygame.image.load("supercat.gif")
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
            self.y = float(self.rect.y)
            self.screen_rect = screen.get_rect()
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom


        def update(self):
            # global 
            pass
        def blitme(self):
            self.screen.blit(self.image,self.rect)

    class Ant_men(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Ant_men, self).__init__()
            self.ship = ship
            self.ai_settings = ai_settings
            self.screen = screen
            self.dur = ai_settings.fleet_diraction
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("block.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)
            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            self.f = 0
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def chek_edges(self):
            if self.f >= 500:
                return True
                print("P")
            if self.f <= 0:
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
    class Fire_man(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Alen, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.dur = ai_settings.fleet_diraction
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("tree.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)

            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            self.f = 0
            self.ship = ship
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def chek_edges(self):
            if self.f >= 500:
                return True
                print("P")
            if self.f <= 0:
                return True


        def update(self):
            pass
    class Sniff(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Sniff, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.ship = ship

            self.image = pygame.image.load("fire.gif")
            self.rect = self.image.get_rect()
            self.rect2 = self.ship.image.get_rect()
            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.x = float(self.rect.x)
            self.y = float(self.rect.y)
            #self.speed = self.ai_settings.alien_speed_factor

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
    class Alien(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Alien, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.dur = ai_settings.fleet_diraction
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("tree.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)

            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            self.f = 0
            self.ship = ship
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def chek_edges(self):
            if self.f >= 500:
                return True
                print("P")
            if self.f <= 0:
                return True


        def update(self):
            pass
    class Stynki_man(Sprite):
        def __init__(self,ai_settings,screen,ship):
            super(Stynki_man, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.dur = ai_settings.fleet_diraction
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load("tree.gif")
            self.rect = self.image.get_rect()

            
            
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height
            self.y = float(self.rect.y)

            self.rect.x = self.rect.width
            self.x = float(self.rect.x)
            self.f = 0
            self.x = ai_settings.screen_width-300
            self.y = 657
            self.rect.x = self.x
            self.rect.y = self.y
            self.ship = ship
        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def chek_edges(self):
            if self.f >= 500:
                return True
                print("P")
            if self.f <= 0:
                return True


        def update(self):
            pass


         
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
    class Bllet(Sprite):
        def __init__(self,ai_settings,screen,alien):
            super(Bllet, self).__init__()
            self.trex = 1
            self.trey = 1

            self.screen = screen
            self.ai_settings = ai_settings
        
                
                #if randdom == 0:
            self.image = pygame.image.load("leave.gif")
            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
                
            self.image = pygame.image.load("strawberry.gif")
        
            self.alien_rect = alien.image.get_rect()
                
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)
                
                

        def update(self):
            global ch
            global ch
            pass
        def draw_bullet(self):
                
            self.screen.blit(self.image,self.rect)
#     def run_game_3():
#         global ch,dobollet,db,wea
#         pygame.init()
#         turn = 0
    

#         fg = 1
#         pfg = 1
        
#         i = 0
#         snifs = Group()
#         j = False
#         sit = False
        
#         ai_settings =Settings()
#         screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#         pygame.display.set_caption('Alien Invasion')
#         ship = Ship(ai_settings,screen)
#         ship.image = pygame.image.load('robot.gif')
#         ship.x = 0
#         ship.y = 0
        
#         bullets = Group()
    
#         ships = Group()

#         ships.add(ship)
#         while True:
#             if pygame.sprite.spritecollideany(ship,snifs):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
#             rand = randint(-1000,1000)
            
#             if j == True and i == 0:
                
#                 ert = 0
#                 ship.y -= 1*pfg
#                 fg += 1*pfg
#                 #print(ship.y)
#                 ship.rect.y = ship.y
#                 if fg == 190:
#                     pfg*=-1
#                 if fg == 0:
#                     i = 0
#                     pfg*=-1
#                     j = False
                
#                 scr = screen.get_rect()
#             if j == False and ship.rect.y < 752:
#                 ship.y+=1
#                 ship.rect.y = ship.y
#         #    ship.y+= 1
#          #   ship.rect.y = ship.y
#             if dobollet == True:
#                 new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                 bullets.add(new_bullet)

                


#             for event in pygame.event.get():

                
#             #for event in pygame.event.get():

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         ship.image = pygame.image.load('fire.gif')
#                         uii = 1
#                     if event.key == pygame.K_1:
#                         first = randint(0,220)
#                         second = randint(0,220)
#                         three = randint(0,220)
#                         ai_settings.bg_color = (first,second,three)
#                     if event.key == pygame.K_b:
#                         sys.exit()
#                     if event.key == pygame.K_RIGHT:
                        
#                         ship.movin_right = True
#                         turn = 0


#                     if event.key == pygame.K_LEFT:
#                         ship.movin_left = True
#                         turn = 1

#                     if event.key == pygame.K_DOWN:
#                         sit = True
#                     if event.key == pygame.K_i:
        
#                         if j == False:
#                     #        print("O")
#                             j = True
#                             i = 0
                     
#                     if event.key == pygame.K_v:
#                         if wea == 0:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                         if wea == 1:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 50
#                             new_bullet.rect.y = new_bullet.y
                            
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 0
#                             new_bullet.rect.y = new_bullet.y
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= -50
#                             new_bullet.rect.y = new_bullet.y
                            
#                 elif event.type == pygame.KEYUP:
#                     if event.key == pygame.K_RIGHT:
#                         ship.movin_right = False               
#                     if event.key == pygame.K_LEFT:               
#                         ship.movin_left = False     

#                     if event.key == pygame.K_UP:
                    
#                         ship.image = pygame.image.load('robot.gif')
#                         uii = 0
#                     if event.key == pygame.K_2:
#                         ship.image = pygame.image.load(random.choice(images))
#                     if event.key == pygame.K_DOWN:
#                         sit = False
#                     if event.key == pygame.K_v:
                        
#                         dobollet = False
                    
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if db == 1:

#                         mouse_x,mouse_y = pygame.mouse.get_pos()
#                         bul = Alien(ai_settings,screen,ship)
#                         aliens.add(bul)
#                         bul.rect.x = mouse_x
#     #276
#                         bul.rect.y = mouse_y
# #276
#             ship.update()
  
        
#         #    bullets.update(bullets,aliens)
            
#                           #print('you lose')
#             #break
#             ship.blitme()
#             if uii == 0:
#                 if pygame.sprite.spritecollideany(ship,aliens):
#                     # j = True
#                     # i = 1
                
#                     ship.y-=1
#                     ship.rect.y = ship.y
#             else:
#                 collisions = pygame.sprite.groupcollide(aliens,ships,False,True)
#                 print(len(aliens))

                        
#             # elif :
#             #     j = False
#             #     i = 0

#  #           print(len(alienbullets))
#             for bullet in bullets.copy():
#                 if bullet.rect.x >= ai_settings.screen_width or bullet.rect.x <= 0:
#                     bullets.remove(bullet)
            
#             screen.fill(ai_settings.bg_color)
            
#             for bullet in bullets.sprites():
#                 collisions = pygame.sprite.groupcollide(snifs,bullets,True,True)

#                 collisions = pygame.sprite.groupcollide(bullets,aiens,True,True)
#                 bullet.draw_bullet()
                    
#                 first = randint(0,200)
#                 second = randint(0,200)
#                 three = randint(0,200)
#                 ai_settings.bullet_color = (first,second,three)
#             for ship in ships.sprites():
#                 if pygame.sprite.spritecollideany(ship,sty):
#                     aen.x = randint(0,ai_settings.screen_width)
#                     aen.y = randint(0,ai_settings.screen_height)

#                     alien.rect.x = alien.x
#                     aen.rect.y = alien.y
#                     score += 1
#             tre = randint(-1000,1000)
#             if tre == 0:
#                 sni = Sniff(ai_settings,screen,ship)
#                 snifs.add(sni)
                   
#             bullets.update()
#             ship.blitme()
#             aliens.draw(screen)
            
#             aliens.draw(screen)
            
#             if pygame.sprite.spritecollideany(ant,ships):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
                
        
#             if pygame.sprite.spritecollideany(ant,bullets):
#             #    sys.exit()
#                 #print('your score is',score)
#                 ch -= 1
#                 bullets.empty()
#                 if ch <= 0:
#                     print('you win')
#                     db = 1
#                     break
#             snifs.draw(screen)
#             snifs.update()
#             ant.blitme()
#             ant.update()
#             pygame.display.flip()
            

#     def run_game_3():
#         global ch,dobollet,db,wea
#         pygame.init()
#         turn = 0
    

#         fg = 1
#         pfg = 1
        
#         i = 0
#         snifs = Group()
#         j = False
#         sit = False
        
#         ai_settings =Settings()
#         screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#         pygame.display.set_caption('Alien Invasion')
#         ship = Ship(ai_settings,screen)
#         ship.image = pygame.image.load('robot.gif')
#         ship.x = 0
#         ship.y = 0
        
#         bullets = Group()
    
#         ships = Group()

#         ships.add(ship)
#         while True:
#             if pygame.sprite.spritecollideany(ship,snifs):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
#             rand = randint(-1000,1000)
            
#             if j == True and i == 0:
                
#                 ert = 0
#                 ship.y -= 1*pfg
#                 fg += 1*pfg
#                 #print(ship.y)
#                 ship.rect.y = ship.y
#                 if fg == 190:
#                     pfg*=-1
#                 if fg == 0:
#                     i = 0
#                     pfg*=-1
#                     j = False
                
#                 scr = screen.get_rect()
#             if j == False and ship.rect.y < 752:
#                 ship.y+=1
#                 ship.rect.y = ship.y
#         #    ship.y+= 1
#          #   ship.rect.y = ship.y
#             if dobollet == True:
#                 new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                 bullets.add(new_bullet)

                


#             for event in pygame.event.get():

                
#             #for event in pygame.event.get():

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         ship.image = pygame.image.load('fire.gif')
#                         uii = 1
#                     if event.key == pygame.K_1:
#                         first = randint(0,220)
#                         second = randint(0,220)
#                         three = randint(0,220)
#                         ai_settings.bg_color = (first,second,three)
#                     if event.key == pygame.K_b:
#                         sys.exit()
#                     if event.key == pygame.K_RIGHT:
                        
#                         ship.movin_right = True
#                         turn = 0


#                     if event.key == pygame.K_LEFT:
#                         ship.movin_left = True
#                         turn = 1

#                     if event.key == pygame.K_DOWN:
#                         sit = True
#                     if event.key == pygame.K_i:
        
#                         if j == False:
#                     #        print("O")
#                             j = True
#                             i = 0
                     
#                     if event.key == pygame.K_v:
#                         if wea == 0:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                         if wea == 1:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 50
#                             new_bullet.rect.y = new_bullet.y
                            
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 0
#                             new_bullet.rect.y = new_bullet.y
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= -50
#                             new_bullet.rect.y = new_bullet.y
                            
#                 elif event.type == pygame.KEYUP:
#                     if event.key == pygame.K_RIGHT:
#                         ship.movin_right = False               
#                     if event.key == pygame.K_LEFT:               
#                         ship.movin_left = False     

#                     if event.key == pygame.K_UP:
                    
#                         ship.image = pygame.image.load('robot.gif')
#                         uii = 0
#                     if event.key == pygame.K_2:
#                         ship.image = pygame.image.load(random.choice(images))
#                     if event.key == pygame.K_DOWN:
#                         sit = False
#                     if event.key == pygame.K_v:
                        
#                         dobollet = False
                    
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if db == 1:

#                         mouse_x,mouse_y = pygame.mouse.get_pos()
#                         bul = Alien(ai_settings,screen,ship)
#                         aliens.add(bul)
#                         bul.rect.x = mouse_x
#     #276
#                         bul.rect.y = mouse_y
# #276
#             ship.update()
  
        
#         #    bullets.update(bullets,aliens)
            
#                           #print('you lose')
#             #break
#             ship.blitme()
#             if uii == 0:
#                 if pygame.sprite.spritecollideany(ship,aliens):
#                     # j = True
#                     # i = 1
                
#                     ship.y-=1
#                     ship.rect.y = ship.y
#             else:
#                 collisions = pygame.sprite.groupcollide(aliens,ships,False,True)
#                 print(len(aliens))

                        
#             # elif :
#             #     j = False
#             #     i = 0

#  #           print(len(alienbullets))
#             for bullet in bullets.copy():
#                 if bullet.rect.x >= ai_settings.screen_width or bullet.rect.x <= 0:
#                     bullets.remove(bullet)
            
#             screen.fill(ai_settings.bg_color)
            
#             for bullet in bullets.sprites():
#                 collisions = pygame.sprite.groupcollide(snifs,bullets,True,True)

#                 collisions = pygame.sprite.groupcollide(bullets,aiens,True,True)
#                 bullet.draw_bullet()
                    
#                 first = randint(0,200)
#                 second = randint(0,200)
#                 three = randint(0,200)
#                 ai_settings.bullet_color = (first,second,three)
#             for ship in ships.sprites():
#                 if pygame.sprite.spritecollideany(ship,sty):
#                     aen.x = randint(0,ai_settings.screen_width)
#                     aen.y = randint(0,ai_settings.screen_height)

#                     alien.rect.x = alien.x
#                     aen.rect.y = alien.y
#                     score += 1
#             tre = randint(-1000,1000)
#             if tre == 0:
#                 sni = Sniff(ai_settings,screen,ship)
#                 snifs.add(sni)
                   
#             bullets.update()
#             ship.blitme()
#             aliens.draw(screen)
            
#             aliens.draw(screen)
            
#             if pygame.sprite.spritecollideany(ant,ships):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
                
        
#             if pygame.sprite.spritecollideany(ant,bullets):
#             #    sys.exit()
#                 #print('your score is',score)
#                 ch -= 1
#                 bullets.empty()
#                 if ch <= 0:
#                     print('you win')
#                     db = 1
#                     break
#             snifs.draw(screen)
#             snifs.update()
#             ant.blitme()
#             ant.update()
#             pygame.display.flip()
            


#     def game_meny():
#         global ch,dobollet,db,wea
#         pygame.init()
#         turn = 0
    

#         fg = 1
#         pfg = 1
        
#         i = 0
#         snifs = Group()
        
#         ai_settings =Settings()
#         screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#         pygame.display.set_caption('Alien Invasion')
#         ship = Ship(ai_settings,screen)
#         alien = Ship(ai_settings,screen)
#         ship.image = pygame.image.load('robot.gif')
#         alien.image = pygame.image.load('fire.gif')
#         ship.x = 0
#         ship.y = 0
#         ship.rect.x = ship.x
#         ship.rect.y = ship.y
#         alien.x = ai_settings.screen_width
#         alien.y = ai_settings.screen_height
#         alien.rect.x = ship.x
#         alien.rect.y = ship.y
#         bullets = Group()
    
#         ships = Group()

#         ships.add(ship)
#         ships.add(alien)
#         while True:

#                 scr = screen.get_rect()
#             if j == False and ship.rect.y < 752:
#                 ship.y+=1
#                 ship.rect.y = ship.y
#         #    ship.y+= 1
#          #   ship.rect.y = ship.y
#             if dobollet == True:
#                 new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                 bullets.add(new_bullet)

                


#             for event in pygame.event.get():

                
#             #for event in pygame.event.get():

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         ship.image = pygame.image.load('fire.gif')
#                         uii = 1
#                     if event.key == pygame.K_1:
#                         first = randint(0,220)
#                         second = randint(0,220)
#                         three = randint(0,220)
#                         ai_settings.bg_color = (first,second,three)
#                     if event.key == pygame.K_b:
#                         sys.exit()
#                     if event.key == pygame.K_RIGHT:
                        
#                         ship.movin_right = True
#                         turn = 0


#                     if event.key == pygame.K_LEFT:
#                         ship.movin_left = True
#                         turn = 1

#                     if event.key == pygame.K_DOWN:
#                         sit = True
#                     if event.key == pygame.K_i:
        
#                         if j == False:
#                     #        print("O")
#                             j = True
#                             i = 0
                     
#                     if event.key == pygame.K_v:
#                         if wea == 0:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                         if wea == 1:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 50
#                             new_bullet.rect.y = new_bullet.y
                            
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 0
#                             new_bullet.rect.y = new_bullet.y
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= -50
#                             new_bullet.rect.y = new_bullet.y
                            
#                 elif event.type == pygame.KEYUP:
#                     if event.key == pygame.K_RIGHT:
#                         ship.movin_right = False               
#                     if event.key == pygame.K_LEFT:               
#                         ship.movin_left = False     

#                     if event.key == pygame.K_UP:
                    
#                         ship.image = pygame.image.load('robot.gif')
#                         uii = 0
#                     if event.key == pygame.K_2:
#                         ship.image = pygame.image.load(random.choice(images))
#                     if event.key == pygame.K_DOWN:
#                         sit = False
#                     if event.key == pygame.K_v:
                        
#                         dobollet = False
                    
#                 if event.type == pygame.MOUSEBUTTONDOWN:
                    

#                     mouse_x,mouse_y = pygame.mouse.get_pos()
#                     if ship.rect.collidepoint(mouse_x,mouse_y):
#                         #run_game()
#                         run_game2()
#                     if alien.rect.collidepoint(mouse_x,mouse_y):
#                         #run_game3()
#                         #run_game4()
#                         run_game()
#             ships.draw(screen)
#             pygame.display.flip()
            








#     def run_game2():
    
#         global ch,dobollet,db,wea
#         pygame.init()
#         turn = 0
    

#         fg = 1
#         pfg = 1
        
#         i = 0
        
#         j = False
#         sit = False
        
#         ai_settings =Settings()
#         screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
#         pygame.display.set_caption('Alien Invasion')
#         ship = Ship(ai_settings,screen)
#         bullets = Group()
    
#         ships = Group()
#         aliens = Group()
#         alies = Group()
#         alien = Alien(ai_settings,screen,ship)
#         buttons = Group()
#         yu = False
#         snifs = Group()

#         #rint(ship.y)iii
#         alienbullets = Group()
#         ert = 0
#         tr = [1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
#         sty = Group()
#         uii = 0
#         filename = 'liberint.txt'
#         #t = [0,1,1,1,0,0,0,0,0,1,1,1]
#         with open(filename) as file_object:
#             file_object.write(tr)
#         aiens = Group()
#         do_liberint(ship,Block)
#         ant = Stynki_man(ai_settings,screen,ship)
#         ships.add(ship)
#         while True:

#             rand = randint(-1000,1000)
            
#             if j == True and i == 0:
                
#                 ert = 0
#                 ship.y -= 1*pfg
#                 fg += 1*pfg
#                 #print(ship.y)
#                 ship.rect.y = ship.y
#                 if fg == 190:
#                     pfg*=-1
#                 if fg == 0:
#                     i = 0
#                     pfg*=-1
#                     j = False
                
#                 scr = screen.get_rect()
#             if j == False and ship.rect.y < 752:
#                 ship.y+=1
#                 ship.rect.y = ship.y
#         #    ship.y+= 1
#          #   ship.rect.y = ship.y
#             if dobollet == True:
#                 new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                 bullets.add(new_bullet)

                


#             for event in pygame.event.get():

                
#             #for event in pygame.event.get():

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         ship.image = pygame.image.load('fire.gif')
#                         uii = 1
#                     if event.key == pygame.K_1:
#                         first = randint(0,220)
#                         second = randint(0,220)
#                         three = randint(0,220)
#                         ai_settings.bg_color = (first,second,three)
#                     if event.key == pygame.K_b:
#                         sys.exit()
#                     if event.key == pygame.K_RIGHT:
                        
#                         ship.movin_right = True
#                         turn = 0


#                     if event.key == pygame.K_LEFT:
#                         ship.movin_left = True
#                         turn = 1

#                     if event.key == pygame.K_DOWN:
#                         sit = True
#                     if event.key == pygame.K_i:
        
#                         if j == False:
#                     #        print("O")
#                             j = True
#                             i = 0
                     
#                     if event.key == pygame.K_v:
#                         if wea == 0:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                         if wea == 1:
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 50
#                             new_bullet.rect.y = new_bullet.y
                            
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= 0
#                             new_bullet.rect.y = new_bullet.y
#                             new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
#                             bullets.add(new_bullet)
#                             new_bullet.y -= -50
#                             new_bullet.rect.y = new_bullet.y
                            
#                 elif event.type == pygame.KEYUP:
#                     if event.key == pygame.K_RIGHT:
#                         ship.movin_right = False               
#                     if event.key == pygame.K_LEFT:               
#                         ship.movin_left = False     

#                     if event.key == pygame.K_UP:
                    
#                         ship.image = pygame.image.load('robot.gif')
#                         uii = 0
#                     if event.key == pygame.K_2:
#                         ship.image = pygame.image.load(random.choice(images))
#                     if event.key == pygame.K_DOWN:
#                         sit = False
#                     if event.key == pygame.K_v:
                        
#                         dobollet = False
                    
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if db == 1:

#                         mouse_x,mouse_y = pygame.mouse.get_pos()
#                         bul = Alien(ai_settings,screen,ship)
#                         aliens.add(bul)
#                         bul.rect.x = mouse_x
#     #276
#                         bul.rect.y = mouse_y
# #276
#             ship.update()
  
        
#         #    bullets.update(bullets,aliens)
            
            
#                           #print('you lose')
#             #break
#             ship.blitme()
#             if uii == 0:
#                 if pygame.sprite.spritecollideany(ship,aliens):
#                     # j = True
#                     # i = 1
                
#                     ship.y-=1
#                     ship.rect.y = ship.y
#             else:
#                 collisions = pygame.sprite.groupcollide(aliens,ships,False,True)
#                 print(len(aliens))

                        
#             # elif :
#             #     j = False
#             #     i = 0

#  #           print(len(alienbullets))
#             for bullet in bullets.copy():
#                 if bullet.rect.x >= ai_settings.screen_width or bullet.rect.x <= 0:
#                     bullets.remove(bullet)
            
#             screen.fill(ai_settings.bg_color)
            
#             for bullet in bullets.sprites():
#                 collisions = pygame.sprite.groupcollide(bullets,aiens,True,True)
#                 bullet.draw_bullet()
                    
#                 first = randint(0,200)
#                 second = randint(0,200)
#                 three = randint(0,200)
#                 ai_settings.bullet_color = (first,second,three)
#             for ship in ships.sprites():
#                 if pygame.sprite.spritecollideany(ship,sty):
#                     aen.x = randint(0,ai_settings.screen_width)
#                     aen.y = randint(0,ai_settings.screen_height)

#                     alien.rect.x = alien.x
#                     aen.rect.y = alien.y
#                     score += 1
                            
#             bullets.update()
#             ship.blitme()
#             aliens.draw(screen)
            
#             aliens.draw(screen)
            
#             if pygame.sprite.spritecollideany(ant,ships):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
#             if pygame.sprite.spritecollideany(ship,snifs):
#             #    sys.exit()
#                 #print('your score is',score)
#                 sys.exit()
#             tre = randint(-3000,1000)
#             if tre == 0:
#                 sni = Sniff(ai_settings,screen,ship)
#                 snifs.add(sni)
        
#             if pygame.sprite.spritecollideany(ant,bullets):
#             #    sys.exit()
#                 #print('your score is',score)
#                 ch -= 1
#                 print(ch)
#                 bullets.empty()
#                 if ch <= 0:
#                     print('you win')
#                     wea = 1
#                     break
                
                
                
                

            
#             alienbullets.update(bullets,aliens)
#             #aen.draw_bullet()
#             ant.update()
#             ant.blitme()          
#             snifs.update()
#             snifs.draw(screen)
#             #chekupdown_fleet_edges(ai_settings,aliens)
            
#             pygame.display.flip()

    def run_game():
        global ch,dobollet,db,wea,t
        pygame.init()
        turn = 0
    

        fg = 1
        pfg = 1
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        print(len(joysticks))
        for joystick in joysticks:
            joystick.init()
        i = 0
        
        j = False
        sit = False
        
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
    
        ships = Group()
        aliens = Group()
        l = 0
        r = 0
        alies = Group()
        alien = Alien(ai_settings,screen,ship)
        buttons = Group()
        yu = False
        #rint(ship.y)iii
        alienbullets = Group()
        ert = 0
        tr = [1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
        sty = Group()
        uii = 0
        aiens = Group()
        ant = Ant_men(ai_settings,screen,ship)
        ships.add(ship)
        while True:

            rand = randint(-1000,1000)
            
            if j == True and i == 0:
                
                ert = 0
                ship.y -= 1*pfg
                fg += 1*pfg
                #print(ship.y)
                ship.rect.y = ship.y
                if fg == 190:
                    pfg*=-1
                if fg == 0:
                    i = 0
                    pfg*=-1
                    j = False
                
                scr = screen.get_rect()
            if j == False and ship.rect.y < 752:
                ship.y+=1
                ship.rect.y = ship.y
        #    ship.y+= 1
         #   ship.rect.y = ship.y
            if dobollet == True:
                new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
                bullets.add(new_bullet)

                


            for event in pygame.event.get():

                
            #for event in pygame.event.get():

                if event.type == pygame.JOYHATMOTION:
                    print('p')
                
                    buttons = joystick.get_numhats()
                    for i in range(buttons):
                        but = joystick.get_hat(i)
                        if but == (-1,0):

                            
                            l = 1
                            t = 3
                        but = joystick.get_hat(i)
                        if but == (1,0):

                            r = 1
                            t = 2
                        # but = joystick.get_hat(i)
                        # if but == (0,1):

                        #     cl = 1
                        #     cr = 1
                        #     cu = 0
                        #     cd = 1
                        #     t = 0
                        # but = joystick.get_hat(i)
                        # if but == (0,-1):

                        #     cl = 1
                        #     cr = 1
                        #     cu = 1
                        #     cd = 0
                        #     t = 1
                else:
                    l = 0
                    r = 0
                if event.type == pygame.JOYBUTTONDOWN:
            
                    button = joystick.get_numbuttons()
                    # print(button)  
                    #pass
#                    for i in range(button):
                    but = joystick.get_button(False)
                    if but == 1:
                        
                        new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                        bullets.add(new_bullet)
                elif event.type == pygame.JOYBUTTONUP:
                        #buttons = joystick.get_numbuttons()
                    button = joystick.get_button(False)
                    print(button)  
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if db == 1:

                        mouse_x,mouse_y = pygame.mouse.get_pos()
                        bul = Alien(ai_settings,screen,ship)
                        aliens.add(bul)
                        bul.rect.x = mouse_x
    #276
                        bul.rect.y = mouse_y
#276
            ship.update()
  
        
        #    bullets.update(bullets,aliens)
            
            
                          #print('you lose')
            #break
            ship.blitme()
            if uii == 0:
                if pygame.sprite.spritecollideany(ship,aliens):
                    # j = True
                    # i = 1
                
                    ship.y-=1
                    ship.rect.y = ship.y
            else:
                collisions = pygame.sprite.groupcollide(aliens,ships,False,True)
                print(len(aliens))

                        
            # elif :
            #     j = False
            #     i = 0

 #           print(len(alienbullets))
            for bullet in bullets.copy():
                if bullet.rect.x >= ai_settings.screen_width or bullet.rect.x <= 0:
                    bullets.remove(bullet)
            
            screen.fill(ai_settings.bg_color)
            
            for bullet in bullets.sprites():
                collisions = pygame.sprite.groupcollide(bullets,aiens,True,True)
                bullet.draw_bullet()
                    
                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)
            for ship in ships.sprites():
                if pygame.sprite.spritecollideany(ship,sty):
                    aen.x = randint(0,ai_settings.screen_width)
                    aen.y = randint(0,ai_settings.screen_height)

                    alien.rect.x = alien.x
                    aen.rect.y = alien.y
                    score += 1
                            
            bullets.update()
            ship.blitme()
            aliens.draw(screen)
            
            aliens.draw(screen)
            
            if pygame.sprite.spritecollideany(ant,ships):
            #    sys.exit()
                #print('your score is',score)
                sys.exit()
                
        
            if pygame.sprite.spritecollideany(ant,bullets):
            #    sys.exit()
                #print('your score is',score)
                ch -= 1
                bullets.empty()
                if ch <= 0:
                    print('you win')
                    db = 1
                    break
                
                
                
                

            
            alienbullets.update(bullets,aliens)
            #aen.draw_bullet()
            ant.update()
            ant.blitme()          
            bullets.update()
            bullets.draw(screen)
            #chekupdown_fleet_edges(ai_settings,aliens)
            
            pygame.display.flip()
    while True:
        run_game()
        