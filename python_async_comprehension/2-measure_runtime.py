#!/usr/bin/env python3
"""
Runtime ölçmə modulu
"""

import asyncio
import time
from typing import List

# Əvvəlki tapşırıqdan funksiyanı dinamik olaraq import edirik
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension-u 4 dəfə paralel işlədir və ümumi vaxtı ölçür.
    Netice ~10 saniyə olmalıdır, çünki hamısı eyni vaxtda (paralel) işləyir.
    """
    start_time = time.perf_counter()
    
    # 4 paralel çağırış üçün asyncio.gather istifadə edirik
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    return end_time - start_time
