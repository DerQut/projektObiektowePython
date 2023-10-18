import pygame

# TODO: kalulator jak w windows: JEDNO POLE EDYCYJNE, guziczki, PRZECINEK (lub kropka), sinusy cosinusy

if __name__ == "__main__":

    import calculator
    calculator.display_text.push_right()

    clock = pygame.time.Clock()

    while calculator.calculator_window.running:

        clock.tick(150)

        calculator.calculator_window.run()
