import pygame as pg
import sys
import os

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 50
clock = pg.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    return image


def first_widow():
    flag = False
    y_pos = 0
    x = 1
    v = 100  # пикселей в секунду
    fon = load_image('fon.png')
    screen.blit(fon, (0, 0))
    # font = pg.font.Font(None, 30)
    # text = font.render("Погнали!!!!!!", True, 'red')
    # screen.blit(text, (10, 10))
    # text = font.render("Просто вжаривайте!!!!!!", True, 'red')
    # screen.blit(text, (10, 30))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif flag and event.type == 768:
                return
            elif flag and event.type == pg.MOUSEBUTTONDOWN:
                try:
                    if event.button == 4:
                        x += 2
                        if x < 0:
                            x = 0
                    elif event.button == 5:
                        x -= 2
                        if x > 0:
                            x = 0
                    elif event.button == 1 or  event.button  == 3:
                        x = 0
                except:
                    pass
            elif event.type == pg.KEYDOWN or \
                    event.type == pg.MOUSEBUTTONDOWN:
                if not flag:
                    flag = True
                    fon = load_image('fon_1.png')
        if flag:
            y_pos -= x
            if y_pos > 0:
                y_pos = 0
            elif y_pos < -1300:
                y_pos = -1300

        screen.fill('white')
        screen.blit(fon, (0, y_pos))

        pg.display.flip()
        clock.tick(FPS)
