import pygame
FPS = 60
pygame. init()
pygame.mixer.quit()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(r'C:\Python27\video\test-mpeg.mpg')
screen = pygame.display.set_mode(movie.get_size)
movie_screen = pygame.Surface(movie. get_size()).convert(screen)
