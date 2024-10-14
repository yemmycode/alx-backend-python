#!/usr/bin/env python3
'''Task 3: Working with asyncio Tasks
'''

import asyncio

# Importing the 'wait_random' function from the previous task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Creates and returns an asyncio Task for the wait_random coroutine.
    '''
    return asyncio.create_task(wait_random(max_delay))
