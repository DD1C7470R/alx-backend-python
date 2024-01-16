#!/usr/bin/env python3
"""Basic Async Syntax"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(0, 10):
        i = random.uniform(0, 10)
        yield i
        await asyncio.sleep(1)
