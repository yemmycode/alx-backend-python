#!/usr/bin/env python3
'''Task 0: Introduction to async in Python
Create an asynchronous function that accepts an integer parameter 
(`max_delay`, default set to 10) called `wait_random`. This function 
will pause for a random amount of time between 0 and `max_delay` seconds 
(inclusive, as a float), and then return the duration it waited.

Utilizes the `random` module for generating the delay.

'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Pauses execution for a random number of seconds.'''
    delay_duration: float = random.random() * max_delay
    await asyncio.sleep(delay_duration)
    return delay_duration
