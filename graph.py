import pygame

import window
import ui_elements


class GraphingSurface(window.Surface):

    def __init__(self, window, x_cord, y_cord, x_size, y_size, bg_colour, line_colour, line_width):
        super().__init__(window, x_cord, y_cord, x_size, y_size, bg_colour)

        self.line_colour = line_colour
        self.line_width = line_width
        self.points = [(0, 0), (100, 100)]

    def draw(self):

        self.pg_surface.fill(self.colour)

        for element in self.elements:
            if element.is_visible:
                element.draw()

        pygame.draw.lines(self.pg_surface, self.line_colour, False, self.points, self.line_width)

        self.window.screen.blit(self.pg_surface, (self.x_cord, self.y_cord))

