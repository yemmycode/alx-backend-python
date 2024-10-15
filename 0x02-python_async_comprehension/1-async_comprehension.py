#!/usr/bin/env python3
'''Task 1: Asynchronous Comprehensions
This module imports async_generator from the previous task and defines a coroutine 
called async_comprehension, which takes no arguments.

The coroutine collects 10 random numbers by using asynchronous 
comprehension over async_generator and returns the list of 10 random numbers.
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''Generates a list of 10 random numbers from an asynchronous generator.
    '''
    return [number async for number in async_generator()]
