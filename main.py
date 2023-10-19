import pygame

# TODO: kalulator jak w windows: JEDNO POLE EDYCYJNE, guziczki, PRZECINEK (lub kropka), sinusy cosinusy


def main():
    import calculator
    calculator.calculator_obj.text_obj.push_right(8)

    clock = pygame.time.Clock()

    while calculator.calculator_window.running:

        clock.tick(150)

        calculator.calculator_window.run()


if __name__ == "__main__":
    main()
