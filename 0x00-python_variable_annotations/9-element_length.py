#!/usr/bin/env python3
"""Module for Task 9
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Generates a list of tuples, where each tuple includes a string 
    from the provided list along with its length.

    Args:
        lst (Iterable[Sequence]): The collection of strings to evaluate.

    Returns:
         List[Tuple[Sequence, int]]: A list of tuples, each consisting of 
         a string from the original collection and its corresponding length.
    """
    return list(map(lambda i: (i, len(i)), lst))

