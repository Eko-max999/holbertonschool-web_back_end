#!/usr/bin/env python3
"""
Runtime ölçmə modulu
"""

import asyncio
import time

# Əvvəlki tapşırıqdan funksiyanı import edirik
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension funksiyasını 4 dəfə paralel işlədir,
    ümumi vaxtı ölçür və qaytarır.
    """
    start_time = time.perf_counter()
    
    # asyncio.gather 4 tapşırığı eyni anda (paralel) başladır
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()
    return end_time - start_time
