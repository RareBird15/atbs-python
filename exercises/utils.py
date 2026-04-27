# Copyright 2026 RareBird15
"""Utility functions for ATBS exercises."""

import logging
import sys


def setup_exercise_logging() -> None:
    """Set up a consistent logging format for all ATBS exercises."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        stream=sys.stdout,
    )
