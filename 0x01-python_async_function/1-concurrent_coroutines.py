#!/usr/bin/env python3
"""
Executing multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that takes two arguments and returns
    the lists of all the delays (float values). The list
    are in ascending order without using sort
    """
    initial_delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        initial_delays.append(wait_random(max_delay))
    for initial_delay in asyncio.as_completed(initial_delays):
        initial = await initial_delay
        all_delays.append(initial)
    return all_delays
