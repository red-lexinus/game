import pygame as pg
from load_image import load_image
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000


class Scope(pg.sprite.Sprite):
    def __init__(self, group, size=50):
        super().__init__(group)
        self.size = size
        self.image = load_image('scope.png')
        self.name_image = 'scope.png'
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def change_image(self, image):
        if self.name_image != image:
            self.image = load_image(image)
            self.name_image = image
            self.image = pg.transform.scale(self.image, (self.size, self.size))

    def moving_cursor(self, new_pos):
        self.rect.x, self.rect.y = new_pos[0] - 25, new_pos[1] - 18