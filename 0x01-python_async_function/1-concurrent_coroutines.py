#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """Wait for a random delay between 0 and max_delay seconds."""
    delay = []
    for _ in range(n):
        delay.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delay)]
