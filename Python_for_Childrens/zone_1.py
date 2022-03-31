
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
    from dovillage1 import *
    import pygame.font
    import sys 

    #import pygame.mixer
    from pygame import mixer 
    import pygame.mixer_music
    
    t = 0
    t2 = 0

    bulets = 0
    class NPC(Sprite):
        def __init__(self,ai_settings,screen,text='go out'):
            super(NPC, self).__init__()
            
            self.t = 0
            self.text = text
            self.screen = screen
            self.speed_factor = 3
            self.ai_settings = ai_settings
            self.randdom = randint(0,1)
            self.image = pygame.image.load("warrior.gif")
            self.rect = self.image.get_rect()
            self.x = self.rect.x
            self.y = self.rect.y
        def update(self):
            pass
        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Scoreboard():
        def __init__(self,ai_settings,screen,stats,bg):
            self.screen = screen
            self.bg = bg
            self.screen_rect = screen.get_rect()
            self.ai_settings = ai_settings
            self.width,self.heght = 200,50
            self.button_color = (0,255,0)
            self.stats = stats
            self.button_color = (225,255,225)
            self.font = pygame.font.SysFont(None,48)
            self.rect = pygame.Rect(0,0,self.width,self.heght)

            self.text_color = (30,30,30)
            self.prep_score()
        def prep_score(self):
            score_str = str(self.bg)

            self.score_image = self.font.render(score_str,True,self.text_color,self.button_color)
            self.rect = self.score_image.get_rect()
            self.rect.x = self.screen_rect.x - 50
            self.rect.y = 100

            # score_str = str(self.stats.high_score)
            

            # self.score_image = self.font.render(score_str,True,self.text_color,self.button_color)
            # self.rect = self.score_image.get_rect()
            # self.rect.x = self.screen_rect.x - 20
            # self.rect.y = 20

        def show_score(self):
            
            self.screen.blit(self.score_image, self.rect)
            #self.ships.draw(self.screen)
            # self.screen.blit(self.stats.score_image, self.stats.score_rect)        
            
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
                #(block.rect.x)
                blocks.add(block)
                x += 1
        
                ##(len(blocks))


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
            self.fleet_diraction = 1
    class Bullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,alien,t):
            super(Bullet, self).__init__()
            
            self.t = t
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,0)
            
            if randdom == 0:
                self.image = pygame.image.load("leave.gif")
            if randdom == 1:
                self.image = pygame.image.load("branch.gif")
            self.rect = self.image.get_rect()
            self.aliens = aliens
            self.bullets = bullets
            self.count = 20
            

            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = 5
            

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
            self.count -= 1
                
        def draw_bullet(self):
            
            self.screen.blit(self.image,self.rect)












    class Block(Sprite):
        def __init__(self,ai_settings,screen,non):
            super(Block, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load(non)
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
                        #('ouch right')
                        pass
            if self.movin_left and self.rect.left > 0:
                #self.rect.centerx -= 1
                self.senter -= self.ai_settings.ship_speed_factor
                self.rect.centerx = self.senter
                if pygame.sprite.spritecollideany(ship,blocks):
                    if self.canr == False:
                        pass
            if self.movin_up:
                self.rect.bottom -= 1
            if self.movin_down:
                self.rect.bottom += 1

        def blitme(self):
            self.screen.blit(self.image,self.rect)
    class Alien(Sprite):
        def __init__(self,ai_settings,screen):
            super(Alien, self).__init__()
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
            pass


     #       self.x += self.duraction
      #      self.rect.x = self.x
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
                return False
            if self.rect.left <= 0:
                return False
            
        def update(self):


            self.x += self.duraction
            self.rect.x = self.x
    class Alien_what_go_up_and_down(Sprite):
        def __init__(self,ai_settings,screen):
            super(Alien_what_go_up_and_down, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            #self.alienBullet = alienBullet
            

            self.image = pygame.image.load("robot1.gif")
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
                return False
            if self.rect.left <= 0:
                return False
            
        def update(self):


            self.y += self.duraction
            self.rect.y = self.y
            

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
                #("P")
            if self.f <= 0:
                return True


        def update(self):

            if self.rect.x > self.ship.rect.x:
                self.x -= 0.4
                self.image = pygame.image.load('bowserleft.gif')
            if self.rect.x < self.ship.rect.x:
                self.x += 0.4
                self.image = pygame.image.load('bowserright.gif')
            if self.rect.y > self.ship.rect.y:
                self.y -= 0.4
            if self.rect.y < self.ship.rect.y:
                self.y += 0.4

            self.rect.x = self.x
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
      
#    def run_game():
    def run_game():
    
        global ch,dobollet,db,wea,t
        pygame.init()
        pygame.mixer.init()
        shoot = mixer.Sound('19 - GTR Attack!.mp3')
        music = mixer.Sound("sounds/Windows Critical Stop.wav")
        image = pygame.image.load('bg.gif') 
        
        turn = 0
        
        ch = 10
    

        fg = 1
        pfg = 1
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        #(len(joysticks))
        for joystick in joysticks:
            joystick.init()
        i = 0
        
        j = False
        sit = False
        sco = 0
        
        ai_settings =Settings()
        screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        ship = Ship(ai_settings,screen)
        bullets = Group()
    
        ships = Group()
        blocks = Group()
        aliens = Group()
        l = 0
        r = 0
        godown = 0
        sb = Scoreboard(ai_settings,screen,0,sco)
        alies = Group()

        buttons = Group()


        yu = False
        #rint(ship.y)  
        
        alienbullets = Group()
        ert = 0
        tr = [1,1,1,1,0,0,0,0,1,1,1,1,2,0,0,0,0,1,1,1,1,0,0,1,1,1,1,2,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,2]
        sty = Group()
        uii = 0

        jkd = Group()
        aliens = Group()
        poweraps = Group()
        guns = Group()
        npcs = Group()
        do_liberint(pygame,Block,blocks,ai_settings,screen,'village_1.txt',guns, NPC, npcs)
        aiens = Group()
        ant = Ant_men(ai_settings,screen,ship)
        pistol = Alien(ai_settings,screen)
        pistol.image = pygame.image.load('supercat.gif')
        pistol.rect.x = 228
        pistol.rect.y = 171
        pistol.x = 228
        pistol.y = 171
        
        #blocks.add(pistol)
        guns.add(pistol)
        timeka = 0
        ships.add(ship)
        shoot.play(-1)
        gun = 0
        time = 0
        money = 0
        un = 0
        opi = 0
        
        ipo = 1
        tre = 0
        ships2 = Group()
        power = 0
        spee = 3
        jumper = 130
        ppfg = pfg
        cd = 1
        cu = 1
        sg = 0
        cg = 0
        matreshka = 0
        
        for powerap in npcs.sprites():
            blocks.add(powerap)
        # matre = input('do you want to switch to peaceful mode?(y/n): ')
        # if matre == 'y':
        #     aliens.empty()
            
        rod_2 = 0
        sg = 300
        while True:

            pygame.time.wait(5)
            timeka+=1

            # #(len(poweraps))
            # if len(aliens) <= 0:
            #     import sea_battle
            #     import 



            # collisions = pygame.sprite.groupcollide(ships, guns, False,True)
            # print(guns.sprites())
            # if collisions:
            #     power += 1
            #     print(power)
            #     if power == 1:
            #         gun = 1
            #     if power == 2:
            #         rod_2 = 1
#             if j == True and i == 0:
                    


#                 if pygame.sprite.spritecollideany(ship, blocks):
#                     #(pfg)
#                     #('kkkkkk')
                    
#                     if pfg == -1:
#                         #('lkkkl')
#                         j = False
#                         #(j)
#                         i = 0
#                 ert = 0
# #                ship.y -= 1*pfg
#                 for alien in guns.sprites():
#                     alien.y += pfg
#                     alien.rect.y = alien.y
#                 for alien in blocks.sprites():
#                     alien.y += pfg
#                     alien.rect.y = alien.y
#                 if pygame.sprite.spritecollideany(ship,blocks):
#                     for alien in blocks.sprites():
#                         alien.y += pfg*-1
#                         alien.rect.y = alien.y
#                     for alien in guns.sprites():
#                         alien.y += pfg*-1
#                         alien.rect.y = alien.y
#                     if pfg == -1:
#                         pfg = 1    
#                         fg = 0
#                         j = False

                
#                 # #for alien in poweraps.sprites():
#                 # ant.y += pfg
#                 # ant.rect.y = ant.y


#                 fg += 1*pfg
#                 ##(ship.y)
# #                ship.rect.y = ship.y
#                 if fg == jumper:
#                     pfg*=-1
#                 if fg == 0:

#                     pfg*=-1
#                     j = False
#                 #(pfg)
#                 scr = screen.get_rect()
#             if j == False and godown == 0:
#                 for alien in blocks.sprites():
#                     alien.y -= 1
#                     alien.rect.y = alien.y
#                 for alien in guns.sprites():
#                     alien.y -= 1
#                     alien.rect.y = alien.y      
#                 ant.y-=1            #     #updatenow = 1
            #     for alien in aliens.sprites():
            #         alien.x -= 1
            #         alien.rect.x = alien.x
            # if pygame.sprite.spritecollideany(ship,blocks):
            #     for alien in blocks.sprites():
            #         alien.y += 1
            #         alien.rect.y = alien.y
            #     for alien in guns.sprites():
            #         alien.y += 1
            #         alien.rect.y = alien.y
            
            
            
            if cu == 0:
    
                ship.image = pygame.image.load('SCRightUp.gif')
                ship.blitme()
                #pygame.display.flip()
                               
                for alien in blocks.sprites():
                    
                    alien.y += spee
                    alien.rect.y = alien.y
                for alien in guns.sprites():
                    
                    alien.y += spee
                    alien.rect.y = alien.y
                if pygame.sprite.spritecollideany(ship,blocks):
                    for alien in blocks.sprites():
                        alien.y -= spee
                        alien.rect.y = alien.y
                    for alien in guns.sprites():
                        alien.y -= spee
                        alien.rect.y = alien.y
                #pygame.display.flip()
                #pygame.display.flip()
                #pygame.display.flip()
                ship.image = pygame.image.load('SCright.gif')
                ship.blitme()
                # if pygame.sprite.spritecollideany(ship,blocks):
                #     for alien in poweraps.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x
                #     for alien in blocks.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x



            if cd == 0:


                #pygame.display.flip()
                               
                for alien in blocks.sprites():
                    
                    alien.y -= spee
                    alien.rect.y = alien.y
                for alien in guns.sprites():
                    
                    alien.y -= spee
                    alien.rect.y = alien.y
                if pygame.sprite.spritecollideany(ship,blocks):
                    for alien in blocks.sprites():
                        alien.y += spee
                        alien.rect.y = alien.y
                        
                    for alien in guns.sprites():
                        alien.y += spee
                        alien.rect.y = alien.y
            
            
            
            
            
            if r == 0:

                ship.image = pygame.image.load('SCRightUp.gif')
                ship.blitme()
                #pygame.display.flip()
                               
                for alien in blocks.sprites():
                    
                    alien.x -= spee
                    alien.rect.x = alien.x
                for alien in guns.sprites():
                    
                    alien.x -= spee
                    alien.rect.x = alien.x
                if pygame.sprite.spritecollideany(ship,blocks):
                    for alien in blocks.sprites():
                        alien.x += spee
                        alien.rect.x = alien.x
                    for alien in guns.sprites():
                        alien.x += spee
                        alien.rect.x = alien.x
                #pygame.display.flip()
                #pygame.display.flip()
                #pygame.display.flip()
                ship.image = pygame.image.load('SCright.gif')
                ship.blitme()
                # if pygame.sprite.spritecollideany(ship,blocks):
                #     for alien in poweraps.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x
                #     for alien in blocks.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x



            if l == 0:


                #pygame.display.flip()
                               
                for alien in blocks.sprites():
                    
                    alien.x += spee
                    alien.rect.x = alien.x
                for alien in guns.sprites():
                    
                    alien.x += spee
                    alien.rect.x = alien.x
                if pygame.sprite.spritecollideany(ship,blocks):
                    for alien in blocks.sprites():
                        alien.x -= spee
                        alien.rect.x = alien.x
                        
                    for alien in guns.sprites():
                        alien.x -= spee
                        alien.rect.x = alien.x
                #pygame.display.flip()

                # if pygame.sprite.spritecollideany(ship,blocks):
                #     for alien in poweraps.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x
                #     for alien in blocks.sprites():
                #         alien.x += 1
                #         alien.rect.x = alien.x



            if l == 0:

                ant.x += 1    
                ant.rect.x = ant.x            # if pygame.sprite.spritecollideany(ship,blocks):
                #     for alien in poweraps.sprites():
                #         alien.x -= 1
                #         alien.rect.x = alien.x
                #     for alien in blocks.sprites():
                #         alien.x -= 1
                #         alien.rect.x = alien.x

            


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

                            ship.x -= 1
                            ship.rect.x = ship.x
                            if pygame.sprite.spritecollideany(ship,blocks):
                                ship.x += fuster
                                ship.rect.x = ship.x
                            t = 3
                        but = joystick.get_axis(0)
                        if but > .5:

                            ship.x += 1
                            ship.rect.x = ship.x
                            if pygame.sprite.spritecollideany(ship,blocks):
                                ship.x -= fuster
                                ship.rect.x = ship.x

                            t = 2
                        but = joystick.get_axis(1)
                        if but < -.5:

                            j = True
                        # but = joystick.get_axis(1)
                        # if but <  -.5:

                        #     ship.y -= 1
                        #     ship.rect.y = ship.y
                        #     if pygame.sprite.spritecollideany(ship,blocks):
                        #         ship.y += fuster
                        #         ship.rect.y = ship.y

                        #     t = 0
                        # but = joystick.get_axis(1)
                        # if but > .5:

                        #     ship.y += 1
                        #     ship.rect.y = ship.y
                        #     if pygame.sprite.spritecollideany(ship,blocks):
                        #         ship.y -= fuster
                        #         ship.rect.y = ship.y
                        #     t = 1
                        
                if event.type == pygame.JOYHATMOTION:
                
                    buttons = joystick.get_numhats()
                    for i in range(buttons):
                        but = joystick.get_hat(i)
                        if but == (-1,0):

                            l = 0
                            r = 1
                            cu = 1
                            cd = 1
                            t = 3
                        but = joystick.get_hat(i)
                        if but == (1,0):

                            l = 1
                            r = 0
                            cu = 1
                            cd = 1
                            t = 2
                        but = joystick.get_hat(i)
                        if but == (0,1):
                            j = False
                            pfg *=-1
                            j = True
                        but = joystick.get_hat(i)
    
                if event.type == pygame.JOYBUTTONDOWN:
                    button = joystick.get_button(True)
                    # #(button)  
                    #pass
                    if button == 1:
                        music.play()

                        new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                        bullets.add(new_bullet)
                    button = joystick.get_button(True)
                    if button == 0:

                        if un == 0:
                            upda = 1
                        if un == 1:
                            upda = 0
                        un = upda

                
                
                elif event.type == pygame.JOYBUTTONUP:
                        #buttons = joystick.get_numbuttons()
                    button = joystick.get_button(False)
             
                if event.type == pygame.K_KP_ENTER:
                    
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    alien = Alien_what_go_up_and_down(ai_settings,screen)
                    alien.x = mouse_x
                    alien.rect.x = mouse_x
                    alien.y = mouse_y
                    alien.rect.y = mouse_y
                    aliens.add(alien)
                if event.type == pygame.MOUSEBUTTONDOWN:

                    
                        mouse_x,mouse_y = pygame.mouse.get_pos()
                        alien = Alien_what_go_left_and_right(ai_settings,screen)
                        alien.x = mouse_x
                        alien.rect.x = mouse_x
                        alien.y = mouse_y
                        alien.rect.y = mouse_y
                        aliens.add(alien)
                if event.type == pygame.KEYDOWN:
    
                    if event.key == pygame.K_LEFT:

                        l = 0
                        r = 1
                        cu = 1
                        cd = 1
                        t = 3
                    # if event.key == pygame.K_a:
                    #   if tre >= 100:      
                    #     tre = 0
                    #     for k in range(100):
                    #         collisions = pygame.sprite.groupcollide(ships,aliens,False,True)

                    #         screen.fill(ai_settings.bg_color)
                    #         ships2.draw(screen)
                    #         if l == 0:


                    #             #pygame.display.flip()
                    #             collisions = pygame.sprite.groupcollide(ships,aliens,False,True)                                            
                    #             for alien in blocks.sprites():
                                    
                    #                 alien.x += 1
                    #                 alien.rect.x = alien.x
                    #             collisions = pygame.sprite.groupcollide(ships,aliens,False,True)
                    #             if pygame.sprite.spritecollideany(ship,blocks):
                    #                 if alien in aliens.sprites():
                    #                     aliens.remove(alien)
                    #                     blocks.remove(alien)
                    #                     break
                    #                 for alien in blocks.sprites():
                    #                     alien.x -= 1
                    #                     alien.rect.x = alien.x

                    #                 break
                    #         if r == 0:
    

                    #             #pygame.display.flip()
                    #             for k in range(100):
                    #                 collisions = pygame.sprite.groupcollide(ships,aliens,False,True)

                    #                 screen.fill(ai_settings.bg_color)
                    #                 ships2.draw(screen)
                    #                 if r == 0:


                    #                     #pygame.display.flip()
                    #                     collisions = pygame.sprite.groupcollide(ships,aliens,False,True)                                            
                    #                     for alien in blocks.sprites():
                                            
                    #                         alien.x += 1
                    #                         alien.rect.x = alien.x
                    #                     collisions = pygame.sprite.groupcollide(ships,aliens,False,True)
                    #                     if pygame.sprite.spritecollideany(ship,blocks):
                    #                         if alien in aliens.sprites():
                    #                             aliens.remove(alien)
                    #                             blocks.remove(alien)
                    #                             break
                    #                         for alien in blocks.sprites():
                    #                             alien.x -= 1
                    #                             alien.rect.x = alien.x

                    #                         break
#                            ship.blitme()
 #                       ships2.empty()



 



                    if event.key == pygame.K_RIGHT:

                        l = 1
                        r = 0
                        cu = 1
                        cd = 1
                        t = 2
                        #but = joystick.get_hat(i)
                    if event.key == pygame.K_DOWN:

                        l = 1
                        r = 1
                        cu = 1
                        cd = 0
                        t = 1
                    #but = joystick.get_hat(i)
                    if event.key == pygame.K_UP:

                        l = 1
                        r = 1
                        cu = 0
                        cd = 1
                        t = 0
                    if event.key == pygame.K_2:
                        print(sg)
                        if rod_2 == 1 and sg-3 >= 0:
                            new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                            sg -= 3
                            new_bullet.count = 1000
                            if gun == 1:
                                new_bullet.image = pygame.image.load('star.gif')


                                #(t)
                                if t == 2:
                                    #('k')
                                    new_bullet.x+=50
                                if t == 3:
                                    #('k')
                                    new_bullet.x-=75
                                if t == 0:
                                    #('k')
                                    new_bullet.y-=50
                                if t == 1:
                                    #('k')
                                    new_bullet.y+=50


                                        
                            guns.add(new_bullet)



                            bullets.add(new_bullet)

                    if event.key == pygame.K_i:
                        if matreshka == 0:
                            matreshka = 1
                        else:
                            matreshka = 0
                    if event.key == pygame.K_b:
                        print(l,r)
                        if cg <= 150:
                            if timeka >= 150:
                                timeka = 0
                                for x in range(100):
                                    if l == 0:
                        

                                    #pygame.display.flip()
                                                
                                        for alien in blocks.sprites():
                                        
                                            alien.x += spee
                                            alien.rect.x = alien.x
                                        for alien in guns.sprites():
                                        
                                            alien.x += spee
                                            alien.rect.x = alien.x
                                        if pygame.sprite.spritecollideany(ship,blocks):
                                            for alien in blocks.sprites():
                                                alien.x -= spee
                                                alien.rect.x = alien.x
                                            
                                            for alien in guns.sprites():
                                                alien.x -= spee
                                                alien.rect.x = alien.x
                                    if r == 0:
                                

                                            #pygame.display.flip()
                                                        
                                        for alien in blocks.sprites():
                                                
                                            alien.x -= spee
                                            alien.rect.x = alien.x
                                        for alien in guns.sprites():
                                                
                                            alien.x -= spee
                                            alien.rect.x = alien.x
                                        if pygame.sprite.spritecollideany(ship,blocks):
                                            for alien in blocks.sprites():
                                                alien.x += spee
                                                alien.rect.x = alien.x
                                                    
                                            for alien in guns.sprites():
                                                alien.x += spee
                                                alien.rect.x = alien.x
                    if event.key == pygame.K_1:
                        if sg >= 10:
                            sg = 0
                            if gun == 1:
                                for x in range(10):
                                    new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                                    #(t)
                                    new_bullet2 = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                                    new_bullet3 = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                                    if t == 2:
                                        #('k')
                                        new_bullet.x+=x*50
                                        new_bullet2.x+=x*50
                                        new_bullet3.x+=x*50
                                    if t == 3:
                                        new_bullet.x-=x*50
                                        new_bullet2.x-=x*50
                                        new_bullet3.x-=x*50
                                    bullets.add(new_bullet)
                            
                                    if t == 0:
                                        #('k')
                                        new_bullet.y-=x*50
                                        new_bullet2.y-=x*50
                                        new_bullet3.y-=x*50
                                    if t == 1:
                                        new_bullet.y+=x*50
                                        new_bullet2.y+=x*50
                                        new_bullet3.y+=x*50
                                    bullets.add(new_bullet)
                                    # bullets.add(new_bullet2)
                                    # bullets.add(new_bullet3)
                    if event.key == pygame.K_v:
                        if gun == 1:

                            new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,t)
                            new_bullet.speed_factor = 1
                            #(t)
                            if t == 2:
                                #('k')
                                new_bullet.x+=50
                                new_bullet.image = pygame.image.load('sword_right.gif')
                            if t == 3:
                                #('k')
                                new_bullet.x-=75
                                new_bullet.image = pygame.image.load('sword_left.gif')
                            if t == 0:
                                #('k')
                                new_bullet.y-=50
                                new_bullet.image = pygame.image.load('sword_up.gif')
                            if t == 1:
                                #('k')
                                new_bullet.y+=50
                                new_bullet.image = pygame.image.load('sword_down.gif')

                                        
                            bullets.add(new_bullet)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        r = 1
                    if event.key == pygame.K_LEFT:
                        l = 1

                    if event.key == pygame.K_DOWN:
                        cd = 1
                    if event.key == pygame.K_UP:
                        cu = 1


                    
                        
                    
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
            if collisions:
                if len(aliens) <= 0:
                    print('ll')
                cg += 1
                if cg >= 10:
                    #[')
                    spee = 3
                    jumper = 290
                sg += 1


            #(ships.sprites(),guns.sprites(),collisions)
            
            
            gun = 1
                          ##('you lose')
            #break
            ship.blitme()

            if pygame.sprite.spritecollideany(ship,blocks):
                
                for alien in blocks.sprites():
                    alien.y += 1
                    alien.rect.y = alien.y
                ant.y += 1
                ant.rect.y = ant.y

                
            
            #    godown = 0
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
        
            collisions = pygame.sprite.groupcollide(ships,aliens,True,True)
            

            
                
            # for alien in aliens.sprites():

            #     if pygame.sprite.spritecollideany(alien,blocks):
            #         alien.duraction *= -1
            bullets.update(1,2)
            for npc in npcs.sprites():

                if pygame.sprite.spritecollideany(npc,bullets):
                    print('pp[p')
                    tre = input('1)return to camp, 2)dark woods, 3)southern mine, 4)west mine, 5)village ruins: ')
            for bullet in bullets.sprites():
                
                bullet.draw_bullet()
                collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
                if collisions:
                    moneys+=1
                
                
                
                

                first = randint(0,200)
                second = randint(0,200)
                three = randint(0,200)
                ai_settings.bullet_color = (first,second,three)

            bullets.update(bullets,aliens)
            ship.blitme()
            #chekupdown_fleet_edges(ai_settings,aliens)
            #alien.blitme()
            bullets.draw(screen)
            sb.show_score()
            alienbullets.update(bullets,aliens)
            if matreshka == 0:
                aliens.draw(screen)
        

            
            #if un == 0:

            blocks.draw(screen)            
            if pygame.sprite.spritecollideany(ant,ships):
                if pfg == -1:
                    g = 1

                    ant.image = pygame.image.load('bowserflat.gif')
                    bullets.empty()
                    if ch <= 0:

                        #('you win')
                        break
                    un = 1
                    j = False
                    pfg *=-1

                    j = True
                else:
                    if un == 0:
                        #('you lose')
                        sys.exit()
                
            if pygame.sprite.spritecollideany(ship,aliens):
                ch -= 1
                bullets.empty()
                if ch == ch:

                    #('you lose')
                    break
            


            if pygame.sprite.spritecollideany(ant,bullets):
                ch -= 1
                bullets.empty()
                if ch <= 0:

                    #('you win')
                    break
            
            #if bezero == 34:
            #bezero = 0
        
            #sb.show_score()
            #poweraps.draw(screen)

            #pygame.display.update()
            #screen.blit(image,(0,0))
            if l == 0:            
                ship.image = pygame.image.load('SCleft.gif')
   
            #     pygame.display.flip()
            #     ship.blitme()
            if r == 0:     
            
                ship.image = pygame.image.load('SCright.gif')
            #     pygame.display.flip()
            #     ship.blitme()

            aliens.draw(screen)
            pygame.time.wait(0)

            opi += ipo
            tre += 0.5
            if opi == 1000:
                ipo *= -1
                # shoot.stop()
                # shoot = mixer.Sound('07 - Metal man.mp3')
                ai_settings.bg_color = (50,50,50)
                # shoot.play()

            if opi == 0:
                ipo = 1
                shoot.stop()
                shoot = mixer.Sound('19 - GTR Attack!.mp3')
                shoot.play()
                ai_settings.bg_color = (220,220,220)
                tre += 1
            #(opi)
            if ipo == 1 and matreshka == 0:
                blocks.update()
                blocks.update()
                blocks.update()
            aliens.draw(screen)
            for alien in aliens.sprites():
                blocks.remove(alien)
                if pygame.sprite.spritecollideany(alien,blocks):
                    alien.duraction *=-1
                blocks.add(alien)
            guns.draw(screen)
            poweraps.draw(screen)
            collisions = pygame.sprite.groupcollide(ships, guns, False, True)
            

            for bullet in bullets.sprites():
                if bullet.count <= 0:
                    bullets.remove(bullet)
            pygame.display.flip()



            #pygame.display.flip()

            


    run_game()
    