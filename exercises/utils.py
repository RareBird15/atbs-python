# Copyright 2026 RareBird15
"""Utility functions for ATBS exercises."""

import logging
import sys

logger = logging.getLogger(__name__)


class NonPositiveError(Exception):
    """Exception raised when a dimension is zero or negative."""

    message: str

    def __init__(self, message: str = 'Numbers must be positive.') -> None:
        """Initialize the error with a message.

        Args:
            message (str, optional): The error message to show.
            Defaults to 'Numbers must be positive.'.
        """
        self.message = message
        super().__init__(self.message)


def get_validated_int(prompt: str, min_value: int | None = 1) -> int:
    """Prompt for an integer and validate it against a minimum value.

    Args:
        prompt: The message to display to the user.
        min_value: The lowest allowed number. Set to None for no minimum.

    Returns:
        A validated integer.
    """
    while True:
        try:
            logger.info(prompt)
            user_input = input()
            value = int(user_input)

        except ValueError:
            logger.warning('Invalid input. Please enter a whole number.')
        else:
            if min_value is not None and value < min_value:
                logger.warning('Please enter a number no less than %d.', min_value)
                continue
            return value


def pause() -> None:
    """Wait for the user to press Enter before continuing."""
    logger.info('\nPress Enter to continue...')
    input()


def print_header(title: str, char: str = '=') -> None:
    """Print a centered header with decorative characters.

    Args:
        title: The text to display.
        char: The character used for the line (default is '=')
    """
    width = 40
    # We use .info so Ruff doesn't complain about print()
    logger.info('')  # Empty line for spacing
    logger.info(char * width)
    logger.info(title.center(width))
    logger.info(char * width)
    logger.info('')


def setup_exercise_logging() -> None:
    """Set up a consistent logging format for all ATBS exercises."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        stream=sys.stdout,
    )
