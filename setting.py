import pygame as pg
import sys
import os
from game import *

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


class Button(pg.sprite.Sprite):
    def __init__(self, group, x, y, range_x, result=0):
        super().__init__(group)
        self.image = pg.transform.scale(load_image('button_1.png'), (range_x, range_x // 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x, self.y = x, y
        self.range = range_x
        self.flag = False
        self.result = result

    def change_png(self):
        if self.flag:
            self.image = pg.transform.scale(load_image('button_1.png'), (self.range, self.range // 3))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
        else:
            self.image = pg.transform.scale(load_image('button_2.png'), (self.range, self.range // 3))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
        self.flag = not self.flag

    def update(self, arr, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            for i in arr:
                if i.flag:
                    i.change_png()
            self.change_png()
            return self.result
        return '0'


def return_result(buttons):
    for i in buttons.arr_buttons:
        if i.flag:
            return i.result
    return buttons.arr_buttons[1].result


class Buttons():
    def __init__(self):
        self.arr_buttons = []
        self.arr_txt = []
        self.sprites = pg.sprite.Group()
        self.result = 0

    def add_button(self, x, y, range_x=200, result=1):
        self.arr_buttons.append(Button(self.sprites, x, y, range_x, result))

    def add_txt(self, x, y, txt, font=50):
        self.arr_txt.append([txt, x, y, font])

    def draw_buttons(self):
        self.sprites.draw(screen)
        for i in self.arr_txt:
            font = pg.font.Font(None, i[3])
            text = font.render(i[0], True, ('white'))
            text_x, text_y = i[1], i[2]
            screen.blit(text, (text_x, text_y))


def return_exit_button():
    sprite = pg.sprite.Sprite()
    s = pg.sprite.Group()
    sprite.image = pg.transform.scale(load_image('button_1.png'), (250, 250 // 3))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 280
    sprite.rect.y = 700
    s.add(sprite)
    return s



def draw_txt():
    font = pg.font.Font(None, 50)
    text = font.render('Настройте же сложность своей игры', True, ('white'))
    screen.blit(text, (80, 20))
    text = font.render('Ваша реакция', True, ('white'))
    screen.blit(text, (250, 90))
    text = font.render('Длительность урока', True, ('white'))
    screen.blit(text, (230, 250))
    text = font.render('Допустимое количество ошибок', True, ('white'))
    screen.blit(text, (150, 400))
    text = font.render('            Общая сложность', True, ('white'))
    screen.blit(text, (150, 550))
    text = font.render('Погнали?', True, ('white'))
    screen.blit(text, (325, 725))


def settings_window():

    result = []
    exit_button = return_exit_button()
    recharge_rate = Buttons()  # перезарядка
    time_to_win = Buttons()  # время до победы
    quantity_of_life = Buttons()  # хп
    speed_bot = Buttons()
    # кнопки
    recharge_rate.add_button(10, 150, 250, [0, 0])
    recharge_rate.add_button(280, 150, 250, [2, 15])
    recharge_rate.add_button(550, 150, 250, [3, 25])
    # кнопки
    time_to_win.add_button(10, 300, 250, 60)
    time_to_win.add_button(280, 300, 250, 300)
    time_to_win.add_button(550, 300, 250, 600)
    # кнопки
    quantity_of_life.add_button(10, 450, 250, 1)
    quantity_of_life.add_button(280, 450, 250, 3)
    quantity_of_life.add_button(550, 450, 250, 5)
    # кнопки
    speed_bot.add_button(10, 600, 250, 1)
    speed_bot.add_button(280, 600, 250, 5)
    speed_bot.add_button(550, 600, 250, 10)
    #
    recharge_rate.arr_buttons[1].change_png()
    time_to_win.arr_buttons[0].change_png()
    quantity_of_life.arr_buttons[0].change_png()
    speed_bot.arr_buttons[0].change_png()
    # текст
    recharge_rate.add_txt(30, 175, 'мгновенная', font=50)
    recharge_rate.add_txt(330, 175, 'быстрая', font=50)
    recharge_rate.add_txt(575, 175, 'нормальная', font=50)
    time_to_win.add_txt(60, 325, '1 минута', font=50)
    time_to_win.add_txt(340, 325, '5 минут', font=50)
    time_to_win.add_txt(605, 325, '10 минут', font=50)
    quantity_of_life.add_txt(110, 475, '  0', font=50)
    quantity_of_life.add_txt(380, 475, '  2', font=50)
    quantity_of_life.add_txt(650, 475, '  4', font=50)
    speed_bot.add_txt(60, 625, '       1', font=50)
    speed_bot.add_txt(330, 625, '       5', font=50)
    speed_bot.add_txt(610, 625, '     10', font=50)
    # текст
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == 768:
                if event.unicode == '':
                    return
            elif event.type == pg.MOUSEBUTTONDOWN and event.pos[0] >= 300 and event.pos[1] >= 700 and event.pos[
                0] <= 550:
                result.append(return_result(recharge_rate))
                result.append(return_result(time_to_win))
                result.append(return_result(quantity_of_life))
                result.append(return_result(speed_bot))
                return widow(result[1], result[2], result[0][0], result[0][1], result[3])
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    recharge_rate.sprites.update(recharge_rate.sprites, event)
                    time_to_win.sprites.update(time_to_win.sprites, event)
                    quantity_of_life.sprites.update(quantity_of_life.sprites, event)
                    speed_bot.sprites.update(speed_bot.sprites, event)
        fon = pg.transform.scale(load_image('fon_12.png'), (800, 800))
        screen.blit(fon, (0, 0))
        recharge_rate.draw_buttons()
        time_to_win.draw_buttons()
        quantity_of_life.draw_buttons()
        speed_bot.draw_buttons()
        exit_button.draw(screen)
        draw_txt()
        pg.display.flip()
        clock.tick(FPS)

