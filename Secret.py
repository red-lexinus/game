import pygame as pg
from load_image import load_image
import random
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000


class Secret():
    def __init__(self):
        self.sprite = pg.sprite.Sprite()
        self.sprite.image = load_image("game_lower_fon.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprites = pg.sprite.Group()
        self.sprites.add(self.sprite)

    def draw(self):
        global screen
        self.sprite.rect.x, self.sprite.rect.y = random.randint(0, 700), random.randint(0, 700)
        self.sprites.draw(screen)
