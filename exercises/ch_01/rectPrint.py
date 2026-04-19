"""Prints a rectangle of height 5 and the given width."""

RECTANGLE_HEIGHT = 5


def getRectangleWidth() -> int:
    """Prompts the user for the rectangle width and returns it as an integer."""
    return int(input('Enter the rectangle width: '))


def printRectangle(width: int) -> None:
    """Prints a rectangle of the given width and height 5 made up of O characters.

    :param width: The width of the rectangle
    :type width: int
    """
    for _ in range(RECTANGLE_HEIGHT):
        print('O' * width)


def main() -> None:
    """The main function of the program."""
    width = getRectangleWidth()
    printRectangle(width)


if __name__ == '__main__':
    main()
