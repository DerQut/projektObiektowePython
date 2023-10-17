import pygame

if __name__ == "__main__":

    import calculator

    while calculator.calculator_window.running:

        clock = pygame.time.Clock()
        clock.tick(150)

        calculator.calculator_window.run()
