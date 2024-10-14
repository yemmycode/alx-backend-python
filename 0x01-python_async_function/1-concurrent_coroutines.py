#!/usr/bin/env python3

'''Task 1: Running multiple coroutines concurrently with async
'''

import asyncio
from typing import List

# Importing the 'wait_random' function from the previous task
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns a sorted list of all the wait durations (as float values)
    '''
    delays = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )

    return sorted(delays)

