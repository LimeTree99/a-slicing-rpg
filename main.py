import pygame, math
from pathlib import Path
from random import randint
from lib import color, P_sprite, Window, \
                Background, Camera, Animate, \
                chance, Particles, Particle, GUI, projectile





class main_w_aron(Window):
    def __init__(self, name):
        super().__init__(name)
        
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)
        self.camera_follow = None       #set this to an object with a .pos to have the camera follow it
        self.render_list = []           #render relitive to camera
        self.ui_render_list = []        #render without camera interference
        self.keydict = {pygame.K_ESCAPE:self.quit}

    def update(self):
        for item in self.render_list:
            item.update()
        if self.camera_follow is not None:
            self.camera.go_to(self.camera_follow.pos)

    def draw(self):
        
        for item in self.render_list:
            item.draw(self.camera.get_pos())

        for item in self.ui_render_list:
            item.draw()

    def quit(self, arg):
        self.end = True

    def keydown(self, key):
        for k in self.keydict.keys():
            if key == k:
                self.keydict[k](True)

    def keyup(self, key):
        for k in self.keydict.keys():
            if key == k:
                self.keydict[k](False)


class main(main_w_aron):
    def __init__(self):
        super().__init__("GAME!!")
        self.aron = P_sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)

        self.camera_follow = self.aron

        self.label = GUI.Label(self.display, "nw", "Welcome to the start of the game!")

        self.keydict = {pygame.K_ESCAPE:self.quit,
                        pygame.K_w:self.aron.set_up, 
                        pygame.K_s:self.aron.set_down, 
                        pygame.K_a:self.aron.set_left,
                        pygame.K_d:self.aron.set_right}
        
        self.render_list = [self.bg, self.aron]
        self.ui_render_list = [self.label]


if __name__ == "__main__":
    print('----START----')
    main().run()
    print('----END----')




