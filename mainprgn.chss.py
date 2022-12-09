import pygame
import sys

from screen import *
from game import Play

class Main:

    def __init__(self):
        pygame.init()
        self.screenmake = pygame.display.set_mode( (width, length) )
        pygame.display.set_caption("Chess")
        self.game = Play()

    def mloop(self):

        while True:
            self.game.show_bg(self.screenmake)
            self.game.show_piece(self.screenmake)
           
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




            pygame.display.update()

main = Main()
main.mloop()
