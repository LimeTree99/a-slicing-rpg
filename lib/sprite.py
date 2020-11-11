import pygame
from lib.color import *
from lib import Particle, Particles


class Sprite:
    def __init__(self, display, pos, push, friction, max_velocity):
        self.display = display
        self.pos = pos
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.push = push
        self.friction = friction
        self.max_v = max_velocity
        self.left = False
        self.down = False
        self.up = False
        self.right = False
        self.downpace = False

        self.radious = 40

    def set_left(self, val):
        self.left = val

    def set_down(self, val):
        self.down = val

    def set_up(self, val):
        self.up = val

    def set_right(self, val):
        self.right = val

    def draw(self, camera):
        pygame.draw.circle(self.display, white, [int(self.pos[0]-camera[0]), int(self.pos[1] - camera[1])], self.radious)

    def change_values(self):
        self.vx += self.ax
        new_x = self.pos[0] + self.vx

        self.vy += self.ay
        new_y = self.pos[1] + self.vy

        if self.vx > self.max_v:
            self.vx = self.max_v
        if self.vy > self.max_v:
            self.vy = self.max_v
        if self.vx < -self.max_v:
            self.vx = -self.max_v
        if self.vy < -self.max_v:
            self.vy = -self.max_v

        
        if self.vx < self.friction and self.vx > -self.friction and \
           (not self.left) and (not self.right):
            self.vx = 0
            
        if self.vx < 0:
            self.vx += self.friction
        elif self.vx > 0:
            self.vx -= self.friction

        if self.vy < self.friction and self.vy > -self.friction and \
           (not self.up) and (not self.down):
            self.vy = 0
        if self.vy < 0:
            self.vy += self.friction
        elif self.vy > 0:
            self.vy -= self.friction

        return new_x, new_y

    def update(self):       
        # these reset acceleration to 0 when a button is not pressed
        if not (self.left and self.right):
            self.ax = 0

        if not (self.up and self.down):
            self.ay = 0

        if self.right:
            self.ax = self.push
        if self.left:
            self.ax = -self.push
        if self.down:
            self.ay = self.push
        if self.up:
            self.ay = -self.push

        self.pos = self.change_values()


class P_sprite(Sprite):
    def __init__(self, display, pos, push, friction, max_velocity):
        super().__init__(display, pos, push, friction, max_velocity)
        self.particles = Particles(self.display, self.pos)

    def update(self):
        super().update()
        self.particles.pos = self.pos
        self.particles.update()

    def draw(self, camera):
        
        self.particles.draw(camera)


class projectile:
    def __init__(self, display, pos):
        self.display = display
        self.pos = pos
        self.color = red
        self.rad = 30

    def update(self):
        pass

    def draw(self, camera):
        pygame.draw.circle(self.display, self.color, (int(self.pos[0] - camera[0]),\
            int(self.pos[1] - camera[1])), int(self.rad))



