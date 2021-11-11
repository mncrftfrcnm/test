import pygame
import time
import sys

pygame.init()
sc = pygame.display.set_mode((1200, 800))

color_screen=(34,139,34)
color_line=(0,0,255)
sc.fill(color_screen)
# imga = pygame.image.get('BG.jpg')

# imga.blitme()
rect_side=74
y_step=0
x_step=0

for y_coord in range (20):
    y_step=y_coord*rect_side
    for x_coord in range (20):
        x_step=x_coord*rect_side
        pygame.draw.polygon(sc, color_line, [[0+x_step, 0+y_step], [rect_side+x_step, 0+y_step], [rect_side+x_step, rect_side+y_step], [0+x_step, rect_side+y_step]], 2)
        pygame.display.flip()
pygame.image.save(sc,"screenshot2.jpg")