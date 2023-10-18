# TODO utilise the key_handler function to reduce clutter in window.py

import pygame
from pygame.locals import *

import window
import ui_elements

import assets


def button_handler(event):
    print(event)


def key_handler(window, event):
    print(event)


def key_merger(event_key):
    if event_key == pygame.K_PERIOD:
        return pygame.K_COMMA
    elif event_key == pygame.K_RETURN:
        return pygame.K_EQUALS
    return event_key


bg_colour = (43, 34, 34)

button_colour_glowing = (150, 147, 147)
button_colour_light = (102, 97, 97)
button_colour_dark = (68, 61, 61)

orange = (247, 159, 13)
dark_orange = (190, 106, 10)

text_colour = (255, 255, 255)

calculator_window = window.Window(227, 296, DOUBLEBUF, bg_colour)

number_surface = window.Surface(calculator_window, 0, 104, 170, 191, bg_colour)

button_1 = ui_elements.LabelledButton(number_surface, 0, 96, 56, 47, button_colour_light, 49, button_colour_glowing, "1", text_colour, assets.SF_Pro)
button_2 = ui_elements.LabelledButton(number_surface, 57, 96, 56, 47, button_colour_light, 50, button_colour_glowing, "2", text_colour, assets.SF_Pro)
button_3 = ui_elements.LabelledButton(number_surface, 114, 96, 56, 47, button_colour_light, 51, button_colour_glowing, "3", text_colour, assets.SF_Pro)
button_4 = ui_elements.LabelledButton(number_surface, 0, 48, 56, 47, button_colour_light, 52, button_colour_glowing, "4", text_colour, assets.SF_Pro)
button_5 = ui_elements.LabelledButton(number_surface, 57, 48, 56, 47, button_colour_light, 53, button_colour_glowing, "5", text_colour, assets.SF_Pro)
button_6 = ui_elements.LabelledButton(number_surface, 114, 48, 56, 47, button_colour_light, 54, button_colour_glowing, "6", text_colour, assets.SF_Pro)
button_7 = ui_elements.LabelledButton(number_surface, 0, 0, 56, 47, button_colour_light, 55, button_colour_glowing, "7", text_colour, assets.SF_Pro)
button_8 = ui_elements.LabelledButton(number_surface, 57, 0, 56, 47, button_colour_light, 56, button_colour_glowing, "8", text_colour, assets.SF_Pro)
button_9 = ui_elements.LabelledButton(number_surface, 114, 0, 56, 47, button_colour_light, 57, button_colour_glowing, "9", text_colour, assets.SF_Pro)
button_0 = ui_elements.LabelledButton(number_surface, 0, 144, 113, 47, button_colour_light, 48, button_colour_glowing, "0", text_colour, assets.SF_Pro)

button_dot = ui_elements.LabelledButton(number_surface, 114, 144, 56, 47, button_colour_light, 44, button_colour_glowing, ",", text_colour, assets.SF_Pro)


orange_surface = window.Surface(calculator_window, 171, 56, 56, 239, bg_colour)

button_divide = ui_elements.LabelledButton(orange_surface, 0, 0, 56, 47, orange, 47, dark_orange, "÷", text_colour, assets.SF_Pro)
button_multiply = ui_elements.LabelledButton(orange_surface, 0, 48, 56, 47, orange, 56, dark_orange, "×", text_colour, assets.SF_Pro, True)
button_subtract = ui_elements.LabelledButton(orange_surface, 0, 96, 56, 47, orange, 45, dark_orange, "−", text_colour, assets.SF_Pro)
button_add = ui_elements.LabelledButton(orange_surface, 0, 144, 56, 47, orange, 61, dark_orange, "+", text_colour, assets.SF_Pro, True)
button_equals = ui_elements.LabelledButton(orange_surface, 0, 192, 56, 47, orange, 61, dark_orange, "=", text_colour, assets.SF_Pro)


top_gray_surface = window.Surface(calculator_window, 0, 56, 170, 47, bg_colour)

button_clear = ui_elements.LabelledButton(top_gray_surface, 0, 0, 56, 47, button_colour_dark, 27, button_colour_light, "AC", text_colour, assets.SF_Pro_smaller)
button_negate = ui_elements.LabelledButton(top_gray_surface, 57, 0, 56, 47, button_colour_dark, 92, button_colour_light, "⁺⁄₋", text_colour, assets.SF_Pro_smaller)
button_percent = ui_elements.LabelledButton(top_gray_surface, 114, 0, 56, 47, button_colour_dark, 53, button_colour_light, "%", text_colour, assets.SF_Pro_smaller, True)
