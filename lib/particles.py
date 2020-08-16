import pygame
from random import randint
from lib import color

class Particle:
    def __init__(self, pos, volocity, color, rad, shrink, gravity=0):
        self.pos = [pos[0], pos[1]]
        self.vol = [volocity[0], volocity[1]]
        self.color = color
        self.rad = rad
        self.shrink = shrink
        self.gravity = gravity

class Particles:
    def __init__(self, display, pos):
        self.display = display
        self.pos = pos
        self.list = []

    def generate(self):
        self.list.insert(0, Particle(pos=self.pos, \
                                  volocity=(randint(0, 20) / 10 - 1, -2), \
                                  color=color.randgray(10, 255), \
                                  rad=randint(15, 17), \
                                  shrink=randint(1,20) / 20,\
                                  gravity=-0.01))

    def update(self):
        self.generate()
        i = 0
        while i < len(self.list):
            particle = self.list[i]

            particle.pos[0] += particle.vol[0]
            particle.pos[1] += particle.vol[1]
            particle.rad -= particle.shrink
            particle.vol[1] -= particle.gravity
            
            
            if particle.rad <= 0:
                self.list.pop(i)
                i += 1
            i += 1

    def draw(self, camera):
        for particle in self.list:
            pygame.draw.circle(self.display, particle.color, \
                                (int(particle.pos[0] - camera[0]), \
                                int(particle.pos[1] - camera[1])), \
                                int(particle.rad))
