#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Measure the runtime"""
    s = time.perf_counter()
    res = await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapsed = time.perf_counter() - s
    return elapsed
