import pygame, math
from pathlib import Path
from lib import color, Sprite, Window, Background, Camera


class Alarm:
    '''
    returns true every time the 'timer' function is called after the given interval
    or after the "alarm" goes off
    '''
    def __init__(self, interval):
        self.old_time = 1
        self.time_ongoing = 0
        self.interval = interval

    def timer(self):
        time = pygame.time.get_ticks()
        if time - self.old_time >= self.interval:
            self.old_time = time
            return True
        return False


class Animate:
    def __init__(self, display, pos, image_name, type, split_size, fr_time, folder=Path().absolute()):
        self.display = display
        self.pos = pos
        self.image_name = image_name
        self.type = type
        self.split_size = split_size
        self.fr_time = fr_time
        self.swap = Alarm(fr_time)
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

<<<<<<< HEAD
    def draw(self, pos):
        self.display.blit(self.current_frame(self.state), (self.pos[0] - pos[0], self.pos[1] - pos[1]))
      
        
=======
        self.display.blit(self.frames[self.frame], pos)

  
>>>>>>> master
class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = Sprite(self.display, (0,0), 1, 0.5, 20)
        self.bg = Background(self.display)

        self.animate = Animate(self.display, (10, 50), "character.png", "sprite", (64, 64), 1000)



    def update(self):
        self.bg.update()
        self.aron.update()
        self.animate.update()

        self.camera.go_to(self.aron.pos)

    def draw(self):
        
        self.bg.draw(self.camera.get_pos())
        self.aron.draw(self.camera.get_pos())
        self.animate.draw(self.camera.get_pos())

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




