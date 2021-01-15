import pygame as pg
from load_image import load_image
import random
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000

class Enemy(pg.sprite.Sprite):
    def __init__(self, group, level_of_difficulty=1, x=300, y=400, size=200):
        super().__init__(group)
        self.level_of_difficulty = level_of_difficulty
        self.size = size
        self.time_delay = random.randint(0, 2) + random.random()
        self.live = False
        self.original_y = y
        self.image = load_image('enemy_1.png')
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.max_y = size - 20
        self.damage_flag = True

    def update(self, *args, weapon=1):
        if args and args[0].type == pg.MOUSEBUTTONDOWN:
            if weapon == 2:
                self.rect.y = self.original_y
                self.live, self.damage_flag = False, True
                self.time_delay = random.randint(1, 7)
            elif self.rect.collidepoint(args[0].pos):
                self.rect.y = self.original_y
                self.live, self.damage_flag = False, True
                self.time_delay = random.randint(0, 3)

    def add_time(self, time):
        global count_hp, hearts
        if self.live and self.time_delay < 0:
            if self.rect.y + self.max_y > self.original_y and self.rect.y > 120:
                self.rect.y -= (time + self.level_of_difficulty - 1)
            elif self.rect.y <= 120:
                self.damage_flag = False
                count_hp -= 1
                self.rect.y = self.original_y
                self.live, self.damage_flag = False, True
                self.time_delay = random.randint(1, 3)
                hearts.remove_hp()
        else:
            if self.time_delay >= 0:
                self.time_delay -= (0.01 + self.level_of_difficulty / 100)
            else:
                self.live = True
