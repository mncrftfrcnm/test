import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *
import time
turn = 0
inputt = 1
if inputt == 1:
    computer_health = 5
    speed = 0.1
if inputt == 2:
    computer_health = 20
    speed = 0.2
reserve = computer_health
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
    alien.x = 0
    alien.rect.x = alien.x
 #   alien_width = alien.rect.width
    
    alien.y = 710
    alien.rect.y = alien.y
    aliens.add(alien)

class Settings():
    def __init__(self):
        global speed
        self.fleet_diraction = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.screen_width = 1200
        self.bullet_speed_factor = 0.5
        self.screen_height = 800
        self.bg_color = (20,250,200)
        self.ship_speed_factor = 1
        self.bullet_color = 60,60,60
        self.alien_speed_factor = speed
        self.bullet_width = 4
        self.bullet_height = 4
        self.bullet_allowed =  133
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship,aliens,bullets,alien,mouse_x,mouse_y):
        super(Bullet, self).__init__()
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
           
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen

        self.image = pygame.image.load("tree.gif")
        self.rect = self.image.get_rect()
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        
            
            
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.senter = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        self.movin_down = False
        self.movin_up = False
                
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


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
    def jump(self):
        for x in range(1000):
            self.y -= 1
            self.blitme()
    
    #        time.sleep(0.1)
            self.rect.bottom = self.y
            
        for x in range(1000):
            self.y += 1
            
            self.blitme()
    
            self.rect.bottom = self.y
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

def run(ship,turn):
    if turn == 0:
        ship.senter+= 400
        ship.rect.centerx = ship.senter
    
    if turn == 1:
        ship.senter-= 400
        ship.rect.centerx = ship.senter
    
class Alien(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Alien, self).__init__()
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
        self.speed = self.ai_settings.alien_speed_factor

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

        



def run_game():
    global bullets_die,turn,computer_health,reserve
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    alien = Alien(ai_settings,screen,ship)
    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    alien.y = -90
    alien.rect.y = alien.y

            
        
        
        #    print(alien.rect.y)
           
    alien = Alien(ai_settings,screen,ship)

    alien_width = alien.rect.width
    available_spase_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_spase_x / (2*alien_width))
    alien.x = 128
    alien.rect.x = alien.x
 #   alien_width = alien.rect.width
    
    alien.y = 710
    alien.rect.y = alien.y
    aliens.add(alien)
      # aliens.add(alien)


    bg_color = (20,250,200)
    while True:
        
                
            
            
            #    print(alien.rect.y)
        tre = randint(-100,1005)

                
                    
        for event in pygame.event.get():

                
        #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                new_bullet = Bullet(ai_settings,screen,ship,aliens,bullets,alien,mouse_x,mouse_y)
                bullets.add(new_bullet)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    first = randint(0,220)
                    second = randint(0,220)
                    three = randint(0,220)
                    ai_settings.bg_color = (first,second,three)
                if event.key == pygame.K_n:
                    run(ship,turn)
                
                if event.key == pygame.K_b:
                    sys.exit()
                if event.key == pygame.K_RIGHT: 
                    
                    ship.movin_right = True
                    turn = 0
                if event.key == pygame.K_UP: 
                    
                    ship.movin_up = True
                    turn = 0
                if event.key == pygame.K_h: 
                    
                    ship.jump()
                    
                if event.key == pygame.K_DOWN: 
                    
                    ship.movin_down = True
                    turn = 0
                if event.key == pygame.K_SPACE:
                    if len(bullets) < ai_settings.bullet_allowed:

                        new_bullet = Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)       





                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
                    turn = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False
                if event.key == pygame.K_UP: 
                    
                    ship.movin_up = False
                    turn = 0
                if event.key == pygame.K_DOWN: 
                    
                    ship.movin_down = False
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.x <= 0:
                bullets.remove(bullet)
            if bullet.rect.x >= ai_settings.screen_width:
                bullets.remove(bullet)
             
        screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
            first = randint(0,200)
            second = randint(0,200)
            three = randint(0,200)
            ai_settings.bullet_color = (first,second,three)
            
            
            
        ship.blitme()
        aliens.draw(screen)
        alien.blitme()
        chek_fleet_edges(ai_settings,aliens)
        aliens.update()
        if pygame.sprite.spritecollideany(ship,aliens):
            print('you lose')
            computer_health = reserve
            break
        if pygame.sprite.spritecollideany(alien,bullets):
            computer_health -= 1
            print(computer_health)
            if computer_health <=0:
                print('you win')
                sys.exit()
            bullets.empty()
        alien.update()
        pygame.display.flip()
while True:

    run_game()