import pygame as pg
from load_image import load_image

def return_laptop_sprite_group():
    all_sprites = pg.sprite.Group()
    for i in range(3):
        sprite = pg.sprite.Sprite()
        sprite.image = load_image("laptop_1.png")
        sprite.image = pg.transform.scale(sprite.image, (200, 256))
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        sprite.rect.x = 50 + 250 * i
        sprite.rect.y = 300
    return all_sprites