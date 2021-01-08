import pygame as pg
import sys
import os
import random

weapon = 0

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 60
clock = pg.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


class Scope(pg.sprite.Sprite):
    def __init__(self, group, size=50):
        super().__init__(group)
        self.size = size
        self.image = load_image('scope.png')
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0

    def moving_cursor(self, new_pos):
        self.rect.x, self.rect.y = new_pos[0] - 25, new_pos[1] - 18


class Enemy(pg.sprite.Sprite):
    def __init__(self, group, x=300, y=400, size=200):
        super().__init__(group)
        self.size = size
        self.time_delay = 0
        self.live = True
        self.original_y = y
        self.image = load_image('enemy_1.png')
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.max_y = size - 20

    def update(self, *args):
        global weapon
        if args and args[0].type == pg.MOUSEBUTTONDOWN:
            if weapon == 2:
                self.rect.y = self.original_y
                self.live = False
                self.time_delay = random.randint(50, 250)
                print(self.time_delay)
            elif self.rect.collidepoint(args[0].pos) and self.live:
                if weapon == 1:
                    self.rect.y = self.original_y
                    self.live = False
                    self.time_delay = random.randint(50, 250)
                    print(self.time_delay)
                elif weapon == 0:
                    self.rect.y = self.original_y
                    self.live = False
                    self.time_delay = random.randint(50, 250)
                    print(self.time_delay)
        elif self.time_delay > 0:
            self.time_delay -= 1
        elif not self.live:
            self.live = True
        elif self.rect.y + self.max_y > self.original_y:
            self.rect.y -= 1
        else:
            pass


def return_laptop_sprite_group():
    all_sprites = pg.sprite.Group()
    for i in range(3):
        sprite = pg.sprite.Sprite()
        sprite.image = load_image("laptop.png")
        sprite.image = pg.transform.scale(sprite.image, (200, 200))
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        sprite.rect.x = 50 + 250 * i
        sprite.rect.y = 300
    return all_sprites


def widow():
    all_sprites = pg.sprite.Group()
    cursor_sprite = pg.sprite.Group()
    laptops = return_laptop_sprite_group()
    cursor = Scope(cursor_sprite)
    bot_interaction_flag = False
    Enemy(all_sprites, 50, 300)
    Enemy(all_sprites, 300, 300)
    Enemy(all_sprites, 550, 300)

    while True:
        if bot_interaction_flag:
            all_sprites.update(n)
        screen.fill('white')
        for event in pg.event.get():
            if not bot_interaction_flag:
                n = event
                bot_interaction_flag = True

            elif event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == 768:
                if event.unicode == '':
                    return
            elif event.type == pg.MOUSEMOTION:
                if event.pos[1] >= 600:
                    cursor.image = load_image('cursor.png')
                    cursor.image = pg.transform.scale(cursor.image, (cursor.size, cursor.size))
                else:
                    cursor.image = load_image('scope.png')
                    cursor.image = pg.transform.scale(cursor.image, (cursor.size, cursor.size))

                cursor.moving_cursor(event.pos)

            elif event.type == pg.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        all_sprites.draw(screen)
        laptops.draw(screen)
        pg.draw.rect(screen, 'red', (0, 600, 800, 800))
        if pg.mouse.get_focused():
            pg.mouse.set_visible(False)
            cursor_sprite.draw(screen)
        else:
            pg.mouse.set_visible(True)
        pg.display.flip()
        clock.tick(FPS)


widow()
