#!/usr/bin/env python3
'''Module for Task 4: Managing multiple tasks
'''

import asyncio
from typing import List

# Importing the 'task_wait_random' function from the previous task
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Runs task_wait_random concurrently n times and returns the sorted results.
    '''
    delays = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(delays)
