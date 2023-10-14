import pygame
from pygame.locals import *


class Window:

    def __init__(self, x_size, y_size):

        self.x_size = x_size
        self.y_size = y_size

        self.surface = pygame.surface.Surface((self.x_size, self.y_size))

        self.screen = pygame.display.set_mode((self.x_size, self.y_size), DOUBLEBUF)

        self.elements = []

        self.running = True

    def get_events(self):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                ...

    def run(self):

        self.surface.fill((200, 200, 255))

        mouse_pos = pygame.mouse.get_pos()
        self.get_events()

        for element in self.elements:
            if element.is_visible:
                element.draw()

            if element.type == "Button":
                element.mouse_check(mouse_pos)

        self.screen.blit(self.surface, (0, 0))

        pygame.display.flip()

