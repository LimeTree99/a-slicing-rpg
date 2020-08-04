import pygame
from lib import color, Sprite, Window, Background, math


class Shift_sprite(Sprite):
    def __init__(self, display, pos, push, friction, max_velocity):
        super().__init__(display, pos, push, friction, max_velocity)

        self.onscreen_pos = pos
        self.curr_onscreen_pos = pos
        self.accelerate = 5

    def draw(self):
        pygame.draw.circle(self.display, color.white, self.onscreen_pos, self.radious)

    def to_onscreen_pos(self):
        if self.onscreen_pos != self.curr_onscreen_pos:
            pass

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
    def __init__(self, display, fr_time, frames, start_frame=0):
        self.display = display
        self.fr_time = fr_time
        self.frames = frames
        self.frame = start_frame
        self.start_frame = start_frame
        self.swap = Alarm(fr_time)


    def update(self, pos):
        if self.swap.timer():
            # go to next frame
            if self.frame >= len(self.frames)-1:
                self.frame = 0
            else:
                self.frame += 1

        self.display.blit(self.frames[self.frame], pos)
        

    
            
        
class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.aron = Shift_sprite(self.display, 
                                (self.display.get_width() // 2, 
                                self.display.get_height() // 2), 
                                1, 0.5, 20)

        self.bg = Background(self.display)
    
    def update(self):
        self.bg.rect(color.green, (100,100,100,300))
        self.bg.update((self.aron.x, self.aron.y))

        self.aron.update()


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
    main().run()
    print('----END----')




