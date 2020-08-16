import pygame, math
from pathlib import Path
from random import randint
from lib import color, Sprite, Window, \
                Background, Camera, Animate, \
                chance, Particles


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


class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = P_sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)

        self.animate = Animate(self.display, (10, 50), "character.png", "sprite", (64, 64), 1000)

        self.render_listt = [self.bg, self.aron, self.animate]


    def update(self):
        for item in self.render_listt:
            item.update()
            
        self.camera.go_to(self.aron.pos)

    def draw(self):
        for item in self.render_listt:
            item.draw(self.camera.get_pos())

    def keydown(self, key):
        super().keydown(key)
        if key == pygame.K_w:
            self.aron.up = True
        if key == pygame.K_s:
            self.aron.down = True
        if key == pygame.K_a:
            self.aron.left = True
        if key == pygame.K_d:
            self.aron.right = True

    def keyup(self, key):
        if key == pygame.K_w:
            self.aron.up = False
        if key == pygame.K_s:
            self.aron.down = False
        if key == pygame.K_a:
            self.aron.left = False
        if key == pygame.K_d:
            self.aron.right = False

class main(main_w_aron):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    print('----START----')
    main().run()
    print('----END----')




