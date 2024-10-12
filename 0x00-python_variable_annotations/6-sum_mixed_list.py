#!/usr/bin/env python3
"""Module for task 6
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function that takes a list of integers and floats, and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing both integers and floats.

    Returns:
        float: The total sum of all the values in the list.
    """
    return float(sum(mxd_lst))
