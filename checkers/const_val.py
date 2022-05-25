import pygame

# BOARD SIZE INITS
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8 
SQUARE_SIZE = WIDTH//COLS

# COLOR RGB INITS
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 204, 0)
GREY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (45,25))