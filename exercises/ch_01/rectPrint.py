"""Prints a rectangle of height 5 and the given width."""

RECTANGLE_HEIGHT = 5


def get_rectangle_width() -> int:
    """Prompts the user for the rectangle width and returns it as an integer."""
    while True:
        user_input = input('Enter the width of the rectangle: ')
        try:
            # Attempt to convert the input to an integer
            width = int(user_input)
        except ValueError:
            # If the conversion fails, inform the user and prompt again
            print('Invalid input. Please enter a valid integer for the width.')
        else:
            # Check if the width is a positive integer
            if width <= 0:
                print('Please enter a positive integer for the width.')
                continue
            return width


def print_rectangle(width: int) -> None:
    """Prints a rectangle of the given width and height 5 made up of O characters.

    :param width: The width of the rectangle
    :type width: int
    """
    for _ in range(RECTANGLE_HEIGHT):
        print('O' * width)


def main() -> None:
    """The main function of the program."""
    width = get_rectangle_width()
    print_rectangle(width)


if __name__ == '__main__':
    main()
