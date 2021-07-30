#!/usr/bin/env python3
"""The basic of async syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an integer argument
    max_delay with a degaukt value of 10 named wait_random
    that waits for a random delay between 0 and max_delay
    included and float value seconds and eventually returns it
    """
    rand_float = random.uniform(0, max_delay)
    await asyncio.sleep(rand_float)
    return rand_float
