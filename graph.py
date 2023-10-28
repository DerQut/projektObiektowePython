import math

import pygame

import window
import ui_elements


class GraphingSurface(window.Surface):

    def __init__(self, window, x_cord, y_cord, x_size, y_size, bg_colour, line_colour, line_width, axis_colour, highlight_colour):
        super().__init__(window, x_cord, y_cord, x_size, y_size, bg_colour)

        self.line_colour = line_colour
        self.axis_colour = axis_colour
        self.highlight_colour = highlight_colour

        self.line_width = line_width

        self.points = []
        self.highlights = []

        self.last_function = ""

        self.x_unit = 75
        self.y_unit = 75

        self.zero_point = (0.5*self.x_size, 0.5*self.y_size)

    def draw(self):

        self.pg_surface.fill(self.colour)

        self.draw_axis()

        for element in self.elements:
            if element.is_visible:
                element.draw()

        if len(self.points) > 1:
            pygame.draw.lines(self.pg_surface, self.line_colour, False, self.points, self.line_width)

        for highlight in self.highlights:
            pygame.draw.circle(self.pg_surface, self.highlight_colour, highlight, 5)

        self.window.screen.blit(self.pg_surface, (self.x_cord, self.y_cord))

    def clear(self):
        self.highlights = []
        self.points = []
        self.zero_point = (0.5*self.x_size, 0.5*self.y_size)
        self.last_function = ""

        self.x_unit = 75
        self.y_unit = 75

    def draw_axis(self):
        pygame.draw.line(self.pg_surface, self.axis_colour, (0, self.zero_point[1]), (self.x_size, self.zero_point[1]))
        pygame.draw.line(self.pg_surface, self.axis_colour, (self.zero_point[0], 0), (self.zero_point[0], self.y_size))

    def draw_sine(self, angles, uses_radians):

        self.clear()

        self.last_function = "sin"

        conversion_multiplier = 1
        if not uses_radians:
            conversion_multiplier = math.pi/180

        self.x_unit = self.x_unit * conversion_multiplier

        i = -0.6 * self.x_size
        while i*self.x_unit <= 0.5 * self.x_size:
            self.points.append((self.zero_point[0]+i*self.x_unit, self.zero_point[1] - self.y_unit*math.sin(i*conversion_multiplier)))
            i=i+0.01

        self.highlights.append((self.zero_point[0]+angles*self.x_unit, self.zero_point[1] - self.y_unit*math.sin(angles*conversion_multiplier)))

    def draw_cosine(self, angles, uses_radians):

        self.clear()

        self.last_function = "cos"

        conversion_multiplier = 1
        if not uses_radians:
            conversion_multiplier = math.pi / 180

        self.x_unit = self.x_unit * conversion_multiplier

        i = -0.6 * self.x_size
        while i * self.x_unit <= 0.5 * self.x_size:
            self.points.append((self.zero_point[0] + i * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.cos(i * conversion_multiplier)))
            i = i + 0.01

        self.highlights.append((self.zero_point[0] + angles * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.cos(angles * conversion_multiplier)))

    def draw_sinh(self, angles, uses_radians):
        self.clear()

        self.last_function = "sinh"

        self.x_unit = 25
        self.y_unit = 25

        conversion_multiplier = 1
        if not uses_radians:
            conversion_multiplier = math.pi / 180

        self.x_unit = self.x_unit * conversion_multiplier

        i = -0.6 * self.x_size
        while i * self.x_unit <= 0.5 * self.x_size:
            self.points.append((self.zero_point[0] + i * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.sinh(i * conversion_multiplier)))
            i = i + 0.01

        self.highlights.append((self.zero_point[0] + angles * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.sinh(angles * conversion_multiplier)))

    def draw_cosh(self, angles, uses_radians):

        self.clear()

        self.x_unit = 25
        self.y_unit = 25

        self.last_function = "cosh"

        conversion_multiplier = 1
        if not uses_radians:
            conversion_multiplier = math.pi / 180

        self.x_unit = self.x_unit * conversion_multiplier

        i = -0.6 * self.x_size
        while i * self.x_unit <= 0.5 * self.x_size:
            self.points.append((self.zero_point[0] + i * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.cosh(i * conversion_multiplier)))
            i = i + 0.01

        self.highlights.append((self.zero_point[0] + angles * self.x_unit,
                                self.zero_point[1] - self.y_unit * math.cosh(angles * conversion_multiplier)))


    def draw_quadratic(self, a, b, c, solutions):

        self.clear()

        self.x_unit = 20
        self.y_unit = 20

        i = -0.6 * self.x_size
        while i*self.x_unit < 0.5 * self.x_size:

            self.points.append((self.zero_point[0] + i*self.x_unit, self.zero_point[1]-self.y_unit*(a*i**2 + b*i + c)))
            i = i + 0.01

        for solution in solutions:
            print(solution)
            if solution != "NULL":
                self.highlights.append((self.zero_point[0] + solution*self.x_unit, self.zero_point[1]))

