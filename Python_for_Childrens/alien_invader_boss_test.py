import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *

import time
ch = 500
def chek_fleet_duraction(ai_settings,aliens):
    ai_settings.fleet_direction *= -1
    ai_settings.alien_speed_factor += 0.01

def chek_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.chek_edges():
            chek_fleet_duraction(ai_settings,aliens)
            break
        
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit


bullets_die = True

def get_number_rows(ai_settings,ship_height,alien_height):
    available_spase_y = ((ai_settings.screen_height - 4*alien_height) - ship_height)
    number_rows = int(available_spase_y / (3*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)

    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
 #   alien_width = alien.rect.width
    
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)
try:
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
            self.rect = pygame.Rect(0,0,ai_settings.alien_bullet_width,ai_settings.bullet_height)
            self.rect2 = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.rect3 = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            self.alien_rect = alien.image.get_rect()
            self.aliens = alien
    
            
            self.alien_rect.centerx = self.alien_rect.centerx
            self.alien_rect.bottom = self.alien_rect.bottom
            self.rect.centerx = alien.rect.centerx
            self.rect.top = alien.rect.top
            self.rect.bottom = self.rect.bottom
            self.y = float(self.rect.y)
            self.x = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)
            self.y2 = float(self.rect.y)
            self.x2 = float(self.rect.x)
            self.y3 = float(self.rect.y)
            self.x3 = float(self.rect.x)
            self.alien_rect.y = float(self.alien_rect.y)
            self.alien_rect.x = float(self.alien_rect.x)

            self.color = ai_settings.bullet_color
            self.speed_factor = ai_settings.alien_bullet_speed_factor
            

        def update(self,bullets,aliens):
            global ch
            global ch
            self.y += self.speed_factor
            self.rect.y = self.y
            self.x -= self.speed_factor
            self.rect.x = self.x
            self.y += self.speed_factor
            self.rectx = self.x
            self.x += self.speed_factor                
        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)

except TimeoutError:
    pass
else:
    pass       
class Settings():
    def __init__(self):
        self.ships_limit = 3
        self.fleet_diraction = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.screen_width = 1200
        self.bullet_speed_factor = 3
        self.alien_bullet_speed_factor = 2
        self.alien_bullet_width = 54

        self.screen_height = 800
        self.bg_color = (20,250,200)
        self.ship_speed_factor = 1
        self.bullet_color = 60,60,60
        self.alien_speed_factor = 1
        self.bullet_width = 540
        self.bullet_height = 540
        self.bullet_allowed =  133
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y


        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen

        self.image = pygame.image.load("tree.gif")
        self.rect = self.image.get_rect()
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1
        
        
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.senter = float(self.rect.centerx)
    def update(self):
        if self.movin_right and self.rect.right < self.screen_rect.right:
            #self.rect.centerx += 1
            self.senter += self.ai_settings.ship_speed_factor

        if self.movin_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.senter -= self.ai_settings.ship_speed_factor
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
        
class Blocks(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        

        self.image = pygame.image.load("fire.gif")
        self.rect = self.image.get_rect()

        
        
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

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,alienbullets,alien):
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()
    alienbullets.empty()
    alien.rect.x = 0
    time.sleep(0.5)
    


def run_game():
    global bullets_die,ch
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    stats = GameStats(ai_settings)

    aliens = Group()
    alienbullets = Group()
    alien = Alien(ai_settings,screen)
    aliens.add(alien)
      # aliens.add(alien)


    bg_color = (20,250,200)
    while True:
        
                
            
            
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
                    if len(bullets) < ai_settings.bullet_allowed:

                        new_bullet = Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)       


                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False

        ship.update()
        bullets.update()
        for bullet in alienbullets.copy():
            if bullet.rect.bottom >= ai_settings.screen_height or bullet.rect2.bottom >= ai_settings.screen_height or bullet.rect2.bottom >= ai_settings.screen_height:

                alienbullets.remove(bullet)
        
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        
        screen.fill(ai_settings.bg_color)
        for alien in aliens.sprites():
            tre = randint(-1000,1000)
            if tre == 0:
                new_bullet = alienBullet(ai_settings,screen,alien)
                alienbullets.add(new_bullet)
            
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
            
            if len(aliens) ==  0:
                bullets.empty()

        ship.blitme()
        aliens.draw(screen)
        alien.blitme()
        chek_fleet_edges(ai_settings,aliens)
        aliens.update()
        alien.update()
        alienbullets.update(alienbullets,aliens)
        if pygame.sprite.spritecollideany(ship,alienbullets):
            break
        if pygame.sprite.spritecollideany(alien,bullets):
            new_bullet = alienBullet(ai_settings,screen,alien)
            alienbullets.add(new_bullet)
            ch = ch - 1
            if ch <= 0:
                print('you win')
            if ch <= 225:
                ai_settings.alien_bullet_width = 300
        pygame.display.flip()

run_game()