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
    from pygame.mixer import *
    import pygame.mixer
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
    # (joycon_id)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    #pink joycon right (1406, 8199, '9458cbb41938')
    #blue joycon left   

    joycon = MyJoyCon(1406, 8199, 'e0f6b5c308dc')
    joycon.get_status()
    joycon2 = MyJoyCon(1406, 8198, '9458cbb3aeaa')
    joycon2.get_status()
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
        
                ##(len(blocks))


except ConnectionRefusedError:
    #('please run again')
    pass

else:
    images = ['cat1.gif','cat2.gif','tree.gif','tree.gif']
    ch = 50000
    class Settings():

        def __init__(self):
            self.screen_width = 1200
            self.bullet_speed_factor = 5
            self.screen_height = 800
            self.bg_color = (20,250,200)
            self.ship_speed_factor = 1
            self.bullet_color = 50,50,50
            self.bullet_width = 20
            self.bullet_height = 20 
            self.bullet_allowed =  3

    class warrior(Sprite):
        def __init__(self,ai_settings,screen):
            super(warrior, self).__init__()
            
            self.t = 0
            self.screen = screen
            self.speed_factor = 3
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            self.image = pygame.image.load("warrior.gif")
            self.rect = self.image.get_rect()
            self.x = self.rect.x
            self.y = self.rect.y             
        def update(self):
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
        def blitme(self):
            self.screen.blit(self.image,self.rect)
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

    class Nothing(Sprite):
        def __init__(self,ai_settings,screen,image):
            super(Nothing, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()

            
            

            self.y = float(self.rect.y)
            #elf.rect.x = self.rect.width
            self.x = float(self.rect.x)

        def blitme(self):
            self.screen.blit(self.image,self.rect)
        def update(self):
            
            pass            
    class Block(Sprite):
        def __init__(self,ai_settings,screen,image):
            super(Block, self).__init__()
            self.ai_settings = ai_settings
            self.screen = screen
            self.alienBullet = alienBullet
            

            self.image = pygame.image.load(image)
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
            


        def update(self,ship,blocks):

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
    class htBullet(Sprite):
        def __init__(self,ai_settings,screen,ship,aliens,bullets,goal):
            super(htBullet, self).__init__()
            self.screen = screen
            self.ai_settings = ai_settings
            randdom = randint(0,1)
            

            self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.aliens = aliens
            self.bullets = bullets
            self.goal = goal

            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
            self.rect.bottom = ship.rect.bottom                                             
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.bullet_speed_factor
            

        def update(self,o,i):
            global ch
            global ch
            if self.goal.rect.x < self.rect.x:
                self.rect.x -= 3
            if self.goal.rect.x > self.rect.x:
                self.rect.x += 3
            if self.goal.rect.y < self.rect.y:
                self.rect.y -= 3
            if self.goal.rect.y > self.rect.y:
                self.rect.y += 3
        def draw_bullet(self):                                                                                           
            pygame.draw.rect(self.screen,self.color,self.rect)    
      

    def run_game_2():
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
        filename = 'liberint_boss.txt'
#        t = []



    
    
        alienbullets = Group()
        nothing = Group()
        score = 0
        ch = 50
    

        jkd = Group()
        t2 = 1
        do_liberint(pygame,Block,blocks,ai_settings,screen,filename,warrior,aliens,poweraps)
        for power in poweraps.sprites():
            power.image = pygame.image.load('bomb.gif')
        
        
        
        joycon.set_player_lamp_flashing(1)
        joycon2.set_player_lamp_flashing(2)
        bg_color = (20,260,200)
        invis = 0
    
        ships.add(ship)
        i1 = 0
        i2 = 0
        innothing = Group() 
        
        ships2.add(ship2)

                


        shoot = pygame.mixer.Sound('07 - Metal Man.mp3')
        shoot.play(-1)
        collision = pygame.sprite.groupcollide(ships,blocks,false,True)
        collision = pygame.sprite.groupcollide(ships2,blocks,False,True)
        collision = pygame.sprite.groupcollide(ships,aliens,false,True)
        collision = pygame.sprite.groupcollide(ships2,aliens,False,True)

        collision = pygame.sprite.groupcollide(aliens,blocks,false,True)


        # shoot = mixer.Sound("C:\windows\media\Ring02.wav")
        # #C:\windows\downloads\
        ch = 10
        timer = 5
        while True:
            pygame.time.wait(timer)
            screen.fill(ai_settings.bg_color)
            isstickbut = joycon.stick_r_btn
            isstickmove=joycon.stick_r
 
            if isstickmove[1] > 2000:
                
                ship.rect.x += 3
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.x -= 3
                t = 2
                #('up')
            elif isstickmove[1] < 1000:
                #ship.y += 3
                #('down')
                ship.rect.x -= 3
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.x += 3
                t=3
            
            elif isstickmove[0] > 3000:
                #ship.x += 3
                #('r')
                ship.rect.y += 3
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.y -= 3
                t=1
            elif isstickmove[0] < 1000:
                #ship.x -= 3
                #('l')
                t=0
                ship.rect.y -= 3
                if pygame.sprite.spritecollideany(ship,blocks):
                    ship.rect.y += 3

            isstickbut = joycon2.stick_l_btn
            isstickmove=joycon2.stick_l

            if isstickmove[1] > 3000:

                ship2.rect.x -= 3
                t2 = 3
                if pygame.sprite.spritecollideany(ship2,blocks):
                    ship2.rect.x += 3
                #('up')
            elif isstickmove[1] < 2000:
                #ship.y += 3
                #('down')
                t2 = 2
                ship2.rect.x += 3
                if pygame.sprite.spritecollideany(ship2,blocks):
                    ship2.rect.x -= 3
            
            elif isstickmove[0] > 3000:
                #ship.x += 3
                #('r')
                ship2.rect.y -= 3
                t2 = 0

                if pygame.sprite.spritecollideany(ship2,blocks):
                    ship2.rect.y += 3
            elif isstickmove[0] < 1600:
                #ship.x -= 3
                #('l')
                t2 = 1
                ship2.rect.y += 3
                if pygame.sprite.spritecollideany(ship2,blocks):
                    ship2.rect.y -= 3
            # isstickmove=joycon2.stick_l
            # if isstickmove[1] > 3000:
                
            #     ship2.rect.x += 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.x -= 1
            # elif isstickmove[1] < 1000:
            #     #ship.y += 3
            #     #('down')
            #     ship.rect.x -= 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.x += 1
            # elif isstickmove[0] > 3000:
            #     #ship.x += 3
            #     #('r')
            #     ship2.rect.y += 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.y -= 1
            # elif isstickmove[0] < 1000:
            #     #ship.x -= 3
            #     #('l')
            #     ship2.rect.y -= 1
            #     if pygame.sprite.spritecollideany(ship2,blocks):
            #         ship2.rect.y += 1

            for event_type, status in joycon.events():
                if status == 1:
                    if event_type == 'b':
                        bul = Bullet(ai_settings,screen,ship,1,1,1,t)
                        bullets.add(bul)

                    if event_type == 'y':
                        nothingi = Block(ai_settings,screen,'fire.gif')
                        nothingi.rect.x,nothingi.rect.y = ship.rect.x,ship.rect.y
                
                        if t == 0:
                            nothingi.rect.y -= 60
                        if t == 1:
                            nothingi.rect.y += 60
                        if t == 2:
                            nothingi.rect.x += 60
                        if t == 3:
                            nothingi.rect.x -= 60
                                                            
                        blocks.add(nothingi)
                        innothing.add(nothingi)
                    if event_type == 'a':
                        nothingi = Block(ai_settings,screen,'fire.gif')
                        nothingi.rect.x,nothingi.rect.y = ship.rect.x,ship.rect.y
                        blocks.add(nothingi)
                        innothing.add(nothingi)
                    if event_type == 'right_sr':
                        if timer == 5:
                            timer = 50
                        else:
                            timer = 5
            for event_type, status in joycon2.events():
                if status == 1:
                    if event_type == 'up':
                        bul = Bullet(ai_settings,screen,ship2,1,1,1,t2)
                        bullets.add(bul)
                    if event_type == 'left_sr':
                        if timer == 5:
                            timer = 50
                        else:
                            timer = 5
                    if event_type == 'right':
                        nothingi = Block(ai_settings,screen,'fire.gif')
                        nothingi.rect.x,nothingi.rect.y = ship2.rect.x,ship2.rect.y
                        if t2 == 0:
                            nothingi.rect.y -= 60
                        if t2 == 1:
                            nothingi.rect.y += 60
                        if t2 == 2:
                            nothingi.rect.x += 60
                        if t2 == 3:
                            nothingi.rect.x -= 60
                        blocks.add(nothingi)
                        innothing.add(nothingi)
                    if event_type == 'left':
                        nothingi = Block(ai_settings,screen,'fire.gif')
                        nothingi.rect.x,nothingi.rect.y = ship2.rect.x,ship2.rect.y
                        blocks.add(nothingi)
                        innothing.add(nothingi)


                        
                #(event_type, status)
            # for event_type, status in joycon3.events():
            #     #("ButtonEventJoyCon:")
            #     #(event_type, status)
            # for event_type, status in joycon4.events():
            #     #("ButtonEventJoyCon:")
            #     #(event_type, status)
            screen.fill(ai_settings.bg_color)
            jkd.draw(screen)
            
            for bul in bullets.sprites():
                bul.draw_bullet()
            for bul in alienbullets.sprites():
                bul.draw_bullet()
            
            blocks.draw(screen)
            die_blocks.draw(screen)
            ships.draw(screen)
            ships2.draw(screen)
            bullets.update(1,1)
            collision = pygame.sprite.groupcollide(bullets,innothing,True,True)
            collision = pygame.sprite.groupcollide(alienbullets,innothing,True,True)
            collision = pygame.sprite.groupcollide(bullets,blocks,True,false)
            collision = pygame.sprite.groupcollide(bullets,blocks,True,false)

            collision = pygame.sprite.groupcollide(bullets,blocks,True,false)
            collision = pygame.sprite.groupcollide(alienbullets,blocks,True,false)
            collision = pygame.sprite.groupcollide(alienbullets,bullets,True,True)
            collision2 = pygame.sprite.groupcollide(bullets,aliens,True,False)

            if collision2:
                bullets.empty()
                print(len(bullets))
                ch -= 1
                for x in range(10):
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,0)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,1)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,2)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,3)
                    alienbullets.add(bullet)

                print(ch)
                if ch == 0:
                    collision2 = pygame.sprite.groupcollide(bullets,aliens,False,False)
                    shoot.stop()
                    break
            collision = pygame.sprite.groupcollide(bullets,alienbullets,True,True)
            aliens.draw(screen)
            aliens.update()
            bullets.update(9,9)
            alienbullets.update(2,1)
            blocks.draw(screen)
            for alien in aliens.sprites():
                if randint(0,0) == 0 and len(alienbullets) <= 8:
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,0)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,1)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,2)
                    alienbullets.add(bullet)
                    bullet = Bullet(ai_settings,screen,alien,aliens,alienbullets,ship,3)
                    alienbullets.add(bullet)

                tre = randint(0,150)
                if tre == 45:
                    alien.t = randint(0,3)                    
                if pygame.sprite.spritecollideany(alien,blocks):
                    if alien.t == 0:
                        alien.y += 3
                        alien.rect.y += 3
                    if alien.t == 1:
                        alien.y -= 3
                        alien.rect.y -= 3
                    if alien.t == 2:
                        alien.x -= 3
                        alien.rect.x -= 3
                    if alien.t == 3:
                        alien.x += 3
                        alien.rect.x += 3

                    alien.t = randint(0,3)
            if pygame.sprite.spritecollideany(ship,aliens):
                shoot.stop()
                shoot = pygame.mixer.Sound('27 - Game Over.mp3')
                shoot.play(-1)
                aliens.clear()
                alienbullets.clear()
                pygame.quit()
                run_game()
                sys.exit()
            if pygame.sprite.spritecollideany(ship2,aliens):
                shoot.stop()
                shoot = pygame.mixer.Sound('27 - Game Over.mp3')
                shoot.play(0)
                sys.exit()
                pygame.quit()
                run_game()

            if pygame.sprite.spritecollideany(ship,alienbullets):
                shoot.stop()
                shoot = pygame.mixer.Sound('27 - Game Over.mp3')
                shoot.play(-1)
                shoot.stop()
                pygame.quit()
                sys.exit()
                run_game()
            if pygame.sprite.spritecollideany(ship2,alienbullets):
                shoot.stop()
                shoot = pygame.mixer.Sound('27 - Game Over.mp3')
                shoot.play(0)
                shoot.stop()
                pygame.quit()
                
                run_game()
            print(len(aliens),len(alienbullets))

            pygame.display.flip()


