# Copyright 2026 RareBird15
"""Return the perimeter and area of a rectangle given its length and width."""

import logging

from exercises.utils import NonPositiveError, get_validated_int, setup_exercise_logging

# Configure logging to output to the console (stdout)
logger = logging.getLogger(__name__)


class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, length: int, width: int) -> None:
        """Initialize the rectangle and validate dimensions.

        Args:
            length (int): The length of the rectangle.
            width (int): The width of the rectangle.

        Raises:
            NonPositiveError: If either dimension is not positive.
        """
        if length <= 0 or width <= 0:
            # Here we use your custom error!
            raise NonPositiveError

        self.length = length
        self.width = width

    def area(self) -> int:
        """Calculate the area.

        Returns:
            int: The area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self) -> int:
        """Calculate the perimeter.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)


def main() -> None:
    """Run the perimeter and area calculator program."""
    setup_exercise_logging()
    logger.info('Starting calculation...')

    length = get_validated_int('Enter the length of the rectangle:')
    width = get_validated_int('Enter the width of the rectangle:')

    try:
        rect = Rectangle(length, width)
        logger.info('Area: %d', rect.area())
        logger.info('Perimeter: %d', rect.perimeter())
    except NonPositiveError:
        logger.exception('Calculation failed')


if __name__ == '__main__':
    main()
