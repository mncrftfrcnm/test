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
    
    from dolibe import *
    import dolibe
    import dolibe3
    ty = []
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
    ch = 1000
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

    class Alien(Sprite):
        def __init__(self,ai_settings,screen):
            super(Alien, self).__init__()
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

            self.y += 1*self.dur
            
            self.f += 1*self.dur

                
            self.rect.y = self.y
    class Alen(Sprite):
        def __init__(self,ai_settings,screen):
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
    class Alen2(Sprite):
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
        
    def run_game():
        global ch,dobollet
        pygame.init()
        turn = 0
    

        fg = 1
        pfg = 1
        
        i = 0
        
        j = False
        sit = False
        
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
        
        wea = 0
        ships = Group()
        aliens = Group()
        alies = Group()
        buttons = Group()
        yu = False
        #rint(ship.y)iii
        alienbullets = Group()
        ert = 0
        sty = Group()
        uii = 0
        aiens = Group()
        
        tr = [1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]

        ty = []

        filename = input('file: ')

            
        yt = str(ty)
#        try:

        with open(filename, 'r') as file_object:
            er = file_object.read()
            for d in er:
                ty.append(d)
                


                        
        ships.add(ship)
        print(len(ships))
        ra = -1
        libes = 0
        bg_color = (20,250,200)
        but = Button(ai_settings,screen)
        but.x = 0
        but.y = 0
        iiu = 0
        but.rect.x = but.x
        but.rect.y = but.y
        l = 0
        r = 0
        u = 0
        d = 0

        buttons.add(but)
        
        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,ty)
        

        
        while True:
            if u == 1:

                for al in aliens.sprites():
                    al.rect.y+=1
            if d == 1:

                for al in aliens.sprites():
                    al.rect.y-=1
            if l == 1:

                for al in aliens.sprites():
                    al.rect.x+=1
            if r == 1:

                for al in aliens.sprites():
                    al.rect.x-=1


            # rand = randint(-1000,1000)
            # if rand == 0:
                

            #     alien = Alen(ai_settings,screen,ship)
            #     aiens.add(alien)
            #     alien.x = randint(0,ai_settings.screen_width)
            #     alien.y = randint(0,ai_settings.screen_height)

            #     alien.rect.x = alien.x
            #     alien.rect.y = alien.y
        #     # rand = randint(-1000,1000)
            
        #     if j == True and i == 0:
                
        #         ert = 0
        #         ship.y -= 1*pfg
        #         fg += 1*pfg
        #         #print(ship.y)
        #         ship.rect.y = ship.y
        #         if fg == 190:
        #             pfg*=-1
        #         if fg == 0:
        #             i = 0
        #             pfg*=-1
        #             j = False
                
        #         scr = screen.get_rect()
        #     if j == False and ship.rect.y < 752:
        #         ship.y+=1
        #         ship.rect.y = ship.y
        # #    ship.y+= 1
        #  #   ship.rect.y = ship.y
        #     if dobollet == True:
        #         new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,turn)
        #         bullets.add(new_bullet)
            

                
    
            if iiu == 1:
                break
            for event in pygame.event.get():

                
            #for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        ship.image = pygame.image.load('fire.gif')
                        uii = 1
                    if event.key == pygame.K_b:
                        iiu = 1
                    if event.key == pygame.K_RIGHT:
                        
                        ship.movin_right = True
                        turn = 0


                    if event.key == pygame.K_LEFT:
                        ship.movin_left = True
                        turn = 1

                    if event.key == pygame.K_h:
                        
                        
                        ty.remove(ty[ra])

                    
                        
                        yt = str(ty)
                        aliens.empty()
                        dolibe.x,dolibe.y = 0,0
                        with open(filename, 'w') as file_object:
                            file_object.write(yt)

                        dolibe.x,dolibe.y = 0,0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        ra -= 1

                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)
                    if event.key == pygame.K_k:
                        
                        
                        ty.clear()

                    
                        
                        yt = str(ty)
                        aliens.empty()
                        dolibe.x,dolibe.y = 0,0
                        with open(filename, 'w') as file_object:
                            file_object.write('')

                        dolibe.x,dolibe.y = 0,0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        ra = 0                        
                    if event.key == pygame.K_0:
                        
                        
                        ty.append(0)
                        ra+=1

                    
                        
                        yt = str(ty)
                        aliens.empty()
                        dolibe.x,dolibe.y = 0,0
                        with open(filename, 'w') as file_object:
                            file_object.write(yt)

                        dolibe.x,dolibe.y = 0,0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)

#                        do_liberint(pygame,Alien,aliens,ai_settings,screen)
                    if event.key == pygame.K_2:
                        ra += 1
                        ty.append(2)
                        dolibe.x,dolibe.y = 0,0
                        
                        yt = str(ty)
                        aliens.empty()

                        with open(filename, 'w') as file_object:
                            file_object.write(yt+'\n')

                        #yt = str(ty)
                        dolibe.x,dolibe.y = 0,0
                        dolibe.x = 0
                        dolibe.y = 0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)
                        
                    if event.key == pygame.K_1:
                        ra+=1
                        ty.append(1)
                        dolibe.x,dolibe.y = 0,0
                        
                        aliens.empty()
                        
                        yt = str(ty)
                        with open(filename, 'w') as file_object:
                            file_object.write(yt)

                        dolibe.x = 0
                        dolibe.y = 0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)
                    if event.key == pygame.K_4:
                        ra+=1
                        ty.append(4)
                        dolibe.x,dolibe.y = 0,0
                        
                        aliens.empty()
                        
                        yt = str(ty)
                        with open(filename, 'w') as file_object:
                            file_object.write(yt)

                        dolibe.x = 0
                        dolibe.y = 0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)

                    if event.key == pygame.K_3:
                        ra+=1
                        ty.append(3)
                        dolibe.x,dolibe.y = 0,0
                        
                        aliens.empty()
                        
                        yt = str(ty)
                        with open(filename, 'w') as file_object:
                            file_object.write(yt)

                        dolibe.x = 0
                        dolibe.y = 0
                        dolibe3.x = 0
                        dolibe3.y = 0
                        dolibe3.do_liberint(pygame,Alien,aliens,ai_settings,screen,yt)

                    if event.key == pygame.K_RIGHT:
                        r = 1               
                    if event.key == pygame.K_LEFT:               
                        l = 1     

                    if event.key == pygame.K_UP:
                    
                        
                        u = 1
                    if event.key == pygame.K_DOWN:
                        d = 1
                        

                        
                        
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        r = 0               
                    if event.key == pygame.K_LEFT:               
                        l = 0     

                    if event.key == pygame.K_UP:
                    
                        
                        u = 0
                    if event.key == pygame.K_DOWN:
                        d = 0
                    if event.key == pygame.K_v:
                        
                        dobollet = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = pygame.mouse.get_pos()
#                     bul = Alien(ai_settings,screen)
#                     aliens.add(bul)
#                     bul.rect.x = mouse_x
# #276
#                     bul.rect.y = mouse_y
                    break
#276



  
        
        #    bullets.update(bullets,aliens)
            
            
                          #print('you lose')
            #break
            # ship.blitme()
            # if uii == 0:
            #     if pygame.sprite.spritecollideany(ship,aliens):
            #         # j = True
            #         # i = 1
                
            #         ship.y-=1
            #         ship.rect.y = ship.y
            # else:
            #     collisions = pygame.sprite.groupcollide(aliens,ships,False,True)
            #     print(len(aliens))

                        
            # elif :
            #     j = False
            #     i = 0                            
#             bullets.update()
#             ship.blitme()
#             aliens.draw(screen)
#             bullets.draw(screen)
#             aiens.draw(screen)
#             aiens.update()
# #            do_liberint(ship,Alien,aliens,aliens,Alien,ai_settings,screen,0)
#             but.blitme()
#             aliens.draw(screen)
#             but.update()

                
                
                

            

#            aen.draw_bullet()
            
            #chekupdown_fleet_edges(ai_settings,aliens)
            #print(ty)
            screen.fill((100,100,100))
            aliens.draw(screen)
            ship.blitme()
            ship.rect.x = dolibe3.x
            ship.rect.y = dolibe3.y
            



            pygame.display.flip()
            

    

    run_game()

    # while True:
        # filename = input('file: ')

        
        # yt = str(ty)
        # try:

        #     with open(filename, 'w') as file_object:
        #         file_object.write(yt)
                

        # except FileNotFoundError:
        #     print('we have not this file try again')            
        # else:
        #     with open(filename, 'w') as file_object:
        #         file_object.write(yt)
        #     break
            