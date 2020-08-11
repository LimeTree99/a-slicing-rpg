import pygame, math
from pathlib import Path
from random import randint
from lib import color, Sprite, Window, \
                Background, Camera, Animate, \
                chance
        
class Particle:
    def __init__(self, display, pos):
        self.display = display
        self.pos = pos
        self.image = self.generate()
        self.ticks = 0

    def tick(self):
        self.ticks += 1
    
    def get_ticks(self):
        return self.ticks

    def generate(self):
        r = 5
        image = pygame.Surface((r*2,r*2), pygame.SRCALPHA, 32)
        image = image.convert_alpha()
        image.set_colorkey((255,0,255))
        pygame.draw.circle(image, color.red, (r, r), r)
        return image

    def move(self, pos):
        self.pos = (self.pos[0] + pos[0], self.pos[1] + pos[1])

    def draw(self, camera):
        self.display.blit(self.image, (int(self.pos[0])-camera[0], int(self.pos[1])-camera[1]))

class Particles:
    def __init__(self, display, pos):
        self.display = display
        self.pos = pos
        self.objs = []

    def generate(self):
        if chance(20):
            self.objs.append(Particle(self.display, self.pos))

    def remove(self, particle):
        if particle.ticks > 100:
            return True
        else:
            return False

    def move(self, particle):
        particle.move((randint(-1, 1), randint(-2,1)))

    def update(self):
        self.generate()
        for i, particle in enumerate(self.objs):
            particle.tick()
            if self.remove(particle):
                self.objs.pop(i)
            self.move(particle)
        

    def draw(self, camera):
        for particle in self.objs:
            particle.draw(camera)

class Custom_p(Particle):
    def __init__(self, display, pos, color, size):
        self.color = color
        self.size = size
        self.area = 10
        super().__init__(display, pos)
        

    def generate(self):
        r = self.size
        image = pygame.Surface((r*2,r*2), pygame.SRCALPHA, 32)
        image = image.convert_alpha()
        image.set_colorkey((255,0,255))
        pygame.draw.circle(image, self.color, (r, r), r)
        return image

class Smoke(Particles):
    def __init__(self, display, pos):
        super().__init__(display, pos)
        
    def generate(self):
        for perc, col, size in [(50, (50,50,50), 2), \
                            (50, (100,100,100), 3), \
                            (50, (150,150,150), 3)]:
            if chance(perc):
                self.objs.append(Custom_p(self.display, self.pos, col, randint(1,10)))
                
    def remove(self, particle):
        if particle.ticks > 500:
            return True
        else:
            return False

    def move(self, particle):
        if chance(100):
            particle.move((randint(-1, 1), randint(-1, 1)))





class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = Sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)
        self.efect = Smoke(self.display, (-400, 0)) 

        self.animate = Animate(self.display, (10, 50), "character.png", "sprite", (64, 64), 1000)

        self.render_list = [self.bg, self.aron, self.animate, \
                            Smoke(self.display, (-400, 0)), \
                            Smoke(self.display, (-500, 0))]


    def update(self):
        for item in self.render_list:
            item.update()
            
        self.camera.go_to(self.aron.pos)

    def draw(self):
        for item in self.render_list:
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




