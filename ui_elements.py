import pygame
import window


class Rect:

    def __init__(self, window, x_cord, y_cord, x_size, y_size, colour, is_visible=True):

        self.window = window

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.x_size = x_size
        self.y_size = y_size

        self.colour = colour

        self.is_visible = is_visible

        self.type = "Rect"

        self.rect = pygame.rect.Rect(x_cord, y_cord, x_size, y_size)

        self.window.elements.append(self)

    def draw(self):
        self.window.surface.fill(self.colour, self.rect)


class Element:

    def __init__(self, window, x_cord, y_cord, texture, is_visible=True):

        self.window = window

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.is_visible = is_visible

        self.window.elements.append(self)

        self.texture = texture

        self.width = self.texture.get_width()
        self.height = self.texture.get_height()

        self.type = "Element"

    def draw(self):
        self.window.surface.blit(self.texture, (self.x_cord, self.y_cord))

    def change_texture(self, new_texture):
        self.texture = new_texture

        self.width = self.texture.get_width()
        self.height = self.texture.get_height()


class Text(Element):

    def __init__(self, window, x_cord, y_cord, font, text, colour, is_visible=True):
        super().__init__(window, x_cord, y_cord, font.render(text, False, colour), is_visible)

        self.font = font
        self.text = text
        self.colour = colour

        self.type = "Text"

    def change_texture(self, new_font, new_text, new_colour):
        super().change_texture(new_font.render(new_text, False, new_colour))



class Button(Element):

    def __init__(self, window, x_cord, y_cord, texture, button_id, is_visible=True):
        super().__init__(window, x_cord, y_cord, texture, is_visible)

        self.button_id = button_id

        self.type = "Button"

        self.is_highlighted = True

    def mouse_check(self, mouse_pos):
        if self.x_cord+self.width > mouse_pos[0] > self.x_cord and self.y_cord+self.height > mouse_pos[1] > self.y_cord:
            self.is_highlighted = True
        else:
            self.is_highlighted = False

        return self.is_highlighted
