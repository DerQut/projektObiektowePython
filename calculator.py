import pygame
from pygame.locals import *

import window
import ui_elements

import assets


def button_handler(button_id):
    if button_id == 0:
        ...


window = window.Window(1280, 720, DOUBLEBUF, (128, 128, 128))

input_surface = ui_elements.Surface(window, 0, 0, 420, 720, (0, 0, 0))
graph_surface = ui_elements.Surface(window, 422, 0, 858, 720, (12, 12, 12))
