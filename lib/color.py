from random import randint


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


white = (255, 255, 255)
gray3 = (150, 150, 150)
gray2 = (100, 100, 100)
gray1 = (50, 50, 50)
black = (0, 0, 0)

def randgray(a, b):
    c = randint(a, b)
    return (c, c, c)