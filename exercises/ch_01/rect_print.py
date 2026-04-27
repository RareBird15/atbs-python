# Copyright 2026 RareBird15
"""Prints a rectangle of height 5 and the given width."""

import logging
import sys

# Configure logging to output to the console (stdout)
logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)

RECTANGLE_HEIGHT = 5


def get_rectangle_width() -> int:
    """Prompt for the rectangle width and return it as an integer.

    Returns:
        The width of the rectangle.
    """
    while True:
        user_input = input('Enter the width of the rectangle: ')
        try:
            # Attempt to convert the input to an integer
            width = int(user_input)
        except ValueError:
            # If the conversion fails, inform the user and prompt again
            logger.exception(
                'Invalid input. Please enter a valid integer for the width.',
            )
        else:
            # Check if the width is a positive integer
            if width <= 0:
                logger.warning('Please enter a positive integer for the width.')
                continue
            return width


def print_rectangle(width: int) -> None:
    """Print a rectangle of the given width and height 5 made up of O characters.

    Args:
        width: The width of the rectangle.
    """
    for _ in range(RECTANGLE_HEIGHT):
        logger.info('O' * width)


def main() -> None:
    """Run the rectangle printing program."""
    width = get_rectangle_width()
    print_rectangle(width)


if __name__ == '__main__':
    main()
