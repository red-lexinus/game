import pygame as pg

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000


def draw_time_of_restarting_weapons(time_1, time_2):
    global screen
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
