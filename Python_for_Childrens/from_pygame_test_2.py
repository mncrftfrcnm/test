import pygame
import sys
screeen_width = int(input('what width of screen do you wanna: '))
screeen_height = int(input('what heght of screen do you wanna: '))
Ship_speed = int(input('what speed of ship do you wanna: '))
class Settings():
    def __init__(self):
        global screeen_height,screeen_width,Ship_speed
        self.screen_width = screeen_width
        self.screen_height = screeen_height
        self.bg_color = (20,250,200)
        self.ship_speed_factor = Ship_speed
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
        

def run_game():
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
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
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.movin_right = False
                if event.key == pygame.K_LEFT:
                    ship.movin_left = False 
        ship.update()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
run_game()