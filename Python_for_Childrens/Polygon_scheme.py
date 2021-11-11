import pygame
import time
import sys

pygame.init()
sc = pygame.display.set_mode((1200, 800))

color_screen=(34,139,34)
color_line=(0,0,255)

sc.fill(color_screen)

y_step=0
x_step=0
x_step_bool=False


for y_coord in range (9):
    y_step=y_coord*90
    if x_step_bool == True:
        x_step_line=51.96
        x_step_bool = False
    else:
        x_step_line=0
        x_step_bool = True
    for x_coord in range (12):
        x_step=x_coord*103.92
        pygame.draw.polygon(sc, color_line, [[0+x_step+x_step_line, 30+y_step], [51.96+x_step+x_step_line, 0+y_step], [103.92+x_step+x_step_line, 30+y_step], [103.92+x_step+x_step_line, 90+y_step], [51.96+x_step+x_step_line,120+y_step], [0+x_step+x_step_line,90+y_step], [0+x_step+x_step_line,30+y_step]], 2)
        pygame.display.flip()
x_step_bool=False
pygame.image.save(sc,"screenshot.jpg")