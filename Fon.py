import pygame as pg
from load_image import load_image
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000

class Fon():
    def __init__(self):
        self.sprite_1 = pg.sprite.Group()
        self.sprite_2 = pg.sprite.Group()
        self.fon_1 = pg.sprite.Sprite()
        self.fon_2 = pg.sprite.Sprite()
        self.fon_1.image = load_image("game_fon.png")
        self.fon_1.image = pg.transform.scale(self.fon_1.image, (800, 422))
        self.fon_1.rect = self.fon_1.image.get_rect()
        self.fon_1.rect.x, self.fon_1.rect.y = 0, 0
        self.sprite_1.add(self.fon_1)
        self.fon_2.image = load_image("game_fon.png")
        self.fon_2.image = pg.transform.scale(self.fon_2.image, (800, 422))
        self.fon_2.rect = self.fon_2.image.get_rect()
        self.fon_2.rect.x, self.fon_2.rect.y = 0, 422
        self.sprite_2.add(self.fon_2)

    def draw_1_fon(self):
        global screen
        self.sprite_1.draw(screen)

    def draw_2_fon(self):
        global screen
        self.sprite_2.draw(screen)