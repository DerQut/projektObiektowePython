import pygame

if __name__ == "__main__":

    import calculator

    clock = pygame.time.Clock()

    while calculator.calculator_window.running:

        clock.tick(150)

        calculator.calculator_window.run()
