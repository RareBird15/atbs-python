# Copyright 2026 RareBird15
"""Prints a rectangle of height 5 and the given width."""

import logging

from exercises.utils import get_validated_int, setup_exercise_logging

# Configure logging to output to the console (stdout)
logger = logging.getLogger(__name__)

RECTANGLE_HEIGHT = 5


def print_rectangle(width: int) -> None:
    """Print a rectangle of the given width and height 5 made up of O characters.

    Args:
        width: The width of the rectangle.
    """
    for _ in range(RECTANGLE_HEIGHT):
        logger.info('O' * width)


def main() -> None:
    """Run the rectangle printing program."""
    setup_exercise_logging()
    logger.info('Welcome to the rectangle printer!')
    width = get_validated_int('Enter the width of the rectangle:')
    print_rectangle(width)


if __name__ == '__main__':
    main()
