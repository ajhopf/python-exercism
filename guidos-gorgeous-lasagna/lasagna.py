"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time in minutes based on the number of layers

    :param number_of_layers:
    :return: int - preparation time in minutes

    Function that takes the number of layers and multiply it for the average amount of time spent
    to prepare one layer (2 minutes).
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time in the making of a lasagna

    :param number_of_layers: int - number of layers in that special lasagna
    :param elapsed_bake_time: int - how many minutes have already passed since starting that wondrous meal
    :return: int - amount of time in minutes spent in the making of the lasagna

    Function that calculates the elapsed time in minutes based on the number of layers and the elapsed bake time
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
