import pygame

# TODO wykresy, zaznacza dokładnie na wykresie wartość x i y trygonometrycznych, używaj pygame.draw.line()
# TODO wykres funkcji kwadratowej, zaznacza pierwiastki rzeczywiste


def main():
    import calculator
    calculator.calculator_obj.text_obj.push_right(8)

    clock = pygame.time.Clock()

    while calculator.calculator_window.running:

        clock.tick(150)

        calculator.calculator_window.run()


if __name__ == "__main__":
    main()
