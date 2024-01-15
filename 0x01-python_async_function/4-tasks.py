#!/usr/bin/env python3
"""take wait_n function and alter it into a new function task_wait_n"""
import asyncio
from typing import List
take_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of all delays in ascending order"""
    list_of_delays = []
    for i in range(n):
        list_of_delays.append(await take_wait_random(max_delay))
    return sorted(list_of_delays)
