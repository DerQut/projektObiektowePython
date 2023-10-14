import pygame
import window

class Element:

    def __init__(self, window, x_cord, y_cord, texture, is_visible=True):

        self.window = window

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.is_visible = is_visible

        self.window.elements.append(self)

        self.texture = texture

        self.type = "Element"

    def draw(self):
        self.window.surface.blit(self.texture, (self.x_cord, self.y_cord))

    def change_image(self, new_texture):
        self.texture = new_texture


class Text(Element):

    def __init__(self, window, x_cord, y_cord, font, text, colour, is_visible):
        super().__init__(window, x_cord, y_cord, font.render(text, False, colour), is_visible)

        self.font = font
        self.text = text
        self.colour = colour

        self.type = "Text"

class Button(Element):

    def __init__(self, window, x_cord, y_cord, texture, button_id, is_visible):
        super().__init__(window, x_cord, y_cord, texture, is_visible)

        self.button_id = button_id

        self.type = "Button"

        self.is_highlighted = True

    def mouse_check(self, mouse_pos):
        if mouse_pos[0] > self.x_cord and mouse_pos[1] > self.y_cord:
            self.is_highlighted = True
        else:
            self.is_highlighted = False
