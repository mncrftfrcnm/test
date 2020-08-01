import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *
sco  =0
enemy_type = 0
die = 3
time = 0
bullets_die = True
def get_number_rows(ai_settings,ship_height,alien_height):
    available_spase_y = ((ai_settings.screen_height - 3*alien_height) - ship_height)
    number_rows = int(available_spase_y / (2*alien_height))
    return number_rows
def do_new_alien(ai_settings,alien):
    alien.y = 0
    alien.rect.y = alien.y
    random_plase = randint(0,ai_settings.screen_width)
    alien.x = random_plase
    alien.rect.x = alien.x
    ai_settings.alien_speed_factor += 0.03
    
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.bullet_speed_factor = 0.5
        self.screen_height = 800
        self.bg_color = (20,250,200)
        self.ship_speed_factor = 1
        self.alien_speed_factor = 0.1
        self.bullet_color = 60,60,60
        self.bullet_width = 30
        self.bullet_height = 40
        self.bullet_allowed =  3
class bg(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(bg, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('packmanback.jpg')
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
    def draw_bg(self):
        self.screen.blit(self.image,self.rect)

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

        self.image = pygame.image.load("packman.gif")
        self.rect = self.image.get_rect()
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
    
        
        
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
        global time
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.time = time
        self.image = pygame.image.load("cherry.gif")
        self.rect = self.image.get_rect()

        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def update(self):

        self.y += self.ai_settings.alien_speed_factor
        self.rect.y = self.y
        self.y += (9.8*self.time**2) / 2
        self.rect.y = self.y
        self.time += 0.0001



def run_game():
    global sco,enemy_type
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
    b = bg(ai_settings,screen,ship)
    b.draw_bg()
    alien = Alien(ai_settings,screen)

    aliens.add(alien)

        #    print(alien.rect.y)
           
            #reate_alien(ai_settings,screen,aliens,alien_number,row_number)
      # aliens.add(alien)


    bg_color = (20,250,200)
    while True:
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
                    if ai_settings.bullet_allowed>0:

                        new_bullet = Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)     
                        ai_settings.bullet_allowed -= 1  


                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False
           
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
        if pygame.sprite.spritecollideany(alien,bullets):
            if enemy_type == 1:
                
                do_new_alien(ai_settings,alien)
                sco = sco + 1
                ai_settings.bullet_allowed += 1
                tre = randint(0,1)
                enemy_type = tre
                if tre == 1:
                    alien.image = pygame.image.load('bomb.gif')
                else:
                    alien.image = pygame.image.load('cherry.gif')
                #print(enemy_type)
            else:
                print('you lose')
                break
            
    
        ship.blitme()
        aliens.draw(screen)
        alien.blitme()
        aliens.update()
        if pygame.sprite.spritecollideany(ship,aliens):
            alien.time = 0
            if enemy_type == 0:
                
                do_new_alien(ai_settings,alien)
                sco = sco + 1
                tre = randint(0,1)
                enemy_type = tre
                if tre == 1:
                    alien.image = pygame.image.load('bomb.gif')
                else:
                    alien.image = pygame.image.load('cherry.gif')
                #print(enemy_type)
            else:
                print('you lose')
                break
        if alien.rect.y >= 800:
            alien.time = 0
            if enemy_type == 1:
                #print("OJF")
                
                do_new_alien(ai_settings,alien)
                enemy_type = 0
                tre = randint(0,1)
                enemy_type = tre
                if tre == 1:
                    alien.image = pygame.image.load('bomb.gif')
                else:
                    
                    alien.image = pygame.image.load('cherry.gif')

                #print(enemy_type)
            else:
        

                print('you lose, your score is ',sco)

                break
        
        pygame.display.flip()
    
run_game()
while True:
    tre = input('do you want to play again?: ')
    if tre == 'yes':
        sco = 0
        enemy_type = 0
        run_game()
    else:
        print('see you later')
        break