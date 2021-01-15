import pygame as pg
import sys
import os
import random
import time
import setting

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000
clock = pg.time.Clock()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


def welcome_window(win=True):
    sprite = pg.sprite.Sprite()
    fon = pg.sprite.Group()
    if win:
        sprite.image = load_image("win.png")
        sprite.rect = sprite.image.get_rect()
    else:
        sprite.image = load_image("lose.png")
        sprite.rect = sprite.image.get_rect()
    fon.add(sprite)
    fon.draw(screen)
    pg.display.flip()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == 768:
                if event.unicode == '':
                    return setting.settings_window()
        pg.display.flip()

