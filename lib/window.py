import pygame
import os

class Window:
    def __init__(self,
                 window_name,
                 corner_image = os.path.split(__file__)[0][:-4] + '/images/flower_corner_image.png',
                 fps = 60):
        self.fps = fps
        self.end = False
        self.background_on = True
        self.background_colour = (0,0,0)
        self.events = 0
        
        pygame.init()
        self.display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        
        pygame.mouse.set_visible(False)
        pygame.display.set_caption(window_name)
        icon = pygame.image.load(corner_image)
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()

    def update(self):
        pass
    
    def event_handle(self, event):
        pass

    def keyup(self, key):
        pass

    def keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.end = True 

    def run(self):
        while not self.end:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    pygame.quit()  
                    self.end = True
                if event.type == pygame.KEYDOWN:
                    self.keydown(event.key)
                if event.type == pygame.KEYUP:
                    self.keyup(event.key)
                self.event_handle(event)

            
            self.display.fill(self.background_colour)
            self.update()
            pygame.display.update()
            
            self.clock.tick(self.fps)




if __name__ == '__main__':
    
    game = Window(800, 500, 'Working Title')
    game.run()
