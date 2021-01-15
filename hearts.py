import pygame as pg
from load_image import load_image
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000

class Hearts():
    def __init__(self, hp):
        self.max_hp = hp
        self.now_hp = hp
        self.arr_hp = []
        self.sprites = pg.sprite.Group()
        for i in range(hp):
            self.arr_hp.append(pg.sprite.Sprite())
            self.arr_hp[i].image = load_image("heart.png")
            self.arr_hp[i].image = pg.transform.scale(self.arr_hp[i].image, (50, 50))
            self.arr_hp[i].rect = self.arr_hp[i].image.get_rect()
            self.sprites.add(self.arr_hp[i])
            self.arr_hp[i].rect.x = 740 - 50 * i
            self.arr_hp[i].rect.y = 610

    def remove_hp(self):
        self.now_hp -= 1
        self.arr_hp[self.now_hp].image = load_image("heart_2.png")
        self.arr_hp[self.now_hp].image = pg.transform.scale(self.arr_hp[self.now_hp].image, (50, 50))

    def add_hp(self):
        global count_hp
        while count_hp < self.max_hp:
            self.arr_hp[self.now_hp].image = load_image("heart.png")
            self.arr_hp[self.now_hp].image = pg.transform.scale(self.arr_hp[self.now_hp].image, (50, 50))
            self.now_hp += 1
            count_hp += 1

    def draw_hearts(self):
        global screen
        self.sprites.draw(screen)
        pg.draw.rect(screen, (0, 0, 0), (800 - 15 - 50 * self.max_hp, 600, 50 * self.max_hp + 15, 70), 1)
