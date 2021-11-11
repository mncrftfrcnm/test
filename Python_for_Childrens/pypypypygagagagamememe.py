import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import *
turn = 0
from time import *
inputt = 1
if inputt == 1:
    computer_health = 5
    speed = 0.1
if inputt == 2:
    computer_health = 20
    speed = 0.2
reserve = computer_health
def chek_fleet_duraction(ai_settings,aliens):
    ai_settings.fleet_direction *= -1
    

def chek_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.chek_edges():
            print('p')
#            chek_fleet_duraction(ai_settings,aliens)
            break


bullets_die = True

def get_number_rows(ai_settings,ship_height,alien_height):
    available_spase_y = ((ai_settings.screen_height - 4*alien_height) - ship_height)
    number_rows = int(available_spase_y / (3*alien_height))
    return number_rows

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
        self.alien_speed_factor = 0.1
        self.bullet_width = 4
        self.bullet_height = 4
        self.bullet_allowed =  133
class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        global turn
        super(Bullet, self).__init__()
        self.screen = screen
        self.turn = turn
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        if self.turn == 0:
            self.x += self.speed_factor
            self.rect.x = self.x
        if self.turn == 1:
            self.x -= self.speed_factor
            self.rect.x = self.x
        if self.turn == 2:
            self.y -= self.speed_factor
            self.rect.y = self.y

        
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.jump = 1

        self.image = pygame.image.load("tree.gif")
        self.rect = self.image.get_rect()
        self.movin_right = False
        self.movin_left = False
        self.ai_settings = ai_settings
        self.alien_speed_factor = 1
        self.up = False
        
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.senter = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
    def update(self):
        if self.movin_right:
            #self.rect.centerx += 1
            self.senter += self.ai_settings.ship_speed_factor

        if self.movin_left and self.rect.left > 0:
            #self.rect.centerx -= 1
            self.senter -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.senter
        if self.up and self.jump == 1:
            self.jump = 0
            for x in range(100):
                print("P")
                self.bottom -= 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
                self.rect.bottom = self.bottom
            for x in range(100):
                self.bottom += 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
                self.rect.bottom = self.bottom
            self.jump = 1
            self.up = False
    def forward(self):
        self.senter = 0
        self.rect.centerx = self.senter
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
    def __init__(self,ai_settings,screen,ship,x,y):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.pos_x = x
        self.pos_y = y
        self.image = pygame.image.load("fire.gif")
        self.rect = self.image.get_rect()
        self.rect2 = self.ship.image.get_rect()
        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.y = y
        self.x = x
        self.rect.x = self.x
        self.rect.y = self.y
        self.pos_x = x
        self.pos_y = y
        
        self.speed = self.ai_settings.alien_speed_factor

    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def chek_edges(self):
        #screen_rect = self.screen.get_rect()

        if self.rect.right >= self.pos_x+400:
            return True
        if self.rect.left <= self.pos_x-400:
            return True
    def forward(self):
        self.x -= 100
        self.rect.x = self.x

    def update(self):


        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
        

        

        
class Block(Sprite):
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

        
    def update(self):

        
        pass
        



def run_game():
    global bullets_die,turn,computer_health,reserve
    pygame.init()
    ai_settings =Settings()
    f = 1
    b =1
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()


            
        
        
        #    print(alien.rect.y)

    alien = Alien(ai_settings,screen,ship,700,700)


    aliens.add(alien)
    aliens.remove(alien)
      # aliens.add(alien)
    alien = Alien(ai_settings,screen,ship,700,700)


    aliens.add(alien)

    bg_color = (20,250,200)
    while True:
        if f == 0:
            for alien in aliens.sprites():

                alien.x -= 1
                alien.pos_x += 1
                alien.rect.x = alien.x

        if b == 0:
            for alien in aliens.sprites():

                alien.x += 1
                alien.pos_x += 1
                alien.rect.x = alien.x
        
                
            
            
            #    print(alien.rect.y)
        tre = randint(-100,1005)

                
                    
        for event in pygame.event.get():

                
        #for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                alien = Alien(ai_settings,screen,ship,x,y)


                aliens.add(alien)

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
                    
                    f = 0
                    turn = 0
                if event.key == pygame.K_UP: 
                    
            
                    turn = 2
                if event.key == pygame.K_d: 
                    
            
                    ship.up = True
                if event.key == pygame.K_SPACE:
                    if len(bullets) < ai_settings.bullet_allowed:

                        new_bullet = Bullet(ai_settings,screen,ship)
                        bullets.add(new_bullet)       





                if event.key == pygame.K_LEFT:
                    b = 0
                    turn = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    f = 1
                if event.key == pygame.K_LEFT:
                    b = 1

        ship.update()
        aliens.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.x <= 0:
                bullets.remove(bullet)
            if bullet.rect.x >= ai_settings.screen_width:
                bullets.remove(bullet)
            if bullet.rect.y <= 0:
                bullets.remove(bullet)
             
        screen.fill(ai_settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
            first = randint(0,200)
            second = randint(0,200)
            three = randint(0,200)
            ai_settings.bullet_color = (first,second,three)
            collisions = pygame.sprite.groupcollide(bullets,aliens,False,False)
            collisions = pygame.sprite.groupcollide(bullets,aliens,bullets_die,True)
        collisions = pygame.sprite.groupcollide(bullets,aliens,bullets_die,True)
        aliens.update()
                                  











                                  
        ship.blitme()
        aliens.update()
        aliens.draw(screen)

        alien.blitme()
        aliens.draw(screen)
        chek_fleet_edges(ai_settings,aliens)
        aliens.update()
        chek_fleet_duraction(ai_settings,aliens)
        chek_fleet_duraction(ai_settings,aliens)
        if pygame.sprite.spritecollideany(ship,aliens):
            print('you lose')
            sys.exit()
        
                
    #    print(len(bullets))
        aliens.update()
        aliens.draw(screen)
        pygame.display.flip()
while True:

    run_game()