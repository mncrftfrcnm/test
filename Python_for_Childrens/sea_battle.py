import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *
patrons = 200
def chek_fleet_duraction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    ai_settings.alien_speed_factor += 0.01

def chek_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.chek_edges():
            chek_fleet_duraction(ai_settings,aliens)
            break
        

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
    alien.x = randint(0,700)
    alien.rect.x = alien.x
 #   alien_width = alien.rect.width
    
    alien.y = randint(0,700)
    alien.rect.y = alien.y
    aliens.add(alien)
    print(alien.x,alien.y)

class Settings():
    def __init__(self):
        self.fleet_diraction = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.screen_width = 1200
        self.bullet_speed_factor = 3
        self.screen_height = 800
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
        pass
    def blitme(self):
        self.screen.blit(self.image,self.rect)
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        

        self.image = pygame.image.load("nothing.gif")
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


        self.x +=0

        
class Blocks(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        

        self.image = pygame.image.load("nothing.gif")
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

        



def run_game():
    global bullets_die
    
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
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
                # if event.key == pygame.K_SPACE:
                #     if len(bullets) < ai_settings.bullet_allowed:

                #         new_bullet = Bullet(ai_settings,screen,ship)
                #         bullets.add(new_bullet)       


                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                for alien in aliens.sprites():
                    if alien.rect.collidepoint(mouse_x,mouse_y):
                        aliens.remove(alien)
                        print(len(aliens))
                        if len(aliens) < 1:
                            print('you win')
                            break
        ship.update()
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
                # for row_number in range(number_rows):
                #     for alien_number in range(number_aliens_x):
                            
                        
                        
                #         #    print(alien.rect.y)
                        
                #         create_alien(ai_settings,screen,aliens,alien_number,row_number)
        ship.blitme()
        aliens.draw(screen)
        alien.blitme()
        chek_fleet_edges(ai_settings,aliens)
        aliens.update()
        if pygame.sprite.spritecollideany(ship,aliens):
            pass
        pygame.display.flip()
while True:
    run_game()