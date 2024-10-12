#!/usr/bin/env python3
"""Module for task 7 - string and int/float to tuple
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that takes a string and a number (int or float) and returns a tuple.

    Args:
        k (str): The string to be part of the tuple.
        v (Union[int, float]): The integer or float to square for the tuple.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string, 
        and the second is the squared value of the integer or float.
    """
    return (k, float(v**2))
