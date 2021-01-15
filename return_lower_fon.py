import pygame as pg
from load_image import load_image



def return_lower_fon():
    global scope_weapon
    all_sprites = pg.sprite.Group()
    sprite = pg.sprite.Sprite()
    sprite.image = load_image("game_lower_fon.png")
    sprite.image = pg.transform.scale(sprite.image, (800, 200))
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    sprite.rect.x = 0
    sprite.rect.y = 600
    #
    sprite_2 = pg.sprite.Sprite()
    sprite_2.image = load_image("question.png")
    sprite_2.image = pg.transform.scale(sprite_2.image, (100, 100))
    sprite_2.rect = sprite_2.image.get_rect()
    all_sprites.add(sprite_2)
    sprite_2.rect.x = 0
    sprite_2.rect.y = 600
    #
    sprite_3 = pg.sprite.Sprite()
    sprite_3.image = load_image("kahoot.png")
    sprite_3.image = pg.transform.scale(sprite_3.image, (100, 100))
    sprite_3.rect = sprite_3.image.get_rect()
    all_sprites.add(sprite_3)
    sprite_3.rect.x = 0
    sprite_3.rect.y = 700
    return all_sprites
