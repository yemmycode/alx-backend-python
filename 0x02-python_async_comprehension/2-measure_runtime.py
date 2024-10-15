#!/usr/bin/env python3
'''Task 2: Measure runtime for four concurrent comprehensions
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Runs async_comprehension four times concurrently and
    calculates the total elapsed time.
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
