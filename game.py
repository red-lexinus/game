import pygame as pg
import sys
import time
import win
from draw_time_of_restarting_weapons import *
from draw_time_to_win import *
from Enemy import *
from Fon import *
from hearts import *
from load_image import *
from PauseButton import *
from return_laptop_sprite_group import *
from return_lower_fon import *
from Scope import *
from Secret import *

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000
clock = pg.time.Clock()
weapon = 1
launch_time = time.time()
the_current_time = time.time()
time_of_1_weapon = -99
time_of_2_weapon = -99


def new_time():
    return time.time()


def gameplay(time_to_win=60, hp=5, weapon_1_time=2, weapon_2_time=10, level_of_difficulty=2):
    global weapon, launch_time, the_current_time, time_of_1_weapon, time_of_2_weapon, \
        count_hp, weapon_1_t, weapon_2_t, hearts, scope_weapon, screen
    pause_flag = False
    hearts = Hearts(hp)
    weapon_1_t = weapon_1_time
    weapon_2_t = weapon_2_time
    count_hp = hp
    secret = Secret()
    launch_time = new_time()
    all_sprites = pg.sprite.Group()
    cursor_sprite = pg.sprite.Group()
    laptops = return_laptop_sprite_group()
    cursor = Scope(cursor_sprite)
    lower_fon = return_lower_fon()
    #
    scope_weapon = pg.sprite.Sprite()
    scope_weapon.image = load_image("scope_weapon.png")
    scope_weapon.image = pg.transform.scale(scope_weapon.image, (50, 50))
    scope_weapon.rect = scope_weapon.image.get_rect()
    lower_fon.add(scope_weapon)
    scope_weapon.rect.x = 96
    scope_weapon.rect.y = 620
    #
    bot_interaction_flag = False
    background_fon = Fon()
    rivals = []
    esc = PauseButton(740, 740)
    opponent_1, opponent_2, opponent_3 = Enemy(all_sprites, level_of_difficulty, 50, 300), \
                                         Enemy(all_sprites, level_of_difficulty, 300, 300), \
                                         Enemy(all_sprites, level_of_difficulty, 550, 300)
    rivals.append(opponent_1)
    rivals.append(opponent_2)
    rivals.append(opponent_3)
    times = clock.tick() / FPS
    the_current_time = new_time() - launch_time

    while True:
        for event in pg.event.get():
            try:
                if not bot_interaction_flag:
                    n = event
                    bot_interaction_flag = True

                elif event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == 768:
                    if event.unicode == '':
                        if not pause_flag:
                            pause_flag = True
                            pause_time = the_current_time

                        else:
                            pause_flag = False
                            launch_time += the_current_time - pause_time

                elif event.type == pg.KEYUP and int(event.unicode) != weapon and not pause_flag:
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
                        cursor.change_image('cursor.png')
                    else:
                        cursor.change_image('scope.png')
                    cursor.moving_cursor(event.pos)
                elif event.type == pg.MOUSEBUTTONDOWN and not pause_flag:
                    if event.pos[1] < 600:
                        if weapon == 1:
                            if (int(weapon_1_t - the_current_time + time_of_1_weapon)) <= 0 and event.pos[1] < 300:
                                time_of_1_weapon = new_time() - launch_time
                                all_sprites.update(event, weapon=1)
                        else:
                            if (int(weapon_2_t - the_current_time + time_of_2_weapon)) <= 0:
                                time_of_2_weapon = new_time() - launch_time
                                all_sprites.update(event, weapon=2)
                    if event.pos[0] >= 745 and event.pos[1] >= 610 and (event.pos[0] <= 777 and event.pos[1] <= 652):
                        hearts.add_hp()
                    else:
                        if event.pos[0] <= 170 and event.pos[1] < 700:
                            scope_weapon.rect.x = 96
                            scope_weapon.rect.y = 620
                            weapon = 1
                        elif event.pos[0] <= 170 and event.pos[1] >= 700:
                            scope_weapon.rect.x = 100
                            scope_weapon.rect.y = 730
                            weapon = 2

            except:
                pass
        secret.draw()
        times = clock.tick() / FPS
        if not pause_flag and times > 0:
            for i in rivals:
                i.add_time(times)
        background_fon.draw_1_fon()
        all_sprites.draw(screen)
        background_fon.draw_2_fon()
        laptops.draw(screen)
        lower_fon.draw(screen)
        the_current_time = new_time() - launch_time
        if not pause_flag:
            draw_time_to_win(int(time_to_win - the_current_time))
            draw_time_of_restarting_weapons(int(weapon_1_t - the_current_time + time_of_1_weapon),
                                            int(weapon_2_t - the_current_time + time_of_2_weapon))
        else:
            draw_time_to_win(int(time_to_win - pause_time))
            draw_time_of_restarting_weapons(int(weapon_1_t - pause_time + time_of_1_weapon),
                                            int(weapon_2_t - pause_time + time_of_2_weapon))

        hearts.draw_hearts()
        esc.draw()
        if pause_flag:
            esc.draw_pause()
        if pg.mouse.get_focused():
            pg.mouse.set_visible(False)
            cursor_sprite.draw(screen)
        else:
            pg.mouse.set_visible(True)
        pg.display.flip()
        clock.tick(FPS)
        if time_to_win - the_current_time < 0 and not pause_flag:
            # возвращаем победу
            pg.mouse.set_visible(True)
            return win.welcome_window(True)
        elif count_hp <= 0:
            # возвращаем порожение
            pg.mouse.set_visible(True)
            return win.welcome_window(False)

