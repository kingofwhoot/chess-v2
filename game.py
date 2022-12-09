import pygame

from screen import *
from board import Board
class Play:

    def __init__(self):
        self.board = Board()

    def show_bg(self,surface):
        for row in range(rows):
            for col in range(columns):
                if (row + col) % 2 == 0:
                    colour = (181,93,22) #colour brown
                else:
                    colour = (232,196,125) #colour tan

                rect = (col * square_size, row * square_size, square_size, square_size)

                pygame.draw.rect(surface, colour, rect)

    ###checking if piece is on a square we want, saving piece to variable, centering img
    def show_piece(self, surface):
        for row in range(rows):
            for col in range(columns):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    #using pygame.image.load to convert texture into an image
                    img = pygame.image.load(piece.texture)
                    img_center = col * square_size + square_size // 2,  row * square_size + square_size // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    #using blit to recieve object to blit on screen
                    surface.blit(img,piece.texture_rect)
