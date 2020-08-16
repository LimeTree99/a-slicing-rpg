from random import randint

class Base:
    def __init__(self, display):
        self.display = display

    def update(self):
        pass

    def draw(self, camera):
        pass

def chance(percent):
        '''percent chance of returning True'''
        if randint(0, 100) <= percent:
            return True
        else:
            return False