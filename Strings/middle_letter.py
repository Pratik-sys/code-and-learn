#!/usr/bin/python3

# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

"""
For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""


def mid(s):
    """
    s : string
    return a : string
    """
    for i in range(len(s)):
        if len(s) % 2 == 0:
            return "no mid for even length"
    return s[len(s) // 2]


print(mid("hello"))

