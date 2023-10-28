import math
import random

import numpy
import pygame
from pygame.locals import *

import window
import ui_elements
import graph

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

        self.uses_radians = False

        self.last_operator = ""
        self.operation_buffer = 0

        self.ax2 = 0
        self.bx = 0
        self.c = 0

        self.x1 = 0
        self.x2 = 0

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
        self.value = 0
        self.number_count = 1

    def hard_clear(self):
        self.soft_clear()
        self.buffer = 0
        self.last_operator = ""
        self.ax2 = 0
        self.bx = 0
        self.c = 0
        self.x1 = 0
        self.x2 = 0

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

    def add(self):

        self.buffer = self.buffer + self.value
        self.soft_clear()
        self.last_operator = "+"
        self.crop_buffer()

    def subtract(self):

        if self.buffer == 0:
            self.buffer = self.value
        else:
            self.buffer = self.buffer - self.value
        self.soft_clear()
        self.last_operator = "-"
        self.crop_buffer()

    def multiply(self):
        if self.buffer == 0:
            self.buffer = self.buffer = self.value
        else:
            self.buffer = self.buffer * self.value

        self.soft_clear()
        self.last_operator = "*"
        self.crop_buffer()

    def divide(self):
        if self.buffer == 0:
            self.buffer = self.value
        else:
            if self.value:
                self.buffer = self.buffer / self.value
            else:
                print("forbidden")

        self.soft_clear()
        self.last_operator = "/"
        self.crop_buffer()

    def sin(self):
        if self.uses_radians:
            self.value = math.sin(self.value)
        else:
            self.value = math.sin(self.value / 180 * math.pi)
        self.simplify()

    def sinh(self):
        self.value = math.sinh(self.value)
        self.simplify()

    def cos(self):
        if self.uses_radians:
            self.value = math.cos(self.value)
        else:
            self.value = math.cos(self.value / 180 * math.pi)
        self.simplify()

    def cosh(self):
        if self.uses_radians:
            self.value = math.cosh(self.value)
        else:
            self.value = math.cosh(self.value * math.pi / 180)
        self.simplify()

    def tan(self):
        self.value = math.tan(self.value)
        self.simplify()

    def tanh(self):
        self.value = math.tanh(self.value)
        self.simplify()

    def pi(self):
        if self.value:
            self.value = self.value * math.pi
        else:
            self.value = math.pi

        self.simplify()

    def factorial(self):
        if not self.has_comma and self.value >= 0:
            self.value = math.factorial(self.value)
        self.simplify()

    def e(self):
        if self.value:
            self.value = math.e * self.value
        else:
            self.value = math.e
        self.simplify()

    def e_to_x(self):
        self.value = math.e ** self.value
        self.simplify()

    def ten_to_x(self):
        self.value = 10 ** self.value
        self.simplify()

    def log(self):
        if self.value > 0:
            self.value = math.log10(self.value)
            self.simplify()

    def ln(self):
        if self.value > 0:
            self.value = math.log(self.value, math.e)
            self.simplify()

    def randomise(self):
        self.value = random.uniform(0, 1)
        self.simplify()

    def round(self):
        print(abs(self.value) - int(abs(self.value)))
        if abs(self.value) - int(abs(self.value)) >= 0.5:
            self.value = int(self.value) + numpy.sign(self.value)
        else:
            self.value = int(self.value)
        self.simplify()

    def inverse(self):
        if self.value:
            self.value = 1/self.value
            self.simplify()

    def square(self):
        self.value = self.value * self.value
        self.simplify()

    def cube(self):
        self.value = self.value ** 3
        self.simplify()

    def square_root(self):
        if self.value > 0:
            self.value = math.sqrt(self.value)
            self.simplify()

    def cubic_root(self):
        if self.value >= 0:
            self.value = pow(self.value, 1/3)
        else:
            self.value = pow(abs(self.value), 1/3)*(-1)
        self.simplify()

    def equals(self):

        if self.last_operator == "+":
            self.add()

        elif self.last_operator == "*":
            self.multiply()

        elif self.last_operator == "/":
            self.divide()

        elif self.last_operator == "-":
            self.subtract()

        else:
            self.buffer = self.value

        self.last_operator = ""
        self.value = self.buffer
        self.buffer = 0
        if self.value < 0:
            self.is_negative = True
        else:
            self.is_negative = False
        self.simplify()

    def crop(self):
        if len(self.text_obj.text) - self.has_comma - self.is_negative > self.max_length:
            if self.has_comma:
                self.text_obj.text = "{:.8f}".format(float(self.text_obj.text))
                if float(self.text_obj.text) == int(float(self.text_obj.text)):
                    self.text_obj.text = str(int(float(self.text_obj.text)))
                    self.has_comma = False
            else:
                self.text_obj.text = "9"*self.max_length
                if self.is_negative:
                    self.text_obj.text = "-" + self.text_obj.text
                self.calculate_value()

    def crop_buffer(self):
        if abs(self.buffer >= int("1" + self.max_length * "0")):
            if self.buffer > 0:
                self.buffer = int("9"*self.max_length)
            else:
                self.buffer = int("-" + "9"*self.max_length)

    def intify(self):
        if int(self.value) == float(self.value):
            self.value = int(self.value)
            self.has_comma = False
        else:
            self.has_comma = True

    def simplify(self):
        self.intify()
        self.text_obj.text = str(self.value)
        self.crop()

    def quadratic(self):

        self.x1 = 0
        self.x2 = 0

        delta = self.bx**2 - 4*self.ax2*self.c

        if delta >= 0 and self.ax2:
            self.x1 = (-self.bx - math.sqrt(delta))/(2*self.ax2)
            self.x2 = (-self.bx + math.sqrt(delta))/(2*self.ax2)


def button_handler(event_key, needs_shift, is_shifting):

    # Check
    if (needs_shift != is_shifting) and (needs_shift != 0.5):
        return

    # Number input
    if pygame.K_0 <= event_key <= pygame.K_9 and not is_shifting:
        calculator_obj.change_display_value(event_key-48)

    # Clear
    elif event_key == pygame.K_ESCAPE:
        if not is_shifting or is_shifting == 0.5:
            calculator_obj.soft_clear()
        else:
            calculator_obj.hard_clear()

            button_ax2_value.label.colour = button_colour_light
            button_bx_value.label.colour = button_colour_light
            button_c_value.label.colour = button_colour_light

            button_ax2_value.label.change_text("0")
            button_ax2_value.center_text()

            button_bx_value.label.change_text("0")
            button_bx_value.center_text()

            button_c_value.label.change_text("0")
            button_c_value.center_text()

    # Useful buttons
    elif event_key == pygame.K_COMMA or event_key == pygame.K_PERIOD:
        calculator_obj.add_comma()

    elif event_key == pygame.K_BACKSPACE:
        calculator_obj.backspace()

    elif event_key == pygame.K_BACKSLASH:
        calculator_obj.change_sign()

    elif event_key == pygame.K_5 and is_shifting:
        calculator_obj.divide_by_100()

    # Basic operations
    elif event_key == pygame.K_EQUALS and is_shifting:
        calculator_obj.equals()
        calculator_obj.add()

    elif event_key == pygame.K_MINUS and not is_shifting:
        calculator_obj.equals()
        calculator_obj.subtract()

    elif event_key == pygame.K_8 and is_shifting:
        calculator_obj.equals()
        calculator_obj.multiply()

    elif event_key == pygame.K_SLASH:
        calculator_obj.equals()
        calculator_obj.divide()

    elif (event_key == pygame.K_EQUALS and not is_shifting) or event_key == pygame.K_RETURN:
        calculator_obj.equals()

    # trigonometric functions
    elif event_key == pygame.K_s:
        if not is_shifting:
            calculator_obj.sin()
        else:
            calculator_obj.sinh()

    elif event_key == pygame.K_k:
        if not is_shifting:
            calculator_obj.cos()
        else:
            calculator_obj.cosh()

    elif event_key == pygame.K_t:
        if not is_shifting:
            calculator_obj.tan()
        else:
            calculator_obj.tanh()

    # constants
    elif event_key == pygame.K_p and not is_shifting:
        calculator_obj.pi()

    elif event_key == pygame.K_e:
        if not is_shifting:
            calculator_obj.e()
        else:
            calculator_obj.e_to_x()

    # logarithms
    elif event_key == pygame.K_l:
        if is_shifting:
            calculator_obj.ln()
        else:
            calculator_obj.log()

    # Powers and roots
    elif event_key == pygame.K_2 and is_shifting:
        calculator_obj.square()

    elif event_key == pygame.K_3 and is_shifting:
        calculator_obj.cube()

    elif event_key == pygame.K_r:
        if is_shifting:
            calculator_obj.cubic_root()
        else:
            calculator_obj.square_root()

    elif event_key == pygame.K_0 and is_shifting:
        calculator_obj.ten_to_x()

    elif event_key == pygame.K_1 and is_shifting:
        calculator_obj.factorial()

    elif event_key == pygame.K_i:
        calculator_obj.inverse()

    # Rad/Deg button
    elif event_key == pygame.K_m:
        if calculator_obj.uses_radians:
            button_deg.label.change_text("Rad")
            calculator_obj.uses_radians = False
        else:
            button_deg.label.change_text("Deg")
            calculator_obj.uses_radians = True
        button_deg.center_text()

    # ax^2 + bx + c
    elif event_key == pygame.K_F1:
        button_ax2_value.center_text()
        if is_shifting:
            calculator_obj.ax2 = 0
            button_ax2_value.label.colour = button_colour_light
        else:
            calculator_obj.ax2 = calculator_obj.value
            button_ax2_value.label.colour = text_colour

        button_ax2_value.label.text = "{:.2f}".format(calculator_obj.ax2)
        button_ax2_value.label.reload()
        button_ax2_value.center_text()

    elif event_key == pygame.K_F2:
        button_bx_value.center_text()
        if is_shifting:
            calculator_obj.bx = 0
            button_bx_value.label.colour = button_colour_light
        else:
            calculator_obj.bx = calculator_obj.value
            button_bx_value.label.colour = text_colour

        button_bx_value.label.text = "{:.2f}".format(calculator_obj.bx)
        button_bx_value.label.reload()
        button_bx_value.center_text()

    elif event_key == pygame.K_F3:
        button_c_value.center_text()
        if is_shifting:
            calculator_obj.c = 0
            button_c_value.label.colour = button_colour_light
        else:
            calculator_obj.c = calculator_obj.value
            button_c_value.label.colour = text_colour

        button_c_value.label.text = "{:.2f}".format(calculator_obj.c)
        button_c_value.label.reload()
        button_c_value.center_text()

    # Useless shit
    elif event_key == pygame.K_z:
        calculator_obj.round()

    elif event_key == pygame.K_q:
        calculator_obj.randomise()

    # Change buttons appearance depending on L_SHIFT input
    elif event_key == K_LSHIFT:
        if is_shifting:
            button_clear.label.change_text("AC")
        else:
            button_clear.label.change_text("C")
        button_clear.center_text()

    calculator_obj.quadratic()

    calculator_obj.text_obj.reload()
    calculator_obj.text_obj.push_right(8)

    calculator_obj.calculate_value()


def loop_action():
    button_first_result.label.change_text("{:.1f}".format(float(calculator_obj.x1)))
    button_second_result.label.change_text("{:.1f}".format(float(calculator_obj.x2)))
    button_second_result.center_text()
    button_first_result.center_text()




bg_colour = (43, 34, 34)

button_colour_glowing = (150, 147, 147)
button_colour_light = (102, 97, 97)
button_colour_dark = (68, 61, 61)

orange = (247, 159, 13)
dark_orange = (190, 106, 10)

text_colour = (255, 255, 255)


calculator_window = window.Window(569+480, 295, DOUBLEBUF, bg_colour, "macOS Calculator")


###
number_surface = window.Surface(calculator_window, 342, 104, 170, 191, bg_colour)

button_1 = ui_elements.LabelledButton(number_surface, 0, 96, 56, 47, button_colour_light, pygame.K_1, button_colour_glowing, "1", text_colour, assets.SF_Pro_Medium_24)
button_2 = ui_elements.LabelledButton(number_surface, 57, 96, 56, 47, button_colour_light, pygame.K_2, button_colour_glowing, "2", text_colour, assets.SF_Pro_Medium_24)
button_3 = ui_elements.LabelledButton(number_surface, 114, 96, 56, 47, button_colour_light, pygame.K_3, button_colour_glowing, "3", text_colour, assets.SF_Pro_Medium_24)
button_4 = ui_elements.LabelledButton(number_surface, 0, 48, 56, 47, button_colour_light, pygame.K_4, button_colour_glowing, "4", text_colour, assets.SF_Pro_Medium_24)
button_5 = ui_elements.LabelledButton(number_surface, 57, 48, 56, 47, button_colour_light, pygame.K_5, button_colour_glowing, "5", text_colour, assets.SF_Pro_Medium_24)
button_6 = ui_elements.LabelledButton(number_surface, 114, 48, 56, 47, button_colour_light, pygame.K_6, button_colour_glowing, "6", text_colour, assets.SF_Pro_Medium_24)
button_7 = ui_elements.LabelledButton(number_surface, 0, 0, 56, 47, button_colour_light, pygame.K_7, button_colour_glowing, "7", text_colour, assets.SF_Pro_Medium_24)
button_8 = ui_elements.LabelledButton(number_surface, 57, 0, 56, 47, button_colour_light, pygame.K_8, button_colour_glowing, "8", text_colour, assets.SF_Pro_Medium_24)
button_9 = ui_elements.LabelledButton(number_surface, 114, 0, 56, 47, button_colour_light, pygame.K_9, button_colour_glowing, "9", text_colour, assets.SF_Pro_Medium_24)
button_0 = ui_elements.LabelledButton(number_surface, 0, 144, 113, 47, button_colour_light, pygame.K_0, button_colour_glowing, "0", text_colour, assets.SF_Pro_Medium_24)

button_dot = ui_elements.LabelledButton(number_surface, 114, 144, 56, 47, button_colour_light, pygame.K_COMMA, button_colour_glowing, ".", text_colour, assets.SF_Pro_Medium_24)


###
orange_surface = window.Surface(calculator_window, 171+342, 56, 56, 239, bg_colour)

button_divide = ui_elements.LabelledButton(orange_surface, 0, 0, 56, 47, orange, pygame.K_SLASH, dark_orange, "÷", text_colour, assets.SF_Pro_Medium_24)
button_multiply = ui_elements.LabelledButton(orange_surface, 0, 48, 56, 47, orange, pygame.K_8, dark_orange, "×", text_colour, assets.SF_Pro_Medium_24, True)
button_subtract = ui_elements.LabelledButton(orange_surface, 0, 96, 56, 47, orange, pygame.K_MINUS, dark_orange, "−", text_colour, assets.SF_Pro_Medium_24)
button_add = ui_elements.LabelledButton(orange_surface, 0, 144, 56, 47, orange, pygame.K_EQUALS, dark_orange, "+", text_colour, assets.SF_Pro_Medium_24, True)
button_equals = ui_elements.LabelledButton(orange_surface, 0, 192, 56, 47, orange, pygame.K_EQUALS, dark_orange, "=", text_colour, assets.SF_Pro_Medium_24, False)


###
top_gray_surface = window.Surface(calculator_window, 342, 56, 170, 47, bg_colour)

button_clear = ui_elements.LabelledButton(top_gray_surface, 0, 0, 56, 47, button_colour_dark, pygame.K_ESCAPE, button_colour_light, "C", text_colour, assets.SF_Pro_Medium_20, 0.5)
button_negate = ui_elements.LabelledButton(top_gray_surface, 57, 0, 56, 47, button_colour_dark, pygame.K_BACKSLASH, button_colour_light, "⁺⁄₋", text_colour, assets.SF_Pro_Medium_20)
button_percent = ui_elements.LabelledButton(top_gray_surface, 114, 0, 56, 47, button_colour_dark, pygame.K_5, button_colour_light, "%", text_colour, assets.SF_Pro_Medium_20, True)


###
scientific_surface = window.Surface(calculator_window, 0, 56, 342, 239, bg_colour)

button_deg = ui_elements.LabelledButton(scientific_surface, 0, 192, 56, 47, button_colour_dark, pygame.K_m, button_colour_light, "Rad", text_colour, assets.SF_Pro_Medium_20, 0.5)
button_sinh = ui_elements.LabelledButton(scientific_surface, 57, 192, 56, 47, button_colour_dark, pygame.K_s, button_colour_light, "sinh", text_colour, assets.SF_Pro_Medium_20, True)
button_cosh = ui_elements.LabelledButton(scientific_surface, 114, 192, 56, 47, button_colour_dark, pygame.K_c, button_colour_light, "cosh", text_colour, assets.SF_Pro_Medium_20, True)
button_tanh = ui_elements.LabelledButton(scientific_surface, 171, 192, 56, 47, button_colour_dark, pygame.K_t, button_colour_light, "tanh", text_colour, assets.SF_Pro_Medium_20, True)
button_e = ui_elements.LabelledButton(scientific_surface, 228, 192, 56, 47, button_colour_dark, pygame.K_e, button_colour_light, "e", text_colour, assets.SF_Pro_Medium_20, False)
button_ln = ui_elements.LabelledButton(scientific_surface, 285, 192, 56, 47, button_colour_dark, pygame.K_l, button_colour_light, "ln", text_colour, assets.SF_Pro_Medium_20, True)

button_factorial = ui_elements.LabelledButton(scientific_surface, 0, 144, 56, 47, button_colour_dark, pygame.K_1, button_colour_light, "x!", text_colour, assets.SF_Pro_Medium_20, True)
button_sin = ui_elements.LabelledButton(scientific_surface, 57, 144, 56, 47, button_colour_dark, pygame.K_s, button_colour_light, "sin", text_colour, assets.SF_Pro_Medium_20, False)
button_cos = ui_elements.LabelledButton(scientific_surface, 114, 144, 56, 47, button_colour_dark, pygame.K_c, button_colour_light, "cos", text_colour, assets.SF_Pro_Medium_20, False)
button_tan = ui_elements.LabelledButton(scientific_surface, 171, 144, 56, 47, button_colour_dark, pygame.K_t, button_colour_light, "tan", text_colour, assets.SF_Pro_Medium_20, False)
button_pi = ui_elements.LabelledButton(scientific_surface, 228, 144, 56, 47, button_colour_dark, pygame.K_p, button_colour_light, "π", text_colour, assets.SF_Pro_Medium_20, False)
button_log10 = ui_elements.LabelledButton(scientific_surface, 285, 144, 56, 47, button_colour_dark, pygame.K_l, button_colour_light, "log₁₀", text_colour, assets.SF_Pro_Medium_20, False)

button_inverse = ui_elements.LabelledButton(scientific_surface, 0, 96, 56, 47, button_colour_dark, pygame.K_i, button_colour_light, "x⁻¹", text_colour, assets.SF_Pro_Medium_20, 0.5)
button_square_root = ui_elements.LabelledButton(scientific_surface, 57, 96, 56, 47, button_colour_dark, pygame.K_r, button_colour_light, "√x", text_colour, assets.SF_Pro_Medium_20, False)
button_cubic_root = ui_elements.LabelledButton(scientific_surface, 114, 96, 56, 47, button_colour_dark, pygame.K_r, button_colour_light, "³√x", text_colour, assets.SF_Pro_Medium_20, True)
button_squared = ui_elements.LabelledButton(scientific_surface, 171, 96, 56, 47, button_colour_dark, pygame.K_2, button_colour_light, "x²", text_colour, assets.SF_Pro_Medium_20, True)
button_cubed = ui_elements.LabelledButton(scientific_surface, 228, 96, 56, 47, button_colour_dark, pygame.K_3, button_colour_light, "x³", text_colour, assets.SF_Pro_Medium_20, True)
button_e_to_x = ui_elements.LabelledButton(scientific_surface, 285, 96, 56, 47, button_colour_dark, pygame.K_e, button_colour_light, "e^x", text_colour, assets.SF_Pro_Medium_20, True)

button_10_to_x = ui_elements.LabelledButton(scientific_surface, 285, 48, 56, 47, button_colour_dark, pygame.K_0, button_colour_light, "10^x", text_colour, assets.SF_Pro_Medium_18, True)
button_round = ui_elements.LabelledButton(scientific_surface, 0, 48, 56, 47, button_colour_dark, pygame.K_z, button_colour_light, "int()", text_colour, assets.SF_Pro_Medium_18, 0.5)
button_ax2_value = ui_elements.LabelledButton(scientific_surface, 57, 48, 56, 47, button_colour_dark, pygame.K_F1, button_colour_light, "0", button_colour_light, assets.SF_Pro_Medium_18, True)
button_bx_value = ui_elements.LabelledButton(scientific_surface, 114, 48, 56, 47, button_colour_dark, pygame.K_F2, button_colour_light, "0", button_colour_light, assets.SF_Pro_Medium_18, True)
button_c_value = ui_elements.LabelledButton(scientific_surface, 171, 48, 56, 47, button_colour_dark, pygame.K_F3, button_colour_light, "0", button_colour_light, assets.SF_Pro_Medium_18, True)
button_first_result = ui_elements.LabelledButton(scientific_surface, 228, 48, 56, 47, button_colour_dark, 0, button_colour_dark, "0", button_colour_light, assets.SF_Pro_Medium_18, 0.5)

button_random = ui_elements.LabelledButton(scientific_surface, 0, 0, 56, 47, button_colour_dark, pygame.K_q, button_colour_light, "Rand", text_colour, assets.SF_Pro_Medium_18, 0.5)
button_ax2 = ui_elements.LabelledButton(scientific_surface, 57, 0, 56, 47, button_colour_dark, pygame.K_F1, button_colour_light, "ax²", text_colour, assets.SF_Pro_Medium_20, False)
button_bx = ui_elements.LabelledButton(scientific_surface, 114, 0, 56, 47, button_colour_dark, pygame.K_F2, button_colour_light, "bx", text_colour, assets.SF_Pro_Medium_20, False)
button_c = ui_elements.LabelledButton(scientific_surface, 171, 0, 56, 47, button_colour_dark, pygame.K_F3, button_colour_light, "c", text_colour, assets.SF_Pro_Medium_20, False)
button_second_result = ui_elements.LabelledButton(scientific_surface, 228, 0, 56, 47, button_colour_dark, 0, button_colour_dark, "0", button_colour_light, assets.SF_Pro_Medium_18, 0.5)
button_graph = ui_elements.LabelledButton(scientific_surface, 285, 0, 56, 47, button_colour_dark, pygame.K_g, button_colour_light, "Graph", text_colour, assets.SF_Pro_Medium_18, 0.5)


###
top_display_surface = window.Surface(calculator_window, 0, 0, 569, 56, bg_colour)


###
graphing_surface = graph.GraphingSurface(calculator_window, 570, 0, 480, 295, (31, 22, 22), text_colour, 5)

###
calculator_obj = Calc(ui_elements.Text(top_display_surface, 0, 2, assets.SF_Pro_Light_42, "0", text_colour), 22)
