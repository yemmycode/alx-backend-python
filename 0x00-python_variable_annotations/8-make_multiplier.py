#!/usr/bin/env python3
"""Module for task 8
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that takes a float multiplier and returns another function 
    to multiply a given float by the multiplier.

    Args:
        multiplier (float): The value to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
