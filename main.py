import pygame
from checkers.const_val import *
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('CHECKERS')

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while(run):
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_cubes(WIN)
        pygame.display.update()
        number = 1
        word = 'two'
            
    pygame.quit()

main()