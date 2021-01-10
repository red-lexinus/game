import pygame as pg
import sys
import os
import random
import time

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 60
clock = pg.time.Clock()
weapon = 1
launch_time = time.time()
the_current_time = time.time()
time_of_1_weapon = -99
time_of_2_weapon = -99


def new_time():
    return time.time()


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
    def __init__(self, group, level_of_difficulty=1, x=300, y=400, size=200):
        super().__init__(group)
        self.level_of_difficulty = level_of_difficulty
        self.size = size
        self.time_delay = random.randint(0, 50 + (50 // level_of_difficulty))
        self.live = True
        self.original_y = y
        self.image = load_image('enemy_1.png')
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.max_y = size - 20
        self.damage_flag = True

    def update(self, *args):
        global weapon, the_current_time, launch_time, time_of_2_weapon, time_of_1_weapon, \
            count_hp, weapon_1_t, weapon_2_t, hearts
        if args and args[0].type == pg.MOUSEBUTTONDOWN:
            if weapon == 2 and int(weapon_2_t - the_current_time + time_of_2_weapon) <= 0:
                self.rect.y = self.original_y
                self.live, self.damage_flag = False, True
                self.time_delay = random.randint(100, 400 + 100 // self.level_of_difficulty)
            elif self.rect.collidepoint(args[0].pos) and self.live:
                if weapon == 1 and int(weapon_1_t - the_current_time + time_of_1_weapon) <= 0:
                    self.rect.y = self.original_y
                    self.live, self.damage_flag = False, True
                    self.time_delay = random.randint(50, 200 + 50 // self.level_of_difficulty)
        elif self.time_delay > 0:
            self.time_delay -= 1
        elif not self.live:
            self.live = True
        elif self.rect.y + self.max_y > self.original_y:
            number = random.randint(1, 10)
            if number <= self.level_of_difficulty:
                self.rect.y -= self.level_of_difficulty
            self.rect.y -= 1
        else:
            pass
        if self.rect.y <= 120 and self.damage_flag:
            self.damage_flag = False
            count_hp -= 1
            self.rect.y = self.original_y
            self.live, self.damage_flag = False, True
            self.time_delay = random.randint(50, 200 + 50 // self.level_of_difficulty)
            hearts.remove_hp()


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
        if self.now_hp < self.max_hp:
            self.now_hp += 1
            self.arr_hp[self.now_hp].image = load_image("heart.png")
            self.arr_hp[self.now_hp].image = pg.transform.scale(self.arr_hp[self.now_hp].image, (50, 50))

    def draw_hearts(self):
        self.sprites.draw(screen)
        pg.draw.rect(screen, (0, 0, 0), (800 - 15 - 50 * self.max_hp, 600, 50 * self.max_hp + 15, 70), 1)


def draw_time_to_win(time):
    font = pg.font.Font(None, 30)
    text = font.render("время до победы", True, (0, 0, 0))
    text_x = 615
    text_y = 670
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    text = font.render(str(time), True, (0, 0, 0))
    text_x = 695
    text_y = 700
    text_h += text.get_height()
    screen.blit(text, (text_x, text_y))
    pg.draw.rect(screen, (0, 0, 0), (602, 669, text_w + 20, text_h + 20), 1)


def draw_time_of_restarting_weapons(time_1, time_2):
    font = pg.font.Font(None, 50)
    if time_1 > 0:
        font = pg.font.Font(None, 50)
        text = font.render(str(time_1), True, (0, 0, 0))
        text_x = 170
        text_y = 630
        text_w = text.get_width()
        text_h = text.get_height()
        pg.draw.rect(screen, (0, 0, 0), (160, 620, text_w + 20, text_h + 20), 1)
        screen.blit(text, (text_x, text_y))
    else:
        pass
    if time_2 > 0:
        text = font.render(str(time_2), True, (0, 0, 0))
        text_x = 170
        text_y = 740
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pg.draw.rect(screen, (0, 0, 0), (160, 730, text_w + 20, text_h + 20), 1)
    else:
        pass


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
    #
    scope_weapon = pg.sprite.Sprite()
    scope_weapon.image = load_image("scope_weapon.png")
    scope_weapon.image = pg.transform.scale(scope_weapon.image, (50, 50))
    scope_weapon.rect = scope_weapon.image.get_rect()
    all_sprites.add(scope_weapon)
    scope_weapon.rect.x = 96
    scope_weapon.rect.y = 620
    # 96, 620. 100, 730
    return all_sprites


def widow(time_to_win=60, hp=3, weapon_1_time=2, weapon_2_time=10, level_of_difficulty=2):
    global weapon, launch_time, the_current_time, time_of_1_weapon, time_of_2_weapon, \
        count_hp, weapon_1_t, weapon_2_t, hearts
    hearts = Hearts(hp)
    weapon_1_t = weapon_1_time
    weapon_2_t = weapon_2_time
    count_hp = hp
    launch_time = new_time()
    all_sprites = pg.sprite.Group()
    cursor_sprite = pg.sprite.Group()
    laptops = return_laptop_sprite_group()
    cursor = Scope(cursor_sprite)
    lower_fon = return_lower_fon()
    bot_interaction_flag = False
    Enemy(all_sprites, level_of_difficulty, 50, 300)
    Enemy(all_sprites, level_of_difficulty, 300, 300)
    Enemy(all_sprites, level_of_difficulty, 550, 300)

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
        try:
            if not bot_interaction_flag:
                n = event
                bot_interaction_flag = True

            elif event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == 768:
                if event.unicode == '':
                    return
            elif event.type == pg.KEYUP:
                if event.unicode == '1':
                    scope_weapon.rect.x = 96
                    scope_weapon.rect.y = 620
                    weapon = 1
                elif event.unicode == '2':
                    scope_weapon.rect.x = 100
                    scope_weapon.rect.y = 730
                    weapon = 2

            elif event.type == pg.MOUSEMOTION:
                if event.pos[1] >= 600:
                    cursor.image = load_image('cursor.png')
                    cursor.image = pg.transform.scale(cursor.image, (cursor.size, cursor.size))
                else:
                    cursor.image = load_image('scope.png')
                    cursor.image = pg.transform.scale(cursor.image, (cursor.size, cursor.size))

                cursor.moving_cursor(event.pos)

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.pos[1] >= 600:
                    if event.pos[0] <= 170 and event.pos[1] < 700:
                        scope_weapon.rect.x = 96
                        scope_weapon.rect.y = 620
                        weapon = 1
                    elif event.pos[0] <= 170 and event.pos[1] >= 700:
                        scope_weapon.rect.x = 100
                        scope_weapon.rect.y = 730
                        weapon = 2
                else:

                    if weapon == 1:
                        if (int(weapon_1_t - the_current_time + time_of_1_weapon)) <= 0:
                            time_of_1_weapon = new_time() - launch_time
                    else:
                        if (int(weapon_2_t - the_current_time + time_of_2_weapon)) <= 0:
                            time_of_2_weapon = new_time() - launch_time

        except:
            pass
        all_sprites.draw(screen)
        laptops.draw(screen)
        lower_fon.draw(screen)
        the_current_time = new_time() - launch_time
        draw_time_to_win(int(time_to_win - the_current_time))
        draw_time_of_restarting_weapons(int(weapon_1_t - the_current_time + time_of_1_weapon),
                                        int(weapon_2_t - the_current_time + time_of_2_weapon))
        hearts.draw_hearts()
        if pg.mouse.get_focused():
            pg.mouse.set_visible(False)
            cursor_sprite.draw(screen)
        else:
            pg.mouse.set_visible(True)
        pg.display.flip()
        clock.tick(FPS)
        if (time_to_win - the_current_time) < 0:
            # возвращаем победу
            return True
        elif count_hp <= 0:
            # возвращаем порожение
            return False
