import pygame as p
import random

p.init()


class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

    def illuminate(self):
        illuminated_image = p.image.load('illuminated.png').convert_alpha()
        illuminated_image = p.transform.scale(
        illuminated_image, (self.width, self.height))
        self.image.fill((255, 255, 255, 0))
        self.image.blit(illuminated_image, (0, 0))

    def reset(self):
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))


def Update():
    win.blit(background, (0, 0))
    square_group.draw(win)
    square_group.update()
    p.display.update()


WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Tic Tac Toe')
clock = p.time.Clock()

blank_image = p.image.load('Blank.png').convert_alpha()
x_image = p.image.load('x.png')
o_image = p.image.load('o.png')
background = p.image.load('Background.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

square_group = p.sprite.Group()
squares = []

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Square(x, y, num)
        square_group.add(sq)
        squares.append(sq)
        num += 1

# Nueva frecuencia de iluminación (125 Hz)
illumination_frequency = 25

run = False
while run:
    clock.tick(illumination_frequency)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    # Selecciona aleatoriamente un cuadrado que no haya sido iluminado recientemente
    non_illuminated_squares = [
        sq for sq in squares if not hasattr(sq, 'illuminated')]
    if non_illuminated_squares and random.random() < (illumination_frequency / 10):
        random_square = random.choice(non_illuminated_squares)
        random_square.illuminated = True
        random_square.illuminate()
        Update()
        # Redondear a un entero antes de pasar a la función delay
        delay_time = round(1000 / illumination_frequency)
        p.time.delay(delay_time)
        random_square.reset()
        delattr(random_square, 'illuminated')

    Update()
