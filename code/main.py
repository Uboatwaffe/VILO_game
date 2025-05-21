import sys

import pygame

from level import Level
from settings import *

'''
This code has been initially made by "Clear Code" https://github.com/clear-code-projects/Zelda
And has been modified by Uboatwaffe (https://github.com/Uboatwaffe) belonging to 3e group for commercial use
The work has started in 18.10.2024 at 20:10 and finished in DD.MM.YYYY

Project Manager: Bartłomiej K.
Supervisors: Maciej P. and Julia N.

Programmers: Maciej P.
Graphic Designers: Paweł P. Konrad K. Bartosz Ż.
Testers: 
Advertisement: Alisa D. Zofia P.
Plot Of The Game:
'''


# TODO: fill credits out


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
