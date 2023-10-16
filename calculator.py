import pygame

import window
import ui_elements

import assets


def button_handler(button_id):
    if button_id == 2:
        test_text.change_texture(assets.font2, "Bonjour!!!", (0, 0, 0))

    elif button_id == 1:
        test_text.is_visible = not test_text.is_visible


window = window.Window(1280, 720)

test_button_1 = ui_elements.Button(window, 302, 0, assets.test, 1)
test_button_2 = ui_elements.Button(window, 302, 32, assets.test, 2)

hint_text_1 = ui_elements.Text(window, 340, 0, assets.font2, "POKAŻ / UKRYJ", (0, 0, 0))
hint_text_2 = ui_elements.Text(window, 340, 32, assets.font2, "ZMIEŃ CZCIONKĘ", (0, 0, 0))

test_text = ui_elements.Text(window, 500, 500, assets.font1, "Dzień dobry!!", (0, 0, 0), False)

white_bar = ui_elements.Rect(window, 0, 0, 300, 720, (255, 255, 255))
bar_border = ui_elements.Rect(window, 300, 0, 2, 720, (128, 128, 150))
