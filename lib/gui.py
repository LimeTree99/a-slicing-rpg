import pygame
from lib import color


class GUI:
    FONT = 'images/font/dum3.ttf'
    class Frame:
        def __init__(self, display, place, border):
            self.display = display
            self.place = place
            self.bd = border

        def set_location(self, rect):
            "set self.pos based on the passed in rect and the value of self.place"
            center_x = self.display.get_width() // 2 - rect[2] // 2
            center_y = self.display.get_height() // 2 - rect[3] // 2
            left_x = self.display.get_width() - rect[2] - self.bd
            bottom_y = self.display.get_height() - rect[3] - self.bd
            
            if type(self.place) == list or type(self.place) == tuple:
                self.pos = self.place[0] + self.bd, self.place[1] + self.bd
            elif self.place == 'c' or self.place == 'center':
                self.pos = (center_x, center_y)
            elif self.place == 'n':
                self.pos = (center_x, self.bd)
            elif self.place == 'ne':
                self.pos = (left_x,self.bd)
            elif self.place == 'e':
                self.pos = (left_x, center_y)
            elif self.place == 'se':
                self.pos = (left_x, bottom_y)
            elif self.place == 's':
                self.pos = (center_x, bottom_y)
            elif self.place == 'sw':
                self.pos = (self.bd, bottom_y)
            elif self.place == 'w':
                self.pos = (self.bd, center_y)
            elif self.place == 'nw':
                self.pos = (self.bd, self.bd)

        

    class Label(Frame):
        def __init__(self, display, place, text='', font_size='m', char_width=20, border=10):
            super().__init__(display, place, border)
            self.text = text
            self.char_width = char_width
            self.font_size = self.font_from_sml(font_size)
            self.font = pygame.font.Font(GUI.FONT, self.font_size)
            self.fg = color.white
            self.bg = None
            self.image = None
            self.pos = (0,0)
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
            self.set_location(self.image.get_rect())

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