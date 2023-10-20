import pygame
from pygame.locals import *

import window
import ui_elements

import assets


class Calc:

    def __init__(self, text_obj, max_length):

        self.text_obj = text_obj
        self.surface = text_obj.surface
        self.window = text_obj.surface.window

        self.max_length = max_length

        self.value = 0
        self.buffer = 0

        self.number_count = 1

        self.has_comma = False
        self.is_negative = False

    def change_display_value(self, key_pressed):

        if self.text_obj.text != "0":
            if self.number_count < self.max_length:
                self.text_obj.text = self.text_obj.text + str(key_pressed)
        else:
            self.text_obj.text = str(key_pressed)

    def backspace(self):
        if self.text_obj.text != "0" and self.text_obj.text[0] and not (self.is_negative and len(self.text_obj.text) < 3):
            self.text_obj.text = list(self.text_obj.text)
            deleted = self.text_obj.text.pop()
            self.text_obj.text = ''.join(self.text_obj.text)

            if deleted == ".":
                self.has_comma = False

            if len(self.text_obj.text) == 0:
                self.text_obj.text = "0"

        else:
            self.text_obj.text = "0"
            self.is_negative = False

    def add_comma(self):

        if (not self.has_comma) and self.number_count < self.max_length:
            self.text_obj.text = self.text_obj.text + "."
            self.has_comma = True

    def divide_by_100(self):
        self.text_obj.text = str(self.value * 0.01)
        if self.value % 100:
            self.has_comma = True
        else:
            self.has_comma = False
            self.text_obj.text = str(int(self.value*0.01))

        self.calculate_value()

    def soft_clear(self):
        self.has_comma = False
        self.is_negative = False
        self.text_obj.text = "0"
        self.number_count = 1

    def hard_clear(self):
        self.soft_clear()
        self.buffer = 0

    def change_sign(self):
        self.text_obj.text = str(self.value*-1)
        self.is_negative = not self.is_negative

    def calculate_value(self):

        self.crop()

        self.number_count = len(self.text_obj.text) - int(self.has_comma) - int(self.is_negative)

        if not self.has_comma:
            self.value = int(self.text_obj.text)

        else:
            self.value = float(self.text_obj.text + "0")

        print(self.value)

    def crop(self):
        if len(self.text_obj.text) - self.has_comma - self.is_negative > self.max_length:
            self.text_obj.text = "{:.4f}".format(float(self.text_obj.text))
            if float(self.text_obj.text) == int(float(self.text_obj.text)):
                self.text_obj.text = str(int(float(self.text_obj.text)))
                self.has_comma = False


def button_handler(event_key, is_shifting):

    if pygame.K_0 <= event_key <= pygame.K_9 and not is_shifting:
        calculator_obj.change_display_value(event_key-48)

    elif event_key == pygame.K_ESCAPE:
        if not is_shifting:
            calculator_obj.soft_clear()
        else:
            calculator_obj.hard_clear()

    elif event_key == pygame.K_COMMA:
        calculator_obj.add_comma()

    elif event_key == pygame.K_BACKSPACE:
        calculator_obj.backspace()

    elif event_key == pygame.K_5 and is_shifting or event_key == pygame.K_PERCENT:
        calculator_obj.divide_by_100()

    elif event_key == pygame.K_BACKSLASH:
        calculator_obj.change_sign()

    elif event_key == K_LSHIFT:
        if is_shifting:
            button_clear.label.change_text("AC")
        else:
            button_clear.label.change_text("C")
        button_clear.center_text()

    calculator_obj.text_obj.reload()
    calculator_obj.text_obj.push_right(8)

    calculator_obj.calculate_value()


def key_unifier(event_key):
    if event_key == pygame.K_PERIOD:
        return pygame.K_COMMA
    elif event_key == pygame.K_RETURN:
        return pygame.K_EQUALS
    return event_key


def key_separator(event_key):
    if event_key == pygame.K_5:
        return pygame.K_PERCENT
    if event_key == pygame.K_8:
        return pygame.K_ASTERISK
    return event_key


bg_colour = (43, 34, 34)

button_colour_glowing = (150, 147, 147)
button_colour_light = (102, 97, 97)
button_colour_dark = (68, 61, 61)

orange = (247, 159, 13)
dark_orange = (190, 106, 10)

text_colour = (255, 255, 255)

calculator_window = window.Window(227, 296, DOUBLEBUF, bg_colour, "macOS Calculator")

number_surface = window.Surface(calculator_window, 0, 104, 170, 191, bg_colour)

button_1 = ui_elements.LabelledButton(number_surface, 0, 96, 56, 47, button_colour_light, 49, button_colour_glowing, "1", text_colour, assets.SF_Pro_Medium_24)
button_2 = ui_elements.LabelledButton(number_surface, 57, 96, 56, 47, button_colour_light, 50, button_colour_glowing, "2", text_colour, assets.SF_Pro_Medium_24)
button_3 = ui_elements.LabelledButton(number_surface, 114, 96, 56, 47, button_colour_light, 51, button_colour_glowing, "3", text_colour, assets.SF_Pro_Medium_24)
button_4 = ui_elements.LabelledButton(number_surface, 0, 48, 56, 47, button_colour_light, 52, button_colour_glowing, "4", text_colour, assets.SF_Pro_Medium_24)
button_5 = ui_elements.LabelledButton(number_surface, 57, 48, 56, 47, button_colour_light, 53, button_colour_glowing, "5", text_colour, assets.SF_Pro_Medium_24)
button_6 = ui_elements.LabelledButton(number_surface, 114, 48, 56, 47, button_colour_light, 54, button_colour_glowing, "6", text_colour, assets.SF_Pro_Medium_24)
button_7 = ui_elements.LabelledButton(number_surface, 0, 0, 56, 47, button_colour_light, 55, button_colour_glowing, "7", text_colour, assets.SF_Pro_Medium_24)
button_8 = ui_elements.LabelledButton(number_surface, 57, 0, 56, 47, button_colour_light, 56, button_colour_glowing, "8", text_colour, assets.SF_Pro_Medium_24)
button_9 = ui_elements.LabelledButton(number_surface, 114, 0, 56, 47, button_colour_light, 57, button_colour_glowing, "9", text_colour, assets.SF_Pro_Medium_24)
button_0 = ui_elements.LabelledButton(number_surface, 0, 144, 113, 47, button_colour_light, 48, button_colour_glowing, "0", text_colour, assets.SF_Pro_Medium_24)

button_dot = ui_elements.LabelledButton(number_surface, 114, 144, 56, 47, button_colour_light, 44, button_colour_glowing, ".", text_colour, assets.SF_Pro_Medium_24)


orange_surface = window.Surface(calculator_window, 171, 56, 56, 239, bg_colour)

button_divide = ui_elements.LabelledButton(orange_surface, 0, 0, 56, 47, orange, 47, dark_orange, "÷", text_colour, assets.SF_Pro_Medium_24)
button_multiply = ui_elements.LabelledButton(orange_surface, 0, 48, 56, 47, orange, 42, dark_orange, "×", text_colour, assets.SF_Pro_Medium_24, True)
button_subtract = ui_elements.LabelledButton(orange_surface, 0, 96, 56, 47, orange, 45, dark_orange, "−", text_colour, assets.SF_Pro_Medium_24)
button_add = ui_elements.LabelledButton(orange_surface, 0, 144, 56, 47, orange, 61, dark_orange, "+", text_colour, assets.SF_Pro_Medium_24, True)
button_equals = ui_elements.LabelledButton(orange_surface, 0, 192, 56, 47, orange, 61, dark_orange, "=", text_colour, assets.SF_Pro_Medium_24)


top_gray_surface = window.Surface(calculator_window, 0, 56, 170, 47, bg_colour)

button_clear = ui_elements.LabelledButton(top_gray_surface, 0, 0, 56, 47, button_colour_dark, 27, button_colour_light, "C", text_colour, assets.SF_Pro_Medium_20, 0.5)
button_negate = ui_elements.LabelledButton(top_gray_surface, 57, 0, 56, 47, button_colour_dark, pygame.K_BACKSLASH, button_colour_light, "⁺⁄₋", text_colour, assets.SF_Pro_Medium_20)
button_percent = ui_elements.LabelledButton(top_gray_surface, 114, 0, 56, 47, button_colour_dark, 37, button_colour_light, "%", text_colour, assets.SF_Pro_Medium_20, True)


top_display_surface = window.Surface(calculator_window, 0, 0, 227, 56, bg_colour)

calculator_obj = Calc(ui_elements.Text(top_display_surface, 0, 2, assets.SF_Pro_Light_42, "0", text_colour), 8)
