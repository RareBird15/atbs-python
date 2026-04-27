# Copyright 2026 RareBird15
"""Return the perimeter and area of a rectangle given its length and width."""

import logging
import sys

# Configure logging to output to the console (stdout)
logging.basicConfig(level=logging.INFO, format='%(message)s', stream=sys.stdout)
logger = logging.getLogger(__name__)


def get_dimension(label: str) -> int:
    """Prompt the user for a dimension and return it as an integer.

    Args:
        label (str): The name of the dimension, like 'width' or 'length'.

    Returns:
        int: The validated integer dimension provided by the user.
    """
    while True:
        user_input = input(f'Enter the {label} of the rectangle: ')
        try:
            value = int(user_input)
        except ValueError:
            logger.exception(
                'Invalid input. Please enter a valid integer for the %s.',
                label,
            )
        else:
            if value <= 0:
                logger.warning('Please enter a positive integer for the %s.', label)
                continue
            return value


def calculate_perimeter(length: int, width: int) -> int:
    """Calculate the perimeter of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """
    return 2 * (length + width)


def calculate_area(length: int, width: int) -> int:
    """Calculate the area of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    return length * width


def main() -> None:
    """Run the perimeter and area calculator program."""
    length = get_dimension('length')
    width = get_dimension('width')

    perimeter = calculate_perimeter(length, width)
    area = calculate_area(length, width)

    logger.info('The perimeter of the rectangle is: %d', perimeter)
    logger.info('The area of the rectangle is: %d', area)


if __name__ == '__main__':
    main()
