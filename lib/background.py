import pygame


class Background:
    def __init__(self, display):
        self.display = display

    def update(self):
        pass

    def rect(self, color, rect):
        pygame.draw.rect(self.display, color,rect)

    def draw(self, camera):
        self.rect((10,100, 200), (100 - camera[0],100 - camera[1],100,100))