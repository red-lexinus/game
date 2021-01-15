import pygame as pg
from load_image import load_image
pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 1000

class PauseButton():
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.esc = pg.sprite.Sprite()
        self.esc.image = load_image("esc.png")
        self.esc.image = pg.transform.scale(self.esc.image, (50, 50))
        self.esc.rect = self.esc.image.get_rect()
        self.sprite = pg.sprite.Group()
        self.sprite.add(self.esc)
        self.sprite_2 = pg.sprite.Group()
        self.esc.rect.x, self.esc.rect.y = x, y
        self.pause = pg.sprite.Sprite()
        self.pause.image = load_image("pause.png")
        self.pause.image = pg.transform.scale(self.pause.image, (200, 200))
        self.pause.rect = self.pause.image.get_rect()
        self.pause.rect.x, self.pause.rect.y = 280, 600
        self.sprite_2.add(self.pause)

    def draw(self):
        global screen
        self.sprite.draw(screen)
        font = pg.font.Font(None, 30)
        text = font.render("для паузы нажмите", True, (0, 0, 0))
        screen.blit(text, (self.x - 220, self.y + 10))
        pg.draw.rect(screen, (0, 0, 0), (self.x - 230, self.y - 10, 300, 70), 1)

    def draw_pause(self):
        self.sprite_2.draw(screen)
