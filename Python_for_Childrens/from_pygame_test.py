import pygame
import sys
import random
images = ['cat1.gif','cat2.gif','tree.gif']
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20,250,200)
        
class Ship():
    def __init__(self,screen):
        self.screen = screen
        image = random.choice(images)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.movin_right = False
        self.movin_left = False
        self.movin_down = False
        self.movin_up = False
            
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def update(self):
        if self.movin_right:
            self.rect.centerx += 1
        if self.movin_left:
            self.rect.centerx -= 1
        if self.movin_up:
            self.rect.bottom -= 1
        if self.movin_down:
            self.rect.bottom += 1
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        

def run_game():
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    bg_color = (20,250,200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    
                    ship.movin_right = True
                if event.key == pygame.K_LEFT:
                    ship.movin_left = True
                if event.key == pygame.K_DOWN:
                    
                    ship.movin_down = True
                if event.key == pygame.K_UP:
                    ship.movin_up = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False
                if event.key == pygame.K_DOWN:
                    
                    ship.movin_down = False
                if event.key == pygame.K_UP:
                    ship.movin_up = False
            
        ship.update()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        image = random.choice(images)
        ship.image = pygame.image.load(image)
        pygame.display.flip()
run_game()