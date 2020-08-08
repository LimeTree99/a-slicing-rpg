import pygame
from pathlib import Path
from lib import tools


class Animate:
    def __init__(self, display, pos, image_name, type, split_size, fr_time, folder=Path().absolute()):
        self.display = display
        self.pos = pos
        self.image_name = image_name
        self.type = type
        self.split_size = split_size
        self.fr_time = fr_time
        self.swap = tools.Alarm(fr_time)
        self.path = folder.joinpath("images/" + type + '/' + image_name)
        self.screen = self.load_image(self.path)
        self.frame_num = 0
        self.frames = self.split_frames(self.screen, self.split_size)
        self.group = {'all':self.frames}
        self.state = 'all'

    def get_screen(self):
        return self.screen

    def load_image(self, path):
        return pygame.image.load(str(path))

    def split_frames(self, screen, size):
        frames = []
        for x in range(0, screen.get_width(), size[0]):
            for y in range(0, screen.get_height(), size[1]):
                add = screen.subsurface((x, y, size[0], size[1]))
                add = add.copy()
                frames.append(add)
        return frames

    def add_group(self, name, start_fr, end_fr):
        self.group[name] = frames[start_fr : end_fr]

    def next_fr(self, group):
        if self.frame_num >= len(self.frames)-1:
            self.frame_num = 0
        else:
            self.frame_num += 1
        return self.frames[self.frame_num]

    def current_frame(self, group):
        return self.frames[self.frame_num]

    def update(self):
        if self.swap.timer():
            frame = self.next_fr(self.state)

    def draw(self, pos):
        self.display.blit(self.current_frame(self.state), (self.pos[0] - pos[0], self.pos[1] - pos[1]))
      