import pygame, math
from lib import color, Sprite, Window, Background, math


class Shift_sprite(Sprite):
    def __init__(self, display, pos, push, friction, max_velocity):
        super().__init__(display, pos, push, friction, max_velocity)

        self.onscreen_pos = pos
        self.curr_onscreen_pos = pos
        self.accelerate = 5

    def draw(self, camera):
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
        

    
class Camera:
    def __init__(self, offset=[0,0], follow_speed=1):
        self.offset = offset
        self.follow_speed = follow_speed
        self.pos = [0,0]

    def update(self):
        pass

    def go_to(self, pos):
        dx = abs(self.pos[0] - pos[0])
        dy = abs(self.pos[1] - pos[1])
        min_x = dx/self.follow_speed
        min_y = dy/self.follow_speed

        dirx = 0
        if (pos[0] - self.pos[0]) > min_x or (self.pos[0] - pos[0]) > min_y:
            if pos[0] < self.pos[0]:
                dirx = -1
            else:
                dirx = 1
        diry = 0
        if (pos[1] - self.pos[1]) > min_x or (self.pos[1] - pos[1]) > min_y:
            if pos[1] < self.pos[1]:
                diry = -1
            else:
                diry = 1

        self.pos[0] += dirx * min_x
        self.pos[1] += diry * min_y
        

    def set_pos(self, pos):
        self.pos = pos

    def get_int_pos(self):
        return int(self.pos[0]+self.offset[0]), int(self.pos[1]+self.offset[1])

    def get_pos(self):
        return self.pos[0]+self.offset[0], self.pos[1]+self.offset[1]

        
class main_w_aron(Window):
    def __init__(self):
        super().__init__("Slice Slice")
        self.camera = Camera((-self.display.get_width()//2, 
                            -self.display.get_height()//2), 7)

        self.aron = Sprite(self.display, (0,0), 1, 0.5, 20)

        self.bg = Background(self.display)
    
    def update(self):
        self.bg.update()
        self.aron.update()
        self.camera.go_to((self.aron.x, self.aron.y))

    def draw(self):
        self.bg.draw(self.camera.get_pos())
        self.aron.draw(self.camera.get_pos())

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




