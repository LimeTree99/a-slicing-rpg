import math

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
