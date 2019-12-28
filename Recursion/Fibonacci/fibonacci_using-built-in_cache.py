#!/usr/bin/python3

# Write a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2.

"""
Input: 100
Output : 437845991669110338052
"""

# Solution: Method 3 ( Use in-built cache )

from functools import lru_cache # LRU stands for Least Recently USed Cache. ist's an in-built function.

@lru_cache(maxsize = 1000) # Define the cache, default python will cache 128 most  recently used value.

def fib(n):
    """
    This function returns the the fibonaaci number
    """
    # check whether ther input is positive integer
    if type(n) != int:
        raise TypeError("n must be a integer")
    if n < 1:
        raise TypeError("n must be postive integer")

    # Compute the nth term.
    if n == 1:
        return 0
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n - 1) + fib(n - 2)


print(fib(100))
