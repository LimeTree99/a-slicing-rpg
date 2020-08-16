import pygame, math
from pathlib import Path
from random import randint
from lib import color, P_sprite, Window, \
                Background, Camera, Animate, \
                chance, Particles, Particle
<<<<<<< HEAD
from lib import color, Sprite, Window, Background, Camera, Animate


class GUI:
    FONT = 'images/font/dum3.ttf'
    class Frame:
        def __init__(self, display, rect):
            self.display = display
            self.rect = rect

    class Label(Frame):
        def __init__(self, display, pos, text='', font_size=20, char_width=20):
            super().__init__(display, [pos[0], pos[1], 0, 0])
            self.pos = pos
            self.text = text
            self.char_width = char_width
            self.font = pygame.font.Font(GUI.FONT, font_size)
            self.fg = color.white
            self.bg = None
            self.image = None
            self.generate()

        def generate(self):
            lines = self.text.split('\n')
            fonts = []
            width = 0
            height = 0
            
            for section in self.text.split('\n'):
                prev = 0
                end = False
                while not end:
                    if  prev + self.char_width > len(section):
                        space_pos = len(section)
                        end = True
                    else:
                        space_pos = prev + self.char_width
                        for i in range(space_pos, prev, -1):
                            if section[i] == ' ':
                                space_pos = i
                                break
                    if section[prev] == ' ':
                        prev += 1
                    font = self.font.render(section[prev:space_pos], True, self.fg, self.bg)
                    prev = space_pos

                    fonts.append(font)
                    height += font.get_height()
                    if font.get_width() > width:
                        width = font.get_width()
                    
            
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            for i in range(len(fonts)):
                self.image.blit(fonts[i], (0, i * fonts[i].get_height()))


        def set_text(self, text):
            self.text = text
            self.generate()

        def draw(self):
            self.display.blit(self.image, self.pos)


    class Button(Label):
        def __init__(self, display, rect, comand):
            super().__init__(display, rect)
            self.comand = comand
        
        
=======
from random import randint
from lib import color, P_sprite, Window, \
                Background, Camera, Animate, \
                chance, Particles, Particle


>>>>>>> particles
class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = P_sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)

        

<<<<<<< HEAD
        self.label = GUI.Label(self.display, (10,10), \
                                "Hi there what is going on there, is the line splitting working properly. I really hope so beacuse then I wouldn't have to fix anything\nsecond")
        
=======
        self.render_list = [self.bg, self.aron]

>>>>>>> particles

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




