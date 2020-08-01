import pygame
import sys
import pygame.font

from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *

import time
images = ['cat1.gif','fire.gif','tree.gif']
class Button():
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width,self.heght = 200,50
        self.button_color = (0,255,0)
        self.button_color = (225,255,225)
        self.font = pygame.font.SysFont(None,48)
        self.rect = pygame.Rect(0,0,self.width,self.heght)
        self.rect.center = self.screen_rect.center
        self.text_color = (0,145,123)
        self.prep_msg(msg)
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
            
class Bullet2(Sprite):
    def __init__(self,ai_settings,screen,ship,aliens,bullets,alien,mouse_x,mouse_y):
        super(Bullet2, self).__init__()
        self.mouse_x = mouse_x
        self.trex = 1
        self.trey = 1

        self.mouse_y = mouse_y
        self.mousex = mouse_x
        self.mousey = mouse_y
        self.screen = screen
        self.ai_settings = ai_settings
    
            
            #if randdom == 0:
        self.image = pygame.image.load("leave.gif")
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
            
        self.image = pygame.image.load("branch.gif")
    
    #    self.alien_rect = alien.image.get_rect()
        self.aliens = aliens
        self.bullets = bullets
            
     #   self.alien_rect.centerx = self.alien_rect.centerx
      #  self.alien_rect.bottom = self.alien_rect.bottom
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.rect.bottom = ship.rect.bottom
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        #self.alien_rect.y = float(self.alien_rect.y)
        #self.alien_rect.x = float(self.alien_rect.x)
            
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
            

    def update(self):
        global ch
        global ch
        if self.rect.x > self.mouse_x:
            self.x -= 1
        if self.rect.x < self.mouse_x:
            self.x += 1
        if self.rect.y > self.mouse_y:
            self.y -= 1
        if self.rect.y < self.mouse_y:
            self.y += 1
        self.rect.x = self.x
        self.rect.y = self.y
    def draw_bullet(self):
            
        self.screen.blit(self.image,self.rect)
        
def chek_fleet_duraction(ai_settings,aliens):
    # for alien in aliens.sprites():
    #     alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
 #   ai_settings.alien_speed_factor += 0.01

def chek_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.chek_edges():
            chek_fleet_duraction(ai_settings,aliens)
            break
        
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
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

class Settings():
    def __init__(self):
        self.ships_limit = 3
        self.fleet_diraction = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.screen_width = 1200
        self.bullet_speed_factor = 0.3
        self.screen_height = 800
        self.bg_color = (20,250,200)
        self.ship_speed_factor = 1
        self.bullet_color = 60,60,60
        self.alien_speed_factor = 1
        self.bullet_width = 50
        self.width = 30
        self.height = 30
        self.bullet_height = 50
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
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1
        
        self.movin_down = False
        self.movin_up = False        
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.senter = float(self.rect.centerx)
        self.color = (0,0,0)
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
        pygame.draw.rect(self.screen,self.color,self.rect)
class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
    
        self.screen = screen

        
        self.rect = pygame.Rect(0,0,ai_settings.width,ai_settings.height)
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1
        
        self.movin_down = False
        self.movin_up = False        
        self.screen_rect = screen.get_rect()

        self.senter = float(self.rect.centerx)
        self.x = float(self.rect.x)
        self.color = (0,0,0)
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    def chek_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        
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

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    alien.y = -90
    alien.rect.y = alien.y
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            
        
        
        #    print(alien.rect.y)
           
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
      # aliens.add(alien)
    time.sleep(0.5)
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
            self.rect = pygame.Rect(0,0,10,30)
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

            self.color = ai_settings.bullet_color
            self.speed_factor = 3
            

        def update(self,bullets,aliens):
            global ch
            global ch
            self.y += self.speed_factor
            self.rect.y = self.y
            

        def draw_bullet(self):
            
            pygame.draw.rect(self.screen,self.color,self.rect)
except TimeoutError:
    pass
else:
    pass    


def run_game():
    global bullets_die
    pygame.init()
    ai_settings =Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    alienbullets = Group()
    play_button = Button(ai_settings,screen,'Run!')

    stats = GameStats(ai_settings)

    aliens = Group()
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    
    print(alien.rect.y)
    aliens.add(alien)
    tre = 9
            
        
        
        #    print(alien.rect.y)
           
    #        create_alien(ai_settings,screen,aliens,alien_number,row_number)
      # aliens.add(alien)


    bg_color = (20,250,200)
    while True:
        if not stats.game_active:
            play_button.draw_button()
            for event in pygame.event.get():

                    
            #for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    #for alien in aliens.sprites():
                    if play_button.rect.collidepoint(mouse_x,mouse_y):
                        stats.game_active = True

        if stats.game_active == True:
            if tre == 1:
                break
                
            
                
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
                    
            #             create_alien(ai_se
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    new_bullet = Bullet2(ai_settings,screen,ship,aliens,bullets,alien,mouse_x,mouse_y)
                    bullets.add(new_bullet)                
                    new_bullet.draw_bullet()
                


            #for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_f:
                        print('d')
                        mouse_x,mouse_y = pygame.mouse.get_pos()
                        new_bullet = Bullet2(ai_settings,screen,ship,aliens,bullets,alien,alien.rect.x,alien.rect.y)
                        bullets.add(new_bullet)                
                        new_bullet.draw_bullet()
                        
                    if event.key == pygame.K_8:
                        tre = 1
                    if event.key == pygame.K_1:
                        first = randint(0,220)
                        second = randint(0,220)
                        three = randint(0,220)
                        ai_settings.bg_color = (first,second,three)
                    if event.key == pygame.K_b:
                        stats.game_active = False

                    if event.key == pygame.K_RIGHT: 
                        ship.movin_up = False
                        ship.movin_down = False
                        ship.movin_left = False
                        ship.movin_right = True
                    if event.key == pygame.K_UP:
                        
                        ship.movin_up = True
                        ship.movin_down = False
                        ship.movin_left = False
                        ship.movin_right = False

                    if event.key == pygame.K_DOWN:
                        ship.movin_up = False
                        ship.movin_down = True
                        ship.movin_left = False
                        ship.movin_right = False
                    if event.key == pygame.K_SPACE:
                        if len(bullets) < ai_settings.bullet_allowed:

                            new_bullet = Bullet(ai_settings,screen,ship)
                            bullets.add(new_bullet)       


                    if event.key == pygame.K_LEFT:
                        ship.movin_up = False
                        ship.movin_down = False
                        ship.movin_left = True
                        ship.movin_right = False
                print(event.type)
                    
            bullets.update()

            ship.update()

         #   aliens.update()

            ship.blitme()

            alienbullets.update(bullets,aliens)
            alienbullets.update(bullets,aliens)
            
            ship.blitme()
            
            for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)
                    print('you lose ')
                    sys.exit()
            
            screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
            if pygame.sprite.spritecollideany(alien,bullets):
                bullets.remove(bullet)

        ship.blitme()
    
        bullets.update()
        alien.blitme()
        aliens.update()
        alien.blitme()


    #sys.exit()
                 
            
        #    aliens.add(alien)
        chek_fleet_edges(ai_settings,aliens)

        #
        
        pygame.display.flip()
while True:
    run_game()