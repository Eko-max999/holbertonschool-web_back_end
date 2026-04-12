#!/usr/bin/env python3
"""
Async Comprehension modulu.
"""
from typing import List

# 0-async_generator-u import edirik
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asinxron generatoru işlədir və nəticələri
    async comprehension vasitəsilə siyahı kimi qaytarır.
    """
    return [i async for i in async_generator()]
