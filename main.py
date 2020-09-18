import pygame, math
from pathlib import Path
from random import randint
from lib import color, P_sprite, Window, \
                Background, Camera, Animate, \
                chance, Particles, Particle, GUI



class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = P_sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)

        self.label = GUI.Label(self.display, (10,10), \
                                "Welcome to the start of the game!")

        self.keydict = {pygame.K_w:self.aron.set_up, 
                        pygame.K_s:self.aron.set_down, 
                        pygame.K_a:self.aron.set_left,
                        pygame.K_d:self.aron.set_right}
        
        self.render_list = [self.bg, self.aron]


    def update(self):
        for item in self.render_list:
            item.update()
            
        self.camera.go_to(self.aron.pos)

    def draw(self):
        for item in self.render_list:
            item.draw(self.camera.get_pos())

        self.label.draw()

    def keydown(self, key):
        super().keydown(key)
        for k in self.keydict.keys():
            if key == k:
                self.keydict[k](True)

    def keyup(self, key):
        for k in self.keydict.keys():
            if key == k:
                self.keydict[k](False)

class main(main_w_aron):
    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    print('----START----')
    main().run()
    print('----END----')




