import pygame as pg
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000


def draw_time_to_win(time):
    global screen
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
