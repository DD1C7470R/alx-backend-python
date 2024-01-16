#!/usr/bin/env python3
"""Basic Async Syntax"""
import asyncio
from index import async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10"""
    result = [i async for i in async_generator()]
    return result
