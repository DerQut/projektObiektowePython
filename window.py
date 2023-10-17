# TODO: kalulator obecnie używa prawego klawisza myszy; dowiedz się, czemu lewy nie chciał działać

import pygame
from pygame.locals import *

import calculator


class Surface:

    def __init__(self, window, x_cord, y_cord, x_size, y_size, colour):

        self.window = window

        self.elements = []

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.x_size = x_size
        self.y_size = y_size

        self.colour = colour

        self.pg_surface = pygame.surface.Surface((self.x_size, self.y_size))

        self.window.surfaces.append(self)

    def draw(self):

        self.pg_surface.fill(self.colour)

        for element in self.elements:
            if element.is_visible:
                element.draw()

        self.window.screen.blit(self.pg_surface, (self.x_cord, self.y_cord))



class Window:

    def __init__(self, x_size, y_size, flags, bg_colour):

        self.x_size = x_size
        self.y_size = y_size

        self.surfaces = []

        self.screen = pygame.display.set_mode((self.x_size, self.y_size), flags)

        self.bg_colour = bg_colour

        self.running = True
        self.is_clicking = False

    def get_events(self):

        events = pygame.event.get()

        mouse_pos = pygame.mouse.get_pos()
        self.is_clicking = False

        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    self.is_clicking = True

                    for surface in self.surfaces:
                        for element in surface.elements:

                            if element.type == "Button" or element.type == "LabelledButton":
                                if element.mouse_check(mouse_pos) and self.is_clicking:
                                    calculator.button_handler(element.unicode_id)
                                    element.colour = element.secondary_colour

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    for surface in self.surfaces:
                        for element in surface.elements:
                            if element.type == "Button" or element.type == "LabelledButton":
                                element.colour = element.main_colour

            elif event.type == pygame.KEYDOWN:
                calculator.button_handler(event.key)
                for surface in self.surfaces:
                    for element in surface.elements:
                        if element.type == "Button" or element.type == "LabelledButton":
                            if element.unicode_id == event.key:
                                element.colour = element.secondary_colour

            elif event.type == pygame.KEYUP:
                for surface in self.surfaces:
                    for element in surface.elements:
                        if element.type == "Button" or element.type == "LabelledButton":
                            if element.unicode_id == event.key:
                                element.colour = element.main_colour

    def run(self):

        self.screen.fill(self.bg_colour)

        for surface in self.surfaces:
            surface.draw()

        self.get_events()

        pygame.display.flip()
