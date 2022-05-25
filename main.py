import pygame
from checkers.const_val import *
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # To display the whole board for the gui of the game
pygame.display.set_caption('CHECKERS') # Title that appears at the top of the interface

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

        board.draw(WIN)
        pygame.display.update()
            
    pygame.quit()

main()