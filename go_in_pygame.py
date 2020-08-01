import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *

def create_piano(ai_settings,ships,screen):
    for x in range(20):
        ship = Ship(ai_settings,screen)
        ship.rect.x = x*100
        ships.add(ship)
class Settings():
    def __init__(self):
        self.fleet_diraction = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.screen_width =  300
        self.bullet_speed_factor = 3
        self.screen_height = 300
        self.bg_color = (20,250,200)
        self.ship_speed_factor = 1
        self.bullet_color = 60,60,60
        self.alien_speed_factor = 1
        self.bullet_width = 644
        self.bullet_height = 4
        self.bullet_allowed =  133
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship,mouse_x,mouse_y):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(mouse_x,mouse_y,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = mouse_y
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()

        self.screen = screen
        self.color = (0,0,0)

        #self.image = pygame.Rect(mouse_x,mouse_y,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1
        
        
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.senter = float(self.rect.centerx)
    def update(self):
        pass
    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
class Alien(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Alien, self).__init__()
        self.ship =ship 
        self.color = (0,0,0)
        self.plus_y = randint(5,200)
        self.plus_x = randint(5,200)
        self.ai_settings = ai_settings
        self.screen = screen
        

        self.image = self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect = self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)

        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    def chek_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        
    def update(self):


        self.rect.x = self.ship.rect.x+plus_x
        self.rect.y = self.ship.rect.y+plus_y

        
class Blocks(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        

        self.image = pygame.Rect(mouse_x,mouse_y,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect = pygame.Rect(mouse_x,mouse_y,ai_settings.bullet_width,ai_settings.bullet_height)

        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def chek_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        
    def update(self):

        
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

        



def run_game():
    global bullets_die
    
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    ships = Group()
    ships.add(ship)
    create_piano(ai_settings,ships,screen)
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    alien.y = -90
    alien.rect.y = alien.y
    
    for alien_number in range(number_aliens_x):
            
        
        
        #    print(alien.rect.y)
           
        create_alien(ai_settings,screen,aliens,alien_number,5)
      # aliens.add(alien)


    bg_color = (20,250,200)
    while True:
        
        pygame.mouse.set_visible(True)
        
                
            
            
            #    print(alien.rect.y)
        # tre = randint(-1000,1000)
        # if tre == 1:    
        #     alien.y = 0
        #     create_alien(ai_settings,screen,aliens,alien_number,row_number)
        # if tre >= 990:    
        #     bullets_die = False
        #     for row_number in range(number_rows):
        #         for alien_number in range(number_aliens_x):
                    
                
                
        #         #    print(alien.rect.y)
                
        #             create_alien(ai_settings,screen,aliens,alien_number,row_number)
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
                if event.key == pygame.K_SPACE:
                    print("IOU")
                    for alien in ships.sprites():
                        
                        new_bullet = Bullet(ai_settings,screen,alien,0,0)
                        bullets.add(new_bullet)
                    print(len(ships))
                    print(len(bullets))
                                                
                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                mouse_x,mouse_y = pygame.mouse.get_pos()
                for ship in ships.sprites():
                    ship.rect.x = mouse_x
                    ship.rect.y = mouse_y
                    

        ships.update()
        
        bullets.update()
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
            
            collisions = pygame.sprite.groupcollide(bullets,aliens,bullets_die,True)
            if len(aliens) ==  0:
                bullets.empty()
                for row_number in range(number_rows):
                    for alien_number in range(number_aliens_x):
                            
                        
                        
                #         #    print(alien.rect.y)
                        
                        create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
        chek_fleet_edges(ai_settings,aliens)
        aliens.update()
        if pygame.sprite.spritecollideany(ship,aliens):
            pass
        pygame.display.flip()
        for bullet in ships.sprites():
            bullet.blitme()
            first = randint(0,200)
            second = randint(0,200)
            three = randint(0,200)
            ai_settings.bullet_color = (first,second,three)
            
            collisions = pygame.sprite.groupcollide(bullets,aliens,bullets_die,True)
            if len(aliens) ==  0:
                bullets.empty()
                for row_number in range(number_rows):
                    for alien_number in range(number_aliens_x):
                            
                        
                        
                #         #    print(alien.rect.y)
                        
                        create_alien(ai_settings,screen,aliens,alien_number,row_number)
        pygame.display.flip()
        for bullet in aliens.sprites():
            bullet.blitme()
            first = randint(0,200)
            second = randint(0,200)
            three = randint(0,200)
            ai_settings.bullet_color = (first,second,three)
            
            collisions = pygame.sprite.groupcollide(bullets,aliens,bullets_die,True)
            if len(aliens) ==  0:
                bullets.empty()
                for row_number in range(number_rows):
                    for alien_number in range(number_aliens_x):
                            
                        
                        
                #         #    print(alien.rect.y)
                        
                        create_alien(ai_settings,screen,aliens,alien_number,row_number)
        pygame.display.flip()
while True:
    run_game()