import pygame


class Background:
    def __init__(self, display):
        self.display = display
        self.pos = (0,0)

    def update(self, pos):
        self.pos = pos

    def rect(self, color, rect):
        pygame.draw.rect(self.display, color, 
                        [rect[0] + self.pos[0], rect[1] + self.pos[1], rect[2], rect[3]])

        