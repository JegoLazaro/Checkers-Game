import pygame
from checkers.const_val import *
from checkers.board import Board
from game_system import Game_Sys

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # To display the whole board for the gui of the game
pygame.display.set_caption('CHECKERS') # Title that appears at the top of the interface

FPS = 60

def get_row_col_mouseclick(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game_Sys(WIN)

    """
    TEST FOR PIECE MOVEMENT
    piece = board.get_piece(0,1)

    board.move(piece, 4, 3)
    """

    while(run):
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_mouseclick(pos)
                if game.turn == RED:
                    game.select(row,col)

        game.update()
            
    pygame.quit()

main()