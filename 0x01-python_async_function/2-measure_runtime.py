#!/usr/bin/env python3
'''Task 2: Calculate the execution time
'''

import asyncio
import time

# Importing the 'wait_n' function from the previous task
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Calculates the average time taken to execute wait_n.
    '''
    start_time = time.time()  
    asyncio.run(wait_n(n, max_delay))  
    elapsed_time = time.time() - start_time  
    return elapsed_time / n  
