#!/usr/bin/env python3
"""
Async Comprehension modulu
"""

from typing import List

# Əvvəlki tapşırıqdan asinxron generatoru import edirik
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_generator-dan gələn 10 ədədi asinxron siyahı
    olaraq toplayır və qaytarır.
    """
    return [i async for i in async_generator()]
