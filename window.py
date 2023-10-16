import pygame
from pygame.locals import *

import calculator


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
        self.is_clicking = False
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.is_clicking = True

            elif event.type == pygame.KEYDOWN:
                ...

    def run(self):

        self.screen.fill(self.bg_colour)

        for surface in self.surfaces:
            surface.draw()

        mouse_pos = pygame.mouse.get_pos()
        self.get_events()

        for element in self.surfaces[0].elements:
            if element.is_visible:
                element.draw()

            if element.type == "Button":
                if element.mouse_check(mouse_pos) and self.is_clicking:
                    calculator.button_handler(element.button_id)

        pygame.display.flip()
