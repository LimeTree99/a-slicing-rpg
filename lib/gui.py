import pygame
from lib import color

class GUI:
    FONT = 'images/font/dum3.ttf'
    class Frame:
        def __init__(self, display, rect):
            self.display = display
            self.rect = rect

    class Label(Frame):
        def __init__(self, display, pos, text='', font_size='m', char_width=20):
            super().__init__(display, [pos[0], pos[1], 0, 0])
            self.pos = pos
            self.text = text
            self.char_width = char_width
            self.font_size = self.font_from_sml(font_size)
            self.font = pygame.font.Font(GUI.FONT, self.font_size)
            self.fg = color.white
            self.bg = None
            self.image = None
            self.generate()

        def generate(self):
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

        def font_from_sml(self, arg):
            if arg == 's' or arg == 'S':
                return int(self.display.get_height() / 54)
            elif arg == 'm' or arg == 'M':
                return int(self.display.get_height() / 37)
            elif arg == 'l' or arg == 'L':
                return int(self.display.get_height() / 20)


    class Button(Label):
        def __init__(self, display, rect, comand):
            super().__init__(display, rect)
            self.comand = comand
