import pygame
from pygame.locals import *

import window
import ui_elements

import assets


def button_handler(button_id):
    print(button_id)
    if button_id == 0:
        ...

button_colour = (53, 47, 46)

window = window.Window(1280, 720, DOUBLEBUF, (128, 128, 128))

left_surface = ui_elements.Surface(window, 0, 0, 409, 720, (33, 26, 26))

input_surface = ui_elements.Surface(window, 0, 128, 409, 412, (33, 26, 26))

button_1 = ui_elements.Button(input_surface, 3, 3, 133, 133, button_colour, 1)

graph_surface = ui_elements.Surface(window, 409, 0, 871, 720, (12, 12, 12))
