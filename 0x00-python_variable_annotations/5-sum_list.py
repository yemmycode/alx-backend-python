#!/usr/bin/env python3
"""Module for task 5
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Function that takes a list of floats and returns their total sum.

    Args:
        input_list (List[float]): A list containing float values to be summed.

    Returns:
        float: The total sum of all the floats in the list.
    """
    return float(sum(input_list))
