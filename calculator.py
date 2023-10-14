import pygame

import window
import ui_elements

import assets

window = window.Window(1280, 720)
button = ui_elements.Element(window, 300, 300, assets.test)
text = ui_elements.Text(window, 500, 500, assets.font, "HELLO", (0, 0, 0), True)
