#!/usr/bin/env python3
'''Task 0: Asynchronous Generator Example
'''
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    '''This coroutine loops 10 times asynchronously,
    waiting for 1 second each time and yielding a random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
