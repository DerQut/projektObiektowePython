import pygame
from pygame.locals import *

import window
import ui_elements

import assets


def button_handler(button_id):
    print(button_id)


bg_colour = (43, 34, 34)

button_colour_glowing = (150, 147, 147)
button_colour_light = (102, 97, 97)
button_colour_dark = (68, 61, 61)

text_colour = (255, 255, 255)

calculator_window = window.Window(574, 250, DOUBLEBUF, bg_colour)

input_surface = window.Surface(calculator_window, 0, 58, 574, 240, bg_colour)


button_1 = ui_elements.LabelledButton(input_surface, 0, 96, 56, 47, button_colour_light, 1, button_colour_glowing, "1", text_colour, assets.SF_Pro)
button_2 = ui_elements.LabelledButton(input_surface, 57, 96, 56, 47, button_colour_light, 2, button_colour_glowing, "2", text_colour, assets.SF_Pro)
button_3 = ui_elements.LabelledButton(input_surface, 114, 96, 56, 47, button_colour_light, 3, button_colour_glowing, "3", text_colour, assets.SF_Pro)
button_4 = ui_elements.LabelledButton(input_surface, 0, 48, 56, 47, button_colour_light, 4, button_colour_glowing, "4", text_colour, assets.SF_Pro)
button_5 = ui_elements.LabelledButton(input_surface, 57, 48, 56, 47, button_colour_light, 5, button_colour_glowing, "5", text_colour, assets.SF_Pro)
button_6 = ui_elements.LabelledButton(input_surface, 114, 48, 56, 47, button_colour_light, 6, button_colour_glowing, "6", text_colour, assets.SF_Pro)
button_7 = ui_elements.LabelledButton(input_surface, 0, 0, 56, 47, button_colour_light, 7, button_colour_glowing, "7", text_colour, assets.SF_Pro)
button_8 = ui_elements.LabelledButton(input_surface, 57, 0, 56, 47, button_colour_light, 8, button_colour_glowing, "8", text_colour, assets.SF_Pro)
button_9 = ui_elements.LabelledButton(input_surface, 114, 0, 56, 47, button_colour_light, 9, button_colour_glowing, "9", text_colour, assets.SF_Pro)
button_0 = ui_elements.LabelledButton(input_surface, 0, 144, 113, 47, button_colour_light, 0, button_colour_glowing, "0", text_colour, assets.SF_Pro)




