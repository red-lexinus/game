import pygame as pg
import sys
import os
from first_window import *
from game import *

pg.init()
size = width, height = 800, 800

WIDTH, HEIGHT = width, height
screen = pg.display.set_mode(size)
FPS = 60
clock = pg.time.Clock()
pg.display.set_caption("Перемещение героя")  # заголовок
setting_widow()
widow()
